print("Bem vindo ao jogo de Adivinhação!")
#Declaração da variável
numero_secreto = 43
#Input para digitar o número/input sempre retorna string
chute_str = input("Digite o seu número:")
#Print para mostrar qual foi digitado
print("Você digitou: ", chute_str)
#variável para converter a string em número inteiro
chute = int(chute_str)
#IF para comparação == compara o tipo também
if(numero_secreto == chute):
    print("Você acertou!!")
#Else para caso não tenha retorno igual
else:
    print("Você errou, tente novamente!!")
