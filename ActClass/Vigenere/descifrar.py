import os 
abc = 'abcdefghijklmnñopqrstuvwxyz '
def descifrar (cadena,clave):
	cadena_cifrar = ''
	i = 0
	for letra in cadena:
		suma = abc.find(letra) - abc.find(clave[i % len(clave)])
		modulo = int(suma) % len(abc)
		cadena_cifrar = cadena_cifrar + str(abc[modulo])
		i+=1
	os.remove('includes/texto_cifrado.txt')
	return cadena_cifrar