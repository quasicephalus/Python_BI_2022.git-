### Functions challenge

1. `sequential_map` applies multiple functions passed in _*args_ to an object or a list on objects (the last arg) and returns list of reworked objects
2. `consensus_filter` applies multiple logical functions to a list of objects (as described above) and returns the list of filtered objects
3. `conditional_reduce` takes two functions, first of which must return boolean value and second must take two arguments and return one (as in functools.reduce), and a collection of objects to reduce. Objects from collections "checked" by function 1 and then reduced by function 2. Returns one value.
4. `func_chain` takes number of functions in _*args_ and returns a function which applies all of them to the given single object
5. `multiple_partial` does the same as `functools.partial`, but with multiple functions passed in _*args_
6. `printer` is a `print()` implementation without flush argument