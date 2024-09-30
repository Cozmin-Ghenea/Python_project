# def functia_mea(param_1, param_2):
#     return "Ana are mere", "Ana are mere"
#
#
# rezultat = functia_mea(1, 2)
# print(rezultat)


# def suma(a: int = 1,b: int = 2, *args, **kwargs) -> (int, int):
#     print(type(args))
#     suma = a + b
#     for i in args:
#         suma = suma + i
#     for i in kwargs.values():
#         suma = suma + i
#     return suma, a-b
# *args -> permite functiei sa selecteze mai multe argumente pozitionale
# *args -> tuplu
# **kargs -> permite functiei sa foloseasca mai multe argumente si se vor folosi in parametrii de tip a=1,b=2,c=3)
# **kargs -> dictionar
# rezultat_suma, rezultat_diferenta = suma(3,45,6,2,3,3,4,5,3, d=5,e=6)
# print(rezultat_suma , rezultat_diferenta)