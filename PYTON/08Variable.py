puntaje  = 0

if puntaje >100 or puntaje <= 0 :
  print ("Puntaje no valido") 
else: 
    if puntaje >= 95 and puntaje <= 100:  #van en la linea del IF si 
     print("Su puntaje es Aprobado con honores")
    elif puntaje >= 50  and puntaje < 95: #ejecuta directamente la linea 
     print("Aproadoo")
    else :                           #sino se cumplen 
     print ("Repabado")
     print ("Fin de condicional if")
