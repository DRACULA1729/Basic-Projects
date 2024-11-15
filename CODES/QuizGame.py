
print("Welcome to the Quiz Game!\n Hope you were having a fine day senora!")
name=input("What can i call you?").title()
print(f"Hello {name} lets get started with the quiz game\n")
# List of questions, options, and answers
print("Are you ready? (Enter to proceed/ CTRL+C to stop)")
#ask a question
i=0
print("Let's Solve some questions!")
score=0
   
print('''1. What is the largest planet in our solar system?
A) Earth
B) Saturn
C) Jupiter
D) Uranus''')
answer=input("Enter answer: ").lower().strip()

if answer=='c':
   score+=1
else:
   print("Your answer is wrong!")
print('''2. Which programming language is used for web development?
A) Java
B) Python
C) JavaScript
D) C++''')
answer=input("Enter answer: ").lower().strip()
if answer=='c':
   score+=1
else:
   print("Your answer is wrong!")
print('''3. What is the process of water moving through plants?
A) Respiration
B) Photosynthesis
C) Transpiration
D) Evaporation
''')
answer=input("Enter answer: ").lower().strip()
if answer=='c':
   score+=1
else:
   print("Your answer is wrong!")

print('''4. Which river is the longest in the world?
A) Nile
B) Amazon
C) Yangtze
D) Mississippi''')
answer=input("Enter answer: ").lower().strip()
if answer=='a':
   score+=1
else:
   print("Your answer is wrong!")
print('''5. Who was the first President of the United States?
A) George Washington
B) Thomas Jefferson
C) Abraham Lincoln
D) Franklin D. Roosevelt''')
answer=input("Enter answer: ").lower().strip()
if answer=='a':
   score+=1
else:
   print("Your answer is wrong!")

print('''6. Who wrote the famous novel "To Kill a Mockingbird"?
A) F. Scott Fitzgerald
B) Harper Lee
C) Jane Austen
D) J.K. Rowling''')
answer=input("Enter answer: ").lower().strip()

if answer=='b':
   score+=1
else:
   print("Your answer is wrong!")
print('''7. Which city is the capital of France?
A) Berlin
B) Paris
C) London
D) Rome''')
answer=input("Enter answer: ").lower().strip()

if answer=='d':
   score+=1
else:
   print("Your answer is wrong!")


print('''8. Which artist painted the famous painting "The Starry Night"?
A) Leonardo da Vinci
B) Vincent van Gogh
C) Pablo Picasso
D) Claude Monet''')
answer=input("Enter answer: ").lower().strip()

if answer=='b':
   score+=1
else:
   print("Your answer is wrong!")
print('''9. Who wrote the famous play "Romeo and Juliet"?
A) William Shakespeare
B) Christopher Marlowe
C) John Milton
D) Geoffrey Chaucer''')
answer=input("Enter answer: ").lower().strip()

if answer=='a':
   score+=1
else:
   print("Your answer is wrong!")
        
print('''10. What is the value of x in 2x + 5 = 11?
A) 2
B) 3
C) 4
D) 5''')
answer=input("Enter answer: ").lower().strip()

if answer=='c':
   score+=1
else:
   print("Your answer is wrong!")
 
print(f'Hope you had a great time with us! Here is your score {score}.\n B BYE!\n PEACE OUT!!! ')
   
    
