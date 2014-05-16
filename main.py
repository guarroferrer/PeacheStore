def listar():
     with open('aplicaciones.txt',mode='r',encoding='utf-8')as archivo:
         for linia in archivo:
             print(linia)
