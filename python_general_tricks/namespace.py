a_var = 10
print("begin()-> ", dir())
def foo():
 b_var = 11
 print("inside foo()-> ", dir())
foo()
print("end()-> ", dir())