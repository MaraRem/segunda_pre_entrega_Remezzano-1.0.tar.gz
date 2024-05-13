

users = {}
  

def reg_usuario():
    
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input(f"Hola ! Ingresa una contraseña: ")
    

    if usuario not in users:
        users[usuario] = contrasena
        print(f"Bienvenido "+ (str(usuario)) + (str(contrasena)) + " Tu Usuario fue registrado!")
    
    else :
        if usuario in users(usuario) or contrasena in users.values(): 
            print(" Verifica los datos..")     
    

    menu()  


def ingreso():

    while True: 
        
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Hola ! Ingresa una contraseña: ")
        

        if usuario in users and users[usuario] == contrasena:
             print("Inicio de sesión exitoso. ¡BienvenidQ!")
        else: print ("Los datos ingresados son incorrectos. Inténtelo de nuevo.")
        
        menu()
        
               
def menu():
           
    while True:
        opcion = input("Si desea registrar un nuevo usuario seleccione (s)/ Si desea ingresar seleccione (x)/ Si desea Salir seleccion (n) ")
        if opcion.lower() == "s":
            reg_usuario()
        elif opcion.lower() == "n":
            print("Hasta luego..")
            print (f"Diccionario de usuarios y contraseñas ingresado hasta ahora " + (str(users)))
        elif opcion.lower() == "x":
            ingreso()
        else:
            print("Opción no válida. Por favor, ingresa s para registrar un nuevo usuario, x para ingresar o n para salir.")


menu()

