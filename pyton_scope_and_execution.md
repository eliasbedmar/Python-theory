Running Python
* Scripts vs Modules:
    * Scripts - plain text file (.py) to be executed directly by user - top-level program file
    * Modules - plain text file (.py) to be imported and used from another Python file (script or module)
* Python interpreter - later of software between code and machine (code in Python is converted into machine-readable code). Any code you run must be ran via the interpreter. In compiled programming languages, the equivalent to the interpreter is the compiler.
    * The Python interpreter can be a program written in different languages - C (CPython), Java (JYthon), Python (PyPy), .NET (IronPython.
* Execution modes: 2 ways to run code using the interpreter (execution modes):
    * Running a script or a module in the CLI “statically”:
python filename.py
    * Importing a Module into another Module/Script or Typing in code directly into an interactive interpreter session
import child_module from library

elias.bedmar.fresneda@ibm.com@ip-192-168-0-11  ~  python
Python 3.7.2 (default, Feb 13 2020, 17:10:23)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print('This is code run via an interactive Python interpreter')
* You can use an IDE - Integrated Development Environment that contains the Interpreter, Edit features…so you can write code and Run directly

main() function
* main() function - Entry point for many programming languages (called automatically by OS, Not for Python)
    * where the first instructions of a program are executed
    * where the program has access to command line arguments
* In Python - Python interpreter executes scripts starting at the top of the file - no specific function that gets executed automatically
* However - useful to have main() within Python - common pattern in Python files that you want to be executed as a script and imported in another module

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

* __name__ - Special variable Python always defines - Value depends on how code is being executed
    * repr(__name__) - will show the representation of the object __name__ as a string

Value of __name__
* "A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt."
* Depends on execution mode:
    * CLI: __name__ = ‘__main__'
    * Importing a module into another Module or into Interactive Interpreter: __name__ = '__childmodulefilename__'
        * If the module gets imported again - it won’t be run as a script again. i.e. Modules imported only get executed once.

Best practices
* Making code that can run as a script AND as a module imported into another module/interactive session - best practices:
    * Put most code into a Function or Class
    * Using __name__ to control execution of code
    * Create function main() to contain the code to be run
    * Call other functions from main()

1. Putting most code into Function/Class
    * When Python encounters def/Class - it stores the definition. It doesn’t execute unless instructed to do so. Especially for resource intensive code.
    * These can then be imported into other modules/scripts - and executed (execute functions/create objects)
2. Using if __name__ == “main” to control the Execution of your code
    * That constrains the module code to run only when __name__ is equal to “”__main__: i.e. when the script is run from the CLI, not when being imported. Conditional running of modules.
3. Create a function called main() to contain code you want to run
    * entry point to code - starting point of the code that accomplishes primary task
    * It should contain any code you want to run when the Python interpreter esecutes the file
    * Better than putting the code directly into - if __name__ conditional block - as this way the user can reuse main() if they import the module.
4. Call other functions from main()
    * Calling other functions from main() instead of having the ’task-accomplishing’ code in main()
    * Useful when you can compose the overall task from several smaller sub-task that can execute independently
        * All sub-tasks to be defined as different functions
        * Easier for user/others to re-use only parts of the steps if they want
        * main() -> to contain the ‘default’ workflow, so the whole process can be used


See module.py

```buildoutcfg
from time import sleep

print("This is my file to demonstrate best practices.")

print("The value of __name__ is:", repr(__name__))

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the Web"
    return data

def write_data_to_database(data):
    print("Writing data to database:")
    print(data)

# Def function [entry point] with default workflow
def main():
    data = read_data_from_web()
    modified_data=process_data(data)
    write_data_to_database(modified_data)

if __name__ == '__main__':
    main()

```

See script.py
```buildoutcfg
import module as module

print('This is the script calling a module')

print('Execution mode for script - value of __name__:',repr(__name__))

#Running whole workflow from module:
print('Running whole workflow:')
module.main()

#Running selected functions() from module
inputdata = 'Input custom data'
print('Running parts of the workflow for data',inputdata)

modified_data=module.process_data(inputdata)
module.write_data_to_database(modified_data)

```

See scope.py
```buildoutcfg
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"

    do_local()
    print("After local assignment: ", spam)

    do_nonlocal()
    print("After nonlocal assignment: ", spam)

    do_global()
    print("After global assignment: ", spam)


scope_test()
print("In global scope:", spam)

```