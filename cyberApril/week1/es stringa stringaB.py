
"""
scrivere una funzione  che dato in ingresso  lista A contenente n parole
restituisca in outoput  una lista B di interi che rappresentano la 
lunghezza  delle parole contenute in A
"""


def lunghezza_parole(lista_parole):
    lunghezza= [len(parola)for parola in lista_parole]
    return lista_parole, lunghezza


nomi= ["davide","andrea","laura","sara"]
nomi_input, lunghezza = lunghezza_parole(nomi)
print("i nomi immessi sono :", nomi_input)
print(" la conta delle parole è:", lunghezza)
