import random

def guess_number(x):
    print("===============================")
    print("  ¡Bienvenido(a) al juego!   ")
    print("===============================")
    print("Tu meta es adivinar el número generado por la computadora.")
   
    number = random.randint(1, x) 
    
    prediction = 0
    
    while prediction != number:
        prediction = int(input(f"Adivina un número entre 1 y {x}: ")) 
        
        if prediction < number:
            print("Intenta de nuevo. Este número es muy pequeño")
        elif prediction > number:
            print("Intenta de nuevo. Este número es muy grande.")
            
    print(f"¡Felicitaciones! Adivinaste el número {prediction} correctamente")
  
guess_number(10)
