def creartxt():
    archi = open('datos.txt', w)
    archi.close()

def grabartxt():
    archi = open('datos.txt', 'a')
    archi = write('linea 1\n')
    archi = write('linea 2\n')
    archi = write('linea 3\n')
    archi.close()

creartxt()
grabartxt()
