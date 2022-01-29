def conversordevogais(vogal):
   vogal = vogal.upper()

   if(vogal == 'A'):
       return '@'

   if(vogal == 'E'):
       return '&'

   if(vogal == 'I'):
       return '!'

   if(vogal == 'O'):
       return '#'

   if(vogal == 'U'):
       return '*'

#Condicionando a conversão das vogais utilizando if dentro da função.

def programa():
   nome = input('Digite seu nome: ') #Input para o usuário colocar seu nome.

   nomedigitado = ''

   for i in nome:

       if(i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U'):
           nomedigitado += conversordevogais(i.upper())
       else:
           nomedigitado += i.upper()
           #Utilizando outra função que interage com a anterior.
           #Continua a conversão das vogais depois do usuário colocar o nome.

   print(nomedigitado)

if __name__ == '__main__':
   programa()
   #Utilizando o módulo __name__ para rodar o programa.