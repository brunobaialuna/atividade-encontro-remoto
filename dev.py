

def calculo_imc(x, y):
    imc = x / (y ** 2)
    
    return imc
    

def classificacao(imc):
    if imc < 18.5:
        imc = "\nVocê está abaixo do peso."  
    elif imc < 25:
        imc = "\nSeu peso está normal."
    elif imc < 30:
        imc = "\nVocê está com sobrepeso."
    elif imc < 35:
        imc = "\nVocê está com obesidade grau I."
    elif imc < 40:
        imc = "\nVocê está com obesidade grau II."   
    else:
        imc = "\nVocê está com obesidade mórbida."

    return imc
 
   