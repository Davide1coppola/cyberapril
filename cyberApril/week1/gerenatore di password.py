'''
generare una passwourd casuale di n caratteri 
'''


import random
import string


def generate_random_str(n):
  return' '.join(random.choices(string.ascii_letters + string.digits, k=n))

n=int(input("inserisci quanti caratteri vuoi "))
random_string= generate_random_str(n)
if(n <= 8):
  print("la passwuord creata è:\n ", random_string)
  print(" consigliamo una password piu articolata grazie\n")

else :
  print(" la password generata è:\n",random_string)
  print("la password è sicura")

