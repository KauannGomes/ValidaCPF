import re
import sys
#Variaveis de controle
entrada = input('CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada)
cpf_limpo = cpf.replace('.', '').replace('-','')
cpfSemDigito = cpf_limpo[:-2]
cpfSegDigit =  cpf_limpo[:-1]
sequencia = entrada == entrada[0] * len(entrada)
if sequencia:
    print('Voce enviou dados repetidos')
    sys.exit()


c = 10
resultado = 0
#Itera e faz as contas do primeiro digito
for num in cpfSemDigito:
    num = int(num)
    conta = num * c
    resultado += conta  
    if c == 2:
        resultado_verificador = (resultado * 10) % 11
        primeiroDigito = resultado_verificador
        if primeiroDigito > 9:
            primeiroDigito = 0
    c -= 1
#Itera e faz as contas do SEGUNDO digito
c2 = 11
resultado2 = 0
for num in cpfSegDigit:
    num = int(num)
    conta = num * c2
    resultado2 += conta  
    if c2 == 2:
        resultado_verificador2 = (resultado2 * 10) % 11
        segundoDigito = resultado_verificador2
        if segundoDigito > 9:
            segundoDigito = 0
    c2 -= 1
#Valida se os digitos são iguais a os digitados 
for c,num in enumerate(cpf_limpo):
    if c == 9:
        num = int(num)
        if primeiroDigito == num :
            primeiroDigito = True
        else:
            primeiroDigito = False
    if c == 10:
        num = int(num)
        if num == segundoDigito:
            segundoDigito = True
        else:
            segundoDigito = False
#Mostra na tela o resultado
if primeiroDigito and segundoDigito:
    print(f'O CPF {cpf} é valido')
else:
    print(f'O CPF {cpf} NÂO é valido')