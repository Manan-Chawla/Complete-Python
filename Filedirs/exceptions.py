try:
    nums=int(input("Enter a number : "))
    print(1/nums)
except ZeroDivisionError:
    print("We can't divide number by zero")
except ValueError:
    print("Enter a numberical value only ")
except Exception:
    print("Something went wrong")
finally:
    print("Need to do more examples")