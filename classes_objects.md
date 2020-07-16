# Classes - Introduction
* Classes - bundling data and functionality.
* Create a Class = Create new Type of Object -> allowing new Instances of that Object
* Class Instances:
    * Attributes (maintaining its state)
    * Methods, defined by its Class (modifying its state)
* OOP features for Python Classes:
    * Class inheritance - allows multiple base classes
    * Derived class - override any methods of its base class/classes
    * Method - can call the method of a base class with the same name
* Names and Objects - Multiple names (in multiple scopes) - can be bound to the same object
* All values - Objects - therefore have a class (or type). This is stored as a method:
    * object.__class__

**Python Scope and Namespaces**
* Namespaces - Mapping from names to objects
    * There is no relation whatsoever between names in different Namespaces -> prefixing is needed to access attributes
    * Normally Python dictionaries. 
    * Used for
        * Built-in names and functions
        * Global names in a module
        * Local names in function invocation
    * Created at different moments and have different lifetimes.
        * Built-in names - created when interpreter starts, never deleted
        * Global namespace for module - created when module definition read in
        * Local namespace for function - created when function is called, and deleted when the function returns/raises an exception that is not handled
* Attribute - any name following a dot. e.g:
    * z.real - real is an attribute of object z
    * modname.funcname - funcname is an attribute of the module modname Object.
    * Attributes may be read-only or writable.
        * Writable attributes -> can be assigned and deleted (del())
        * Module attributes - writable
* Scope
    * Textual region of a Python programme where a namespace is directly accessible (i.e. an unqualified reference to a name attempts to find the name in the namespace)
    * Determined statically, used dynamically - at any time during execution there are at least 3 nested scopes whose namespaces are directly accessible. Searched in this order:
        * Innermost scope - local names [normally defined variables]
        * Scopes of enclosing functions - contains non-local and non-global names [nonlocal]
        * Next-to-last scope - current module’s global names [global]
        * Outermost scope - namespace containing all built-in names
    * Names can be declared - global/local
        * global - variable to live in the global scope (module’s global names)
        * nonlocal - variable to live in an enclosing scope
        * If no global/nonlocal is in effect - assignment to names always go to the innermost scope.
    * Functions: their global scope of a function defined in a module is that module’s namespace, no matter from where or by what alias the function is called.


**Class definition**
* Class definition syntax
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
    * Statements:
        * Function definitions
        * Other statements
    * When a new Class definition is entered - New Namespace is created -> used as the local scope
        * All assignments to local variables go into this new namespace
        * Function definitions bind the name of the new function here (to this namespace)
    * When a Class definition is left (normally):
        * a Class Object is created (wrapper around the contents of the namespace created by the name definition)
        * The original local scope (just in effect before the class definition was entered) is reinstated
        * The Class Object is bound here to the class name given in the class definition header.

**Class Objects**
* Class Objects - wrapper around the contents of the namespace created by the name definition
```
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
* Support 2 operations: references and instantiation
* Attribute references
    * Standard syntax used for all attribute references in Python (obj.name)
    * Valid attribute names - all names that were in the class’s namespace when the Class Object was created
    * Class attributes can be assigned to (can change attributes)
    * Attribute references:
MyClass.i
MyClass.f

* Class Instantiation
    * Function notation
```
x=MyClass()
    * Creates new instance of the class and assigns this object to the local variable x
    * The instantiation operation above (calling a class object) - creates “empty object”. Many classes like to create objects with instances customised to a specific initial state. Therefore, a class may define a special method named __init__(). This method uses self to create attributes of class instances.
        * When a class defines __init__(), class instantiation automatically invokes init() for the newly created class instance.
        * __init__() - constructor function
    * Simple __init__:
def __init__(self):
    self.data = []
    * More complex __init__:
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        * Instantiation:
x = Complex(3.0, -4.5)
print(x.r, x.i)
>>(3.0, -4,5)
```

**Instance Objects**
* Instance Objects - instantiation of Class Objects
* 2 types of valid attribute names for Instance Objects: data attributes and methods
* Data Attributes - 
    * Instance variables - like local variables, they sprint into existence when they are first assigned to
* Methods
    * Functions that “belong” to an Object
    * By definition - All attributes of a class that are function objects define corresponding methods of its instances.
    * First attribute - self (convention)
    * Any Class attributes that refer to Function Objects -> are All methods of Instance Objects of that Class [Method Objects]
* Method Objects
    * When a non-data attribute of an instance is referenced, the instance’s class is searched. 
        * If the name denotes a valid class attribute that is a Function Object: 
            * An abstract Method Object is created - by creating:
                * Pointer to Instance Object
                * Pointer to Function Object (of Class Object)
            * When this Method Object is called with an argument list, a new argument list is constructed with the Instance Object + new Argument List
                * The Function Object is called
    * Methods can call other methods
    * Methods may reference global names in the same way as ordinary functions -> Scope of method - Module enclosing its definition, not the Class



Class and Instance Variables
* Class variables - to store attributes and methods shared by all instances of the class
* Instance variables - to store data unique to instance

```buildoutcfg
class Dog:
    kind = ‘canine’               #Class variables shared by all instances
    
    def __init__(self, name):     #Instance variables unique to each instance
        self.name = name
        self.tricks = []
    
    def add_trick(self,trick):
        self.tricks.append(trick)
```
* If the same attribute name occurs both in an instance and class - the priority is the instance attribute

Class Inheritance
* Derived Class Definition and execution:
```buildoutcfg
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
class DerivedClassName(module_name.BaseClassName)

* Derived Class __init__() also created, and the __init__() of base class can be called in to inherit everything in __init__():
# child class
```buildoutcfg
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")
```
* When the Derived Class Object is constructed - the Base Class is remembered
    * This is used for resolving attribute references:
        * If a requested attribute is not found in the Derived Class -> The search proceeds to look in the Base Class
        * This search is applied recursively if the Base Class itself is based on some other Class
    * Instantiation of derived Classes - as usual:
DerivedClassName()
    * Method references - resolved:
        * Class attribute is searched, descending down the chain of Base Classes if necessary
        * The method reference is valid if it yields a Function Object
* Derived Classes can override methods of their Base Classes
    * Overriding methods in a Derived Class may want to extend rather than replace the Base Class Method. This is how the Base Class Method can be called directly:
BaseClassName.methodname(self, arguments)

* Built-in functions to work with Inheritance:
# isinstance(obj, type) - Checks an Instance’s Type: 

isinstance(Object1, int) - True if obj.__class__ is int or a Class derived from int

# issubclass(Obj1, Obj2) - Checks class inheritance

issubclass(bool, int) is True since bool is a subclass of int. 

issubclass(float, int) is False since float is not a subclass of int.

* Multiple inheritance - Definition of Class based on multiple Base Classes
```
class DerivedClassName(BaseClass1, BaseClass2, BaseClass3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

* Most basic type of Class - object Class
    * object Class - Base Class (Parent Class) for ALL Classes
    * All Python Classes have object as parent class - and they inherit all its attributes
        * ('__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', ‘__subclasshook__')

Other remarks
* Iterators
* Generators
* Generator Expressions
* Static and Class Methods


















