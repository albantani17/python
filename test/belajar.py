print("=====<INTEGER>====")
data_int = 7;
print("data = ", data_int, "type =", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilainya 0
print("data = ", data_float, "type =", type(data_float))
print("data = ", data_str, "type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

print("=====<FLOAT>====")
data_float = 7.5;
print("data = ", data_float, "type =", type(data_float))
data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)
print("data = ", data_int, "type =", type(data_int))
print("data = ", data_str, "type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

print("=====<STRING>====")
data_str = "8";
print("data = ", data_str, "type =", type(data_str))

data_int   = int(data_str)
data_float = float(data_str)
data_bool  = bool(data_str) 
print("data = ", data_int, "type =", type(data_int)) #harus angka
print("data = ", data_float, "type =", type(data_float)) #harus angka
print("data = ", data_bool, "type =", type(data_bool)) #false kalau string kosong

print("=====<BOOLEAN>====")
data_bool = True;
print("data = ", data_bool, "type =", type(data_bool))

data_int   = int(data_bool)
data_float = float(data_bool)
data_str   = str(data_bool) 
print("data = ", data_int, "type =", type(data_int))
print("data = ", data_float, "type =", type(data_float))
print("data = ", data_str, "type =", type(data_str))
