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


#añadirApp("app1","prov1","0","22-02-2014")
