import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as t_err:
    logging.warning("Erro - {}. Você não pode adicionar uma string para um inteiro, sem converter o inteiro para uma string primeiramente.".format(t_err))
except ValueError as v_err:
    logging.warning("Erro - {}. Erro no valor".format(v_err))
    