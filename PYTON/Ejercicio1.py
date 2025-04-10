temperatura =  float (input("Ingrese la temperatura "))
unidad = input("La tepertura esta en C o F ")

if unidad  == "F":
    conversion = (temperatura * 1.8) + 32
    print ("La temperatura en F es ", conversion)

elif unidad == "C":
     conversion =  (temperatura - 32) / 1.8
     print ("La temperatura en C", conversion)
else : 
     print ("Solo escoge C O F ")


    




