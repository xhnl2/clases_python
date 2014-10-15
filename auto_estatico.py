static auto():
 
    gasolina = 0
    def __init__(gasolina):
        Auto.gasolina = gasolina
        print "tenemos", gasolina, "litros"

    @staticmethod
    def arrancar(gasolina):
        if gasolina > 0:
            print "arranca"
        esle:
            print "no arranca"

    @staticmethod
    def conducir(gasolina):
       if gasolina > 0:
           gasolina -= 1
           print "quedan", gasolina, "litros"
       else:
           print "no se mueve..."
       mi_auto = Auto(10)
       print mi_Auto(5)

#### cuanta gasolina tenemos
print mi_Auto.gasolina
mi_Auto.arranca()
# Arrancamos el carro
mi_Auto.conducir()
mi_Auto.conducir()
mi_Auto.conducir()
mi_Auto.conducir()
mi_Auto.conducir()
mi_Auto.conducir()"""


