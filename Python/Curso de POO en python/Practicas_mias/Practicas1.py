import random
class Player:
    def __init__(self,nombre,daño,armadura,vida,lucha):
        self.nombre = nombre
        self.daño = daño
        self.armadura = armadura
        self.vida = vida
        self.lucha = lucha

    def atacar(self):
        print(f"{self.nombre} a atacado al enemigo y le a quitado {self.daño} puntos de vida")
        
    
    def morir(self):
        if(self.vida <= 0):
            print("HAS MUERTO")
            print("Has perdido el juego")
    
    def caminar(self):
        print("Caminando...")
    
    def picar_ojos(self):
        print("Le picas los ojos al enemigo")

class Enemy:
    def __init__(self,tipo,daño,armadura,vida):
        self.tipo = tipo
        self.daño = daño
        self.armadura = armadura
        self.vida = vida

    def atacar(self):
        
        if (atack_r == 1):
            print(f"el enemigo a atacado al jugador y le a quitado {self.daño} puntos de vida")
            
        else:
            print("el enemigo intento atacar al jugador pero no lo logro")
    
    def morir(self):
        if (self.vida <= 0):
            print("Enemigo derrotado")
        
nombre = input("Decime tu nombre para empezar el juego: ")

jugador = Player(nombre,5,10,50,False)
enemigo = Enemy("Linyera",5,4,20)

while True:
    #Decidir evento 0 para caminar y 1 para luchar
    event_luchar = random.randint(0,1)
    
    if (event_luchar == 0):
        jugador.caminar()
        #event_luchar = random.randint(0,1)
        #print(event_luchar)
    else:
        print(f"Te haz encontrado con un {enemigo.tipo} PREPARATE PARA LUCHAR")
        jugador.lucha = True
    
    #Entrar en batalla
    if (jugador.lucha == True):
        while jugador.lucha == True:
            
            #Mostrar estadisticas de vida
            print(f"""ESTADISTICAS: \n
                  Tu Vida: {jugador.vida} \n
                  Vida Enemigo: {enemigo.vida} \n
                  """)
            
            #Pedir accion
            accion = input("Dime tu accion: ")
            enemigo_ver = True
            #Ataque del jugador
            if (accion == "atacar"):
                jugador.atacar()
                enemigo.vida -= jugador.daño
                atack_r = random.randint(0,1)
            elif(accion == "picar los ojos"):
                jugador.picar_ojos()
                enemigo_ver = False
            else:
                print("No hiciste nada")
                atack_r = random.randint(0,1)
            

            #Ataque del enemigo
            if(enemigo_ver == True):
                if(atack_r == 1):
                    enemigo.atacar()
                    jugador.vida -= enemigo.daño
                else:
                    print("el enemigo intento atacar al jugador, pero fallo")
                
            if(enemigo_ver == False):
                print(f"le picaste los ojos a {enemigo.tipo} ahora no puede ver")

            #muerte del enemigo
            if (enemigo.vida <= 0):
                jugador.lucha = False
                enemigo.morir()
                break
            #Muerte del jugador
            elif (jugador.vida <= 0):
                jugador.lucha = False
                jugador.morir()
                break
    if(enemigo.vida <= 0):
        print("HAS GANADO EL JUEGO")
        break
    elif(jugador.vida <= 0):
        break