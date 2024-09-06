
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_y = outer_function(5)
print(add_y(4))

# =========================================================
# Write a closure that multiplies numbers by a given factor
# =========================================================
def outer_function(factor):
    
    def inner_function(x):
        return x * factor

    return inner_function

factor_proc = outer_function(5)
print(factor_proc(4))

# =========================================================
# Experiment with different variables to see how closures retain their values
# =========================================================
z = 54
def outer_function():
    y = 5
    def inner_function(x):
        return x + y + z
    return inner_function

add_all = outer_function()
print(add_all(4))

# ========================================================
# YET ANTOHER EXAMPLE
# ========================================================
def outer_function():
    y = 10
    def inner_function(k):
        nonlocal y
        y += k
        return y
    return inner_function

mod_non_local = outer_function()
print(mod_non_local(10))
print(mod_non_local(10))
print(mod_non_local(10))