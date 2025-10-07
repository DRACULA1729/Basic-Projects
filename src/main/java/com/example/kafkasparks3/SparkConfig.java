package com.example.kafkasparks3;

import org.apache.spark.SparkConf;
import org.apache.spark.sql.SparkSession;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SparkConfig {

    @Value("${spark.app.name}")
    private String appName;

    @Value("${spark.master.uri}")
    private String masterUri;

    @Value("${aws.access.key.id}")
    private String awsAccessKey;

    @Value("${aws.secret.access.key}")
    private String awsSecretKey;

    @Bean
    public SparkSession sparkSession() {
        SparkConf conf = new SparkConf()
                .setAppName(appName)
                .setMaster(masterUri);

        // Configure Hadoop to use S3A and provide AWS credentials
        conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem");
        conf.set("spark.hadoop.fs.s3a.access.key", awsAccessKey);
        conf.set("spark.hadoop.fs.s3a.secret.key", awsSecretKey);

        return SparkSession.builder()
                .config(conf)
                .getOrCreate();
    }
}