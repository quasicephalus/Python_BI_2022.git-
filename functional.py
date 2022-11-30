import sys


def sequential_map(*args):
    # Just for sure
    if len(args) == 1:
        return None
    # getting last arg as container
    container = args[-1]
    # I've googled how to check if object is iterable and found out about __iter__
    # It is mostly done for func_chain()
    # If iterable - map them all
    if hasattr(container, '__iter__'):
        for arg in args[0:-1]:
            container = list(map(arg, container))
    # Else - apply all funs to single value
    else:
        for arg in args[0:-1]:
            container = arg(container)
    return container


# It is very similar to the previous
def consensus_filter(*args):
    if len(args) == 1:
        return None
    container = args[-1]
    for arg in args[0:-1]:
        container = list(filter(arg, container))
    return container


def conditional_reduce(fun1, fun2, container):
    # If there is only one value, it is just returned as it is
    if len(container) > 1:
        # Checking all values by fun1
        container = list(filter(fun1, container))
        # Then reducing step by step
        while len(container) > 1:
            container[1] = fun2(container[0], container[1])
            container.remove(container[0])
    return container[0]


def func_chain(*args):
    # I decided to make arg list to append value later later
    args = list(args)

    # Please let me know if I can do the same with lambda in one string
    def temp(x):
        # Just adding value from user's call to args
        args.append(x)
        # and then calling sequential_map
        return sequential_map(*args)

    return temp


# Print implementation.
def printer(*args, sep=' ', end='\n', file=None):
    if file is None:
        file = sys.stdout

    def write(smth):
        file.write(str(smth))

    for arg in args:
        write(arg)
        write(sep)
    write(end)


# Here I was inspired with functools documentation
def multiple_partial(*args, **kwargs):
    def parted(*fargs):
        return fun(*fargs, **kwargs)

    out = []
    for fun in list(args):
        out.append(parted)
    return out
