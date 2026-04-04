# **Python Interview Question with Answers**
---

## **Beginner Level**
1. **What is Python?**
   
   Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.
   Python emphasizes code clarity and lets you write programs with fewer lines than many other languages.
   Python supports mutiple programming paradigms which includes
   1. Procedural Programming meaning writing function
   2. OOPS meaning using classes and object
   3. Functional Programming meaning using high order function like map, filter and reduce
  
3. **What are python's key feature?**
   
   It offer following feature :-
   1. Simple and readable syntax: You can focus on solving problems instead of dealing with complex code structures. 
   2. Interpreted language: Code runs line by line, making debugging easier.
   3. Dynamically typed: You don’t need to declare variable types.
   4. Extensive standard library: Built-in modules like math, os, and datetime save time.
   5. Cross-platform: Works on Windows, macOS, and Linux.
   6. Open-source: Free to use and supported by a large community.
   7. Object-oriented: Everything in Python is an object.

4. **What are python data types?**
   
   1. Numeric -- int, float and complex
   2. Sequence -- str, list, tuple and range
   3. Mapping -- dict
   4. Set -- set, Fronzenset
   5. Boolean -- bool
   6. Binary -- Bytes, bytearray

6. **What is the difference between mutable and immutable data types?**
   
   Mutable are types ideal when you need to update data, while immutable types are safer for integrity

7. **What are Variables in python?**
   
   Variables are container that stores data values, we dont have to declare their type explicitly as python infers it.
   ```
   name = "Manan"
   age = 25
   is_Student=False
   ```
   Variables follow the naming rules :-
   1. Must start with a letter or underscore
   2. Cannot start with a number
   3. Are case sensitive


6. **Explain indentation in python**
   
   Python uses indentation or spaces to define code blocks instead of braces, The standard indentation is 4 spaces
   ```
   if True:
      print("Hello")
   print("No hello")
   ```
   Incorrect indentation raises an indentationerror. Consistent indentation improves readability and enforces structure.

7. **What are lists and tuples?**

   Both list and tuples store ordered collection of data, but they differ in mutability
   List are mutable in nature, represent by '[]' and are slower in speed and generally use when data changes.
   While on other hand Tuple are immutable in nature, represent by '()' and faster in speed and uses when data remains constant.

8. **What is a dictionary in python?**
   
   A dictionary stores key-value pairs and allows fast lookups.
   ```
   student={ "name":"Bella", "age":20, "grade":"A" }
   ```
   Dictionary are mutable, unordered and indexed by a key. A key must be immuntable type like string, numbers or tuples.

9. **What are conditional statements in python?**

    Conditional statements control program flow based on conditions.
    There are three main type of it:-
    1. If
    2. if-else
    3. if-elif

10. **What are loops in python?**
    Loops execute a block of code multiple times.
    ``` py
    for i in range(3):
        print(i)

    count=0
    while count <3:
       print(count)
       count +=1
    ```
