import re
from validate_docbr import CPF

def validate_cpf(numero_cpf) :
    cpf = CPF()
    return not cpf.validate(numero_cpf)


def validate_nome(nome) :
    return not nome.isalpha() 

def validate_celular(celular) :
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular)
    print(resposta)
    return not resposta
