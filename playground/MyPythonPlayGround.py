class MyPythonPlayGround:
    # Integers and Floats
    # The format here is: Variable Name = Variable Value
    answer = 42

    # We can also have floats
    pi = 3.14159

    # Don't worry about conversion
    print(answer + pi)  # 45.14159

    # Casting
    int(pi) == 3
    float(answer) == 42.0

    # Strings are defined using single, double or triple quotes
    'Hello World' == "Hello World" == """Hello World"""

    # Useful Methods
    print("hello".capitalize())
    print("hello".replace("e", "a"))
    print("hello".isalpha())
    print("123".isdigit())
    print("some, csv, example".split(","))

    # String format function
    name = "Artemas"
    machine = "HAL"
    print("Nice to meet you {0}. I am {1}".format(name, machine))
    print(f"Nice to meet you {name}. I am {machine}")  # Notice the 'f' at the beginning of the String

    # Boolean and None
    python_course = True
    java_course = False
    print(int(python_course))  # 1
    print(int(java_course))  # 0
    print(str(python_course))  # "True"

    aliens_found = None  # None == null in other languages.

    # If Statements
    number = 5
    if number == 5:
        print("Number is 5")
    else:
        print("Number is NOT 5")

    # Truthy and Falsy Values
    number = 5
    if number:
        print("Number is defined and truthy")

    text = "Python"
    if text:
        print("Text is defined and truthy")

    number = 3
    python_course = True
    if number == 3 and python_course:
        print("This will execute")

    if number == 17 or python_course:
        print("This will also execute")

    # Ternary If Statements
    a = 1
    b = 2
    print("bigger" if a > b else "smaller")
    print("smaller" if a or b else "There is nothing")