'''Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva uma função que dado
 duas palavras, retorne True caso sejam.'''


palavra = "batata"

def palavra_inverso(palavra, palavra2):
    if palavra2 == palavra[::-1]:
        return True
    else:

        return False
  
   
    

