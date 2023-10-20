class Proveedor:
    id_proveedor = ""
    razon_social = ""
    rut_empresa = ""
    def __init__(self,id_proveedor,razon_social,rut_empresa):
        self.id_proveedor= id_proveedor
        self.razon_social= razon_social
        self.rut_empresa= rut_empresa
        
    ###
    def registrarProveedor(self, id_proveedor, razon_social, rut_empresa):
        self.id_proveedor = id_proveedor
        self.razon_social= razon_social
        self.rut_empresa = rut_empresa
        pass
        
#-----------------------------------------------------------------------------------------------------------------------------------------
#Registro_Proveedor
#-----------------------------------------------------------------------------------------------------------------------------------------
def nuevo_proveedor():
    
    print("Ingrese la razon social")
    razon_social= str(input())
    print("Ingrese el rut del proveedor")
    rut= str(input())
    print("Ingrese el nombre del Proveedor")
    # Insumo o Proveedor que se recibe del proveedor
    nombre_Proveedor= str(input())
    id_prove_cero=True
    while id_prove_cero:
        print("Ingrese el ID del insumo")
        id_insumo= str(input())
        try:
            id_insumo = int(id_insumo)
            id_prove_cero= False
        except ValueError:
            print("El indice es incorrecto, intentelo nuevamente ingresando un valor numerico")
    # El ID sera la variable que designemos en el menu dependiendo 
    print("Ingrese el telefono del proveedor")
    telefono= str(input())
    print("¿Son estos datos correctos?\n", razon_social, rut, nombre_Proveedor, id_insumo, telefono)
    si_no=True
    while si_no:
        print("Ingrese si/no")
        respuesta = str(input())
        if respuesta != "si" and respuesta != "SI" and respuesta != "Si"   and respuesta != "no" and respuesta != "NO" and respuesta != "No" :
                print("Opcion invalida")
        else:
            si_no = False
        if respuesta =="si" or respuesta== "Si" or respuesta == "SI":
            sqlb ='SELECT MAX(ID) FROM PROVEEDOR '
            curs.execute(sqlb)
            result = conn.commit()
            for data in curs.fetchone():
                value_b = data
            new_value_b= value_b[2:]
            new_value_b=int(new_value_b)+1
            new_id_prov= "PR"+str(new_value_b)

            sqli ='SELECT MAX(ID) FROM INSUMOS '
            curs.execute(sqli)
            result = conn.commit()
            for data in curs.fetchone():
                valuei = data
            id_insumo= valuei[1:]
            id_insumo= int(id_insumo)+1
            id_insumo='I'+ str(id_insumo)
            
             ## AGREGAR LISTA PARA GUARDAR DATOS DE PRODUCTOS
            
            print("Datos agregados correctamente")
        elif respuesta == "no" or respuesta == "NO" or respuesta == "No":
            print("Intentelo nuevamente")
            nuevo_proveedor()
            return None
    si_no =True
    while si_no:
        print("¿Desea registrar un nuevo Proveedor?")
        print("Ingrese si/no")
        respuesta_2 = str(input())
        if respuesta_2 != "si" and respuesta_2 != "SI" and respuesta_2 != "Si"   and respuesta_2 != "no" and respuesta_2 != "NO" and respuesta_2 != "No" :
            print("Opcion invalida")
        else:
            si_no = False  
        if respuesta_2== "Si" or respuesta_2== "si" or respuesta_2== "SI":
            nuevo_proveedor()
            return None
        elif respuesta_2 == "no" and respuesta_2 == "NO" and respuesta_2 == "No":
            return None
