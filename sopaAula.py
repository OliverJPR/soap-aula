from zeep import Client

client = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')

#Funcion para obtener una lista de estudiantes
def getEstudiantes(servicio):
    return{
        servicio:client.service.getAllEstudiante()
    }[servicio]

def getAsignatura(parametro):
        return {"asignatura":client.service.getAsignatura(parametro)}["asignatura"]
   
def getProfesor(parametro):
        return {"profesor":client.service.getProfesor(parametro)}["profesor"]


#Menu de opciones
opcion = -1
while True:
    print("**************Menu********************")
    print(" 1. Listar Todos los estudiantes")
    print(" 2. Consultar una asignatura")
    print(" 3. Consultar un profesor ")
    print(" 0. Exit")
    print("**************************************")
   
    opcion = int(input("Opción tomada: "))

    if opcion == 0:
        break
    elif opcion == 1:
        print (getEstudiantes("estudiantes"))
    elif opcion == 2:
        opcionAsig = input("Digite el id a consultar: ")
        print (getAsignatura(opcionAsig))
    elif opcion == 3:
        opcionProfe = input("Digite el id a consultar: ")
        print (getProfesor(opcionProfe))
