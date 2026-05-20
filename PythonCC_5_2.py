#Mini Aventura de texto
"""La aventura es sencilla el jugador puede elegir entre pelear o no con un monstruo,
en caso de enfrentarlo tendrá que tomar la decisión de si matarlo o no"""

#Función revisora de la respuesta
def revision(respuesta):
    while True:
        if respuesta == "S" or respuesta == "N":
            return(respuesta)
        else:
            print("Escribe una respuesta válida")
            respuesta=input("S.Si N.No ")

#Función de la primer decisión
def primerDecision(respuesta):
    if respuesta=="S":
        print("Corres increiblemente rápido una rama de uno de los grandes árboles te hace tropezar, el rugido te alcanza, solo vez todo apagarse")
        input("Presiona una tecla para salir, deberías volver a intentarlo")
        exit()
    else:
        print("Te levantas y te pones en una postura de combate, sientes en tu costado una espada y aunque no sabes usarla la empuñas\n Talvez muera aquí pero no se lo dejare sencillo a quien quiera matarme\n Piensas en esto cuando frente a ti se muestra una bestia similar a un enorme león que camina en dos patas \n viste pieles de otros animales como ropa y un garrote enorme que parece hecho de uno de los grandes árboles que te rodean")
        return()

#Solicitud del nombre del jugador para darle algo de inmersión
nombre=input("Escribe tu nombre: ")

#Texto de inicio 
print("Hola " +nombre+ " es un placer darte la bienvenida a esta mini aventura de texto. \nEn esta breve aventura hay 3 posibles finales. ¿Podrás obtenerlos todos? Jajajaja \nEs broma seguro que lo logras")

#Inicia la historia
print("Despiertas enmedio de un bosque, lo primero que haces es percatarte de que tienes\npuesta una armadura que no recuerdas haberte puesto, miras a tu alrededor y solo notas\nla espesura del bosque, árboles tan grandes que casí bloquean la luz del cielo, aunque \nparece ser de día la realidad es que sientes como si estuvieras cerca del anochecer, bajo \nbajo de ti una tierra suelta que ya ha ensuciado parte de tus ropas y tu armadura, tus\nojos empiezan a adaptarse a la oscuridad cuando escuchas un fuerte rugido")

#Primera separación de la historia
accion=input("¿Correras? S.Si N.No ")

primerDecision(accion)

#Tal vez agregar arte ASCII en algunas partes para ilustrar
