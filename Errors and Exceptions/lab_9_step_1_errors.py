import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as err:
    logging.warning("Erro - {}. Você não pode adicionar uma string para um inteiro, sem converter o inteiro para uma string primeiramente.".format(err))

# Para atualizar o respositório