
# %% ########################################################
#
#                         Function
#
#############################################################

def my_function(x):
    """This is docstring"""
    print(x)
    return x

# Function can return tuple / unpacking

def minmax(items): 
    return min(items), max(items)

lower, upper = minmax([81, 82, 83, 84, 85])

print(lower, ' - ', upper)


# %% ########################################################
#
#             Arguments: positional, keyword, *args, **kwargs
#
#############################################################




# %% ########################################################
#
#             Dunder '__name__'
#
#############################################################


# how to execute function if module called directly

if __name__ == '__main__':
   my_function('This is my function')



# %% ########################################################
#
#             Lambdas
#
#############################################################





# %% ########################################################
#
#             Callable Instances
#
#############################################################

import socket

class Resolver:
    def __init__(self):
        self._cache = dict()

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

resolve = Resolver()
print(resolve('microsoft.com'))
print(resolve._cache)

print(resolve('google.com'))
print(resolve._cache)


# %% ########################################################
#
#             Callable Classes
#
#############################################################


# %% ########################################################
#
#             Local Functions
#
#############################################################



# %% ########################################################
#
#             Closures: __closure__ 
#
#############################################################




# %% ########################################################
#
#             Function Decorators
#
#############################################################












