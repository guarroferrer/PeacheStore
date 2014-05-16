def listar():
     with open('aplicaciones.txt',mode='r',encoding='utf-8')as archivo:
         for linia in archivo:
             print(linia)
def añadirApp(nombre,proveedor,precio,fecha):


    identificaion=(nombre+","+proveedor+","+fecha)
    numeroDes="0"
    numeroPunt="0"
    puntuacion="0"
    numComen="0"
    with open('aplicaciones.txt',mode='a',encoding='utf-8')as archivo:
        archivo.write(identificaion+","+precio+","+numeroDes+","+numeroPunt+","+puntuacion+","+numComen+"\n")

def sumar(aplicacion):

     aplicaionN=""
     with open('aplicaciones.txt',mode='r+',encoding='utf-8')as archivo:
         for linia in archivo:
            nombre,proveedor,fecha,precio,numeroDes,numeroPunt,puntuacio,numeroComen = linia.split(',',7)
            npuntuacion=puntuacio.strip("\n")

            aplicaionN=linia.__contains__(aplicacion)
            print (aplicaionN)
            print(npuntuacion)
            npuntuacion=npuntuacion+1
            archivo.write(nombre,proveedor,fecha,precio,numeroDes,numeroPunt,npuntuacion,numeroComen)


#añadirApp("app1","prov1","0","22-02-2014")
