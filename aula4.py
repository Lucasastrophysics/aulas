def do_twice (f,x):
    f(x)
    f(x)
def print_twice(x):
    print(x)
    print(x)
do_twice(print_twice,'spam')
