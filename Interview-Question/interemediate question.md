# **Python Intermediate Question with Answer**
---
1. **What are function in python?**

   Function are refer as reusable block of code that perform specific tasks.
   ```
   def add(a,b):
       return a+b
   print(add(3,4))
   ```

2. **What are *args and kwargs?**
   
   These allow flexible argument passing.
   1. *args collects non-keyword arguments as a tuple
   2. **kwargs collect keyword arguments as a dictionary
      ```
      def details(*args, **kwargs):
          print(args)
          print(kwargs)
      details(10,20,name="manan", age=22)
      ```

3. **What is the difference between return and yield?**

   1. returns end the function and returns a value immediately
   2. yield turns a function into a generator that returns values one by one
      ```
      def sq(n):
          for i in range(n):
              yield i * i
      ```

4. **What are lambda function?**

   A lambda function is one line anonymous function defined using the keyword lambda.
   ```
   sq = lambda x: x: **2
   print(sq)
   ```
   They are often use with map(), filter() and reduce() for concise operation.

5. **What are python modules and packages?**

   A module is a python file containing function, classes and variable.
   While a package is collection of modules organized in directories.
   ```
   import math
   print(math.sqrt(16))
   ```
   We can create custom modules by saving your function in a .py file and importing them elsewhere.

6. **What is the difference between deep copy and shallow copy?**

   1. Shallow copy
      A. It copies only object references
      B. Changes reflect in original
      C. Created using copy.copy()
   2. Deep Copy
      A. Copies entire object recursively
      B. Independent copy
      C. Created using copy.deepcopy()

    ```
    import copy
    list1=[[1,2],[3,4]]
    shallow=copy.copy(list1)
    deep=copy.deepcopy(lis1)
    ```

7. **What are Python exceptions?**

    Exception handle runtime errors gracefully.
    ```
    try: 
         print(10 / 0) 
    except ZeroDivisionError: 
         print("Cannot divide by zero") 
   finally: 
         print("Operation complete")
    ```
    Common exception includes:-
    1. ValueError
    2. TypeError
    3. IndentationError
    4. FileNotFoundError
    5. IndexError

8. **What are python decorators?**

   Decorators modify the behavior of a function without changing its code.
   ```
   def greet(func):
       def wrapper():
           print("hi")
           func()
       return wrapper
   @greet
   def say_name():
       print("Bella")
   say_name()
   ```
   Decorators are used in framework like django, flask for authentication and logging.


9. **What are iterators and generators?**

    1. Iterators -- an object implementing __iter__() and __next__()
    2. Generators -- a function that yields values using yield
    ```
    mylist=[1,2,3]
    iterator=iter(mylist)
    print(next(iterator))
    ```
    Generators save memory as they dont store all data at once.

10. **What are commonly used built in function in python?**

    <table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>len()</code></td>
      <td>Returns length</td>
    </tr>
    <tr>
      <td><code>type()</code></td>
      <td>Returns data type</td>
    </tr>
    <tr>
      <td><code>sum()</code></td>
      <td>Sums all elements</td>
    </tr>
    <tr>
      <td><code>max() / min()</code></td>
      <td>Finds largest/smallest</td>
    </tr>
    <tr>
      <td><code>sorted()</code></td>
      <td>Returns sorted list</td>
    </tr>
    <tr>
      <td><code>range()</code></td>
      <td>Generates number sequence</td>
    </tr>
    <tr>
      <td><code>dir()</code></td>
      <td>Lists available attributes</td>
    </tr>
    <tr>
      <td><code>help()</code></td>
      <td>Displays documentation</td>
    </tr>
  </tbody>
</table>



    
