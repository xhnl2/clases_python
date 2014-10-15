def decorador(funcion):
     def funcion_envoltura():
         print("antes de la funcion")
         funcion()
         print(“despues de la funcion”)
     return funcion_envoltura
