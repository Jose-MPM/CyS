import os 
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def split_string(string, word):
    string = string.upper().replace(" ", "")  
    string = string.replace(",", "")  
    string = string.replace(".", "")  
    block_size = len(word)  
    return([string[i:i+block_size] for i in range(0, len(string), block_size)])
	

def cifrar(cadena, clave):
	clave.upper()
	cadena_cifrar = ''
	i = 0
	j = 0
	for block in cadena: 
		for letra in block:
			suma = abc.find(letra) + abc.find(clave[i% len(clave)])
			modulo = int(suma)% len(abc)
			cadena_cifrar = cadena_cifrar + str(abc[modulo])
			i+=1
		j+=0
		i=0
	return cadena_cifrar	    
	    
cadena= "Prometeo es el titán amigo de los mortales, honrado principalmente por robar el fuego de los dioses darlo a los hombres para su uso y posteriormente ser castigado por Zeus por este motivo"
print(cifrar((split_string(cadena, "MITOLOGIA")), "Mitologia"))