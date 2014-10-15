f = open("archivo.txt")
for linea in f:
    print linea
f.close()

def wfile(archivo):
    f = open(archivo, w)
    f.write("hmmm..ok")
    f.close()
