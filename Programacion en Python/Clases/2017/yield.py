def simple_generator_function():
    yield 1
    yield 2
    yield 3

print "#1"
for value in simple_generator_function():
     print(value)

print "#2"
our_generator = simple_generator_function()
print next(our_generator)

print "#3"
for value in our_generator:
     print(value)
print "#4"
new_generator = simple_generator_function()
print(next(new_generator)) # perfectly valid
