**Objects, Values and Types**
* Objects - Python’s abstraction of data - everything in python is an object, created from the object’s blueprint Class (or a relation beween objects)
    * id(x) - memory address where object x is stored - unchangeable once object is created
    * type(x) - object’s type (object type is also an object itself) - unchangeable once object is created
    * value - can change for some objects (mutable objects), not for others (immutable) - depends on object type
        * *Mutability of object = Whether the value of an object can change.
* Containers - Object with references to other objects - Tuples, Lists, Sets, Dictionaries.
    * Value of Container = Values of contained objects, not the Identities of the contained objects.
        * Therefore - The value of an immutable container can change. This means the value(s) of the contained objects have changed, but NOT their identities.

Built-in Python types
Numberic types
* Module that defines the hierarchy of the numeric classes
* Immutable - once created, values of numeric objects cannot change
* Classes - Numbers type:
    * numbers.Number - root of the numeric hierarchy
    * numbers.Integral - represent elements from the set of integers (+ and -)
        * Integers (int)
        * Boolean (bool)
    * numbers.Real (float) - Floating point numbers
    * numbers.Complex (complex) - imaginary numbers

Sequences types
* Finite ordered sequences indexed by non-negative numbers.
* len() will return the number of items in sequence.
    * Item of len = n has the index set = 0, 1, 2, … n-1 (zero based index)
*  Immutable Sequences:
    * Objects of an immutable sequence type cannot change once it’s created.
    * If the sequence Object contains references to other objects, these may be mutable and may be changed; but the collection of objects directly being referenced cannot change (i.e. the object identities are the same, referenced by the container)
    * Types:
        * String
        * Tuples - (object0, object1, object2…) or: object0, object2, object3..
            * Contain arbitrary Python Objects, separated with commas. 
            * Parenthesis needed to avoid ambiguity (e.g. function having a tuple as an input) 
            * It’s the comma that creates the tuple, not the parenthesis.
            * Singleton (tuple of 1 item) - a, or (a,)
        * Bytes - immutable array of byte literals.
        * Ranges - immutable sequence of numbers, commonly used for looping a specific number of times in for loops
* Mutable Sequences:
    * They are mutable, they can be changed after they’re created
    * Types:
        * Lists - [object0, object1, object2…]
            * Contain arbitrary python objects, separated with commas, inside square brackets.
        * Byte arrays - mutable array of byte literals
        * Arrays - Module that defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers. Like lists but constraint to a single object type - i.e. 1 type code, specified upon creation.

Set types
* Unordered, finite sets of unique, immutable objects.
* Cannot be indexed by any subscript. However, they can be iterated over, and len() function works.
* Use cases: fast membership testing, removing duplicates from a sequence, computing certain mathematical operations (union, intersection,…)
* Immutability rules (same as dictionary keys): If 2 numbers compare equal in numeric comparison (e.g. 2 and 2.0), only one of them can be contained in a set.
* Types:
    * Sets
        * Created with set(), can be modified by several methods, e.g. add()
        * Mutable set
    * Frozen sets
        * Created with frozenset()
        * Immutable and hashable: it can be used again as an element of another set, or as a dictionary key.

Mappings
* Finite sets of objects indexed by arbitrary index sets.
* Subscript notation: a[k] selects item indexed by k from the mapping a.
* It can be iterated over. len() function works
* Type:
    * Dictionaries
        * Mutable. Created by the {…} notation
        * Finite sets of objects indexed by nearly arbitrary values [keys]
        * Only values not accepted as keys - values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity. This is because the efficient implementation of dictionaries requires a key’s hash value to remain constant. 
        * Numeric comparison rule: if 2 numbers compare equal (e.g. 2 and 2.0) then they can be used interchangeably to index the same dictionary entry
        * They preserve insertion order - keys will be produced in the same order as they were added sequentially over the dictionary


Further implications of some data types:
* Lists
    * many useful methods available
    * used cases: Stacks (LIFO), Queues (FIFO), List Comprehensions, Nested List Comprehensions
        * List comprehensions/Nested List comprehensions: make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
    * del() statement - removes item(s) from a list using its index/slice instead of value
* Tuples and Sequences
    * lists and strings - many common properties (indexing, slicing…)
    * Immutable sequences (e.g. Tuples) - support hashing (not implemented - mutable sequences) -> therefore tuple instances can be used as dictionary keys, and be stored in set and frozen set instances
    * Tuples used - contain heterogeneous sequences, accessed via: unpacking or indexing
* Sets
    * Unordered collection with no duplicate elements. Used for: membership testing, eliminating duplicate entries, mathematical operations (union, intersection, difference, symmetric difference)
    * created by set()
    * Set comprehensions are supported
* Dictionaries
    * Unlike sequences (which are indexed by a range of numbers) - Dictionaries are indexed by keys - Keys are unique
    * Keys must be any immutable type - Tuples (if they contain only strings/numbers/tuples)
    * Cannot use lists as keys
    * Key-Value pairs {key: value, key2, value…}
    * dict(), del(), list(dict), Dict comprehensions
* Looping techniques
    * Dictionaries: key and value can be retrieved at the same time - items()
    * Sequences: 
        * Position index and corresponding value can be retrieved at the same time - enumerate()
        * Loop over 2 or + sequences at the same time: pair entries with zip() function
        * Loop over sequence - reversed(), sorted()
    * Lists - easier to create new list on looping than to modify list during loop
* Conditions
    * while, if
    * in, not in - compare whether a value occurs/does not occur in a sequence
    * is, is not - compare whether 2 objects are really the same object - for mutable objects like lists.
    * Chaining of comparisons

Other built-in types:
* None - what Python returns for methods that modify a mutable data structures but return no output
* Range()
* User-defined function
* Classes
* Modules
* Custom Classes - Generally mutable
* Class instances

