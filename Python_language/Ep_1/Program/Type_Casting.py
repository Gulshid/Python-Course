# Type Casting in Python

# Int Conversion
print("*** To Int Conversion ***")

# Float to int Conversion
a = 3.2
b = int(a)
print("Float :", a, " to Int Conversion   int :",b)

# String to int Conversion
c = "78"
d = int(c)
print("String :",c, "To int Conversion Int :", d)


# Boolean to int Conversion
istrue = True
isfalse = False
e = int(istrue)
f = int(isfalse)
print("Boolean :",istrue, " To int Conversion  Int :", e)
print("Boolean :",isfalse, " To int Conversion  Int :", f)

print("*** To Float Conversion ***")


# Int to Float Conversion
g = 34
h = float(g)
print("Int :",g, "To Float COnversion Float :", h)

# String to Float
k = "70"
l =float(k)
print("Int :",k, "To Float COnversion Float :", l)


# Boolean to Float Conversion
isT = True
isF = False
p = float(isT)
o = float(isF)
print("Boolean :",isT, "To Float COnversion Float :", p)
print("Boolean :",isF, "To Float COnversion Float :", o)

print("*** To String Conversion ***")

# Int to String Converison
m = 3
j = str(m)
print("Int :", m, " To String Conversion String :", j)


# Float to String Converison
y = 3.5
u = str(y)
print("Float :", y, " To String Conversion String :", u)

# Boolean to String Converison
ist = True
isf = False
str_a = str(ist)
str_b = str(isf)
print("Boolean :",ist, "To String COnversion String :", str_a)
print("Boolean :",isf, "To String COnversion String :", str_b)

list_a = [1,2,3,4,5]
str_val = str(list_a)
print("List :", list_a, "  To String COnversion String :", str_val)


print("*** To Boolean Conversion ***")


# Int to Boolean Conversion
int_a = 9
bol_a = bool(int_a)
print("Int :", int_a, " To Boolean Conversion BOolean :",bol_a)


# Float to Boolean Conversion
float_a = 0.0
bol_b = bool(float_a)
print("Float  :", float_a, " To Boolean Conversion BOolean :",bol_b)


# String to Boolean Conversion
string_c = "Hello "
bol_c = bool(string_c)
print("String  :", string_c, " To Boolean Conversion BOolean :",bol_c)


# List to Boolean Conversion
list_b = [1,2,3,4]
bol_d = bool(list_b)
print("List   :", list_b, " To Boolean Conversion BOolean :",bol_d)



print("*** To List Conversion ***")

# String to List Conversion
string_g = "Hello WOrld "
list_r = list(string_g)
print("String :", string_g, " To List Conversion List :", list_r)

# tuple to List Conversion
tuple_a = (1,2,3)
list_y = list(tuple_a)
print("Tuple :", tuple_a, " To List Conversion List :", list_y)

# Range to List Conversion
num = range(8)
list_v = list(num)
print("Range :", num, " To List Conversion List :", list_v)

print("*** To Tuple Conversion ***")


# List to Tuple Conversion
list_w = [1,23,56]
tuple_t = tuple(list_w)
print("List :", list_w, " To Tuple Cnveriosn   Tuple :",tuple_t )

# String to Tuple  Conversion
string_i = "Hello!"
tuple_f = tuple(string_i)
print("String :", string_i, " To Tuple Conversion Tuple :",tuple_f)

print("*** To Set Conversion ***")

# list to Set Conversion
list_as = [1,2,3,4]
set_a = set(list_as)
print("List :", list_as, " To Set Conversion Set :",set_a)

# String to Set Conversion
String_abc = "Hello ! This is Type Casting"
set_abc = set(String_abc)
print("String :", String_abc, " To Set Conversion Set :",set_abc )