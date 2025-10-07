package com.example.kafkasparks3;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Service;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.time.Instant;
import java.util.concurrent.TimeoutException;

@Service
public class KafkaS3PipelineService implements CommandLineRunner, DisposableBean {

    private static final Logger logger = LoggerFactory.getLogger(KafkaS3PipelineService.class);

    @Autowired
    private SparkSession sparkSession;

    @Value("${kafka.bootstrap.servers}")
    private String kafkaBootstrapServers;

    @Value("${kafka.topic.name}")
    private String kafkaTopic;

    @Value("${kafka.consumer.group.id}")
    private String kafkaGroupId;

    @Value("${aws.region}")
    private String awsRegion;

    @Value("${aws.access.key.id}")
    private String awsAccessKey;

    @Value("${aws.secret.access.key}")
    private String awsSecretKey;

    @Value("${s3.bucket.name}")
    private String s3BucketName;

    @Value("${s3.key.prefix}")
    private String s3KeyPrefix;

    private StreamingQuery streamingQuery;

    @Override
    public void run(String... args) throws Exception {
        logger.info("Starting Kafka-Spark-S3 pipeline...");

        Dataset<Row> df = sparkSession
                .readStream()
                .format("kafka")
                .option("kafka.bootstrap.servers", kafkaBootstrapServers)
                .option("subscribe", kafkaTopic)
                .option("kafka.group.id", kafkaGroupId)
                .option("kafka.security.protocol", "SASL_SSL")
                .option("kafka.sasl.mechanism", "AWS_MSK_IAM")
                .option("kafka.sasl.jaas.config", "software.amazon.msk.auth.iam.IAMLoginModule required awsRegion=\"" + awsRegion + "\";")
                .option("kafka.sasl.client.callback.handler.class", "software.amazon.msk.auth.iam.IAMClientCallbackHandler")
                .load()
                .selectExpr("CAST(value AS STRING)");

        streamingQuery = df.writeStream()
                .foreachBatch((batchDF, batchId) -> {
                    logger.info("Processing batch ID: {}", batchId);
                    if (!batchDF.isEmpty()) {
                        String jsonOutput = "[" + String.join(",", batchDF.toJSON().collectAsList()) + "]";
                        uploadToS3(jsonOutput);
                    }
                })
                .start();

        logger.info("Pipeline started. Awaiting termination...");
        streamingQuery.awaitTermination();
    }

    private void uploadToS3(String jsonContent) {
        String fileName = s3KeyPrefix + Instant.now().toEpochMilli() + ".json";

        try (S3Client s3 = S3Client.builder().region(Region.of(awsRegion)).build()) {
            PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                    .bucket(s3BucketName)
                    .key(fileName)
                    .build();

            s3.putObject(putObjectRequest, RequestBody.fromString(jsonContent));
            logger.info("Successfully uploaded file {} to S3 bucket {}", fileName, s3BucketName);
        } catch (Exception e) {
            logger.error("Failed to upload file to S3", e);
        }
    }

    @Override
    public void destroy() {
        logger.info("Shutting down Kafka-Spark-S3 pipeline...");
        if (streamingQuery != null) {
            try {
                streamingQuery.stop();
                logger.info("Streaming query stopped successfully.");
            } catch (TimeoutException e) {
                logger.error("Timeout while stopping streaming query", e);
            }
        }
    }
}