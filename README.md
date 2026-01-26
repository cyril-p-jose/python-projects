# Python Programming Repository

A curated collection of **Python programs** focused on building a strong foundation in  
**core programming concepts** through simple, readable, and beginner-friendly code.

---

## 📌 Overview

This repository contains Python programs created for:

- Academic learning  
- Programming practice  
- Laboratory exercises  
- Concept revision  

All programs are written with clarity and simplicity in mind, making them suitable for beginners.

---

## 🧩 Topics Covered

- Basic Input / Output  
- Conditional Statements  
- Loops and Iterations  
- Functions  
- Pattern Programs  
- Number-based Programs  
- Simple Games and Logic Programs  
- More Python programs will be added over time  

---

## 📝 Sample Snippet

**Number Guessing Game (Basic Logic)**

```python
import random

number = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too small.")
    else:
        print("Too large.")
