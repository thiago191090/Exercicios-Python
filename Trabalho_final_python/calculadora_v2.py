#Variável para decisão de continuar o laço while
import time


saida = '' 

#Função que retorna a adição
def adicao (num1, num2): 
    resultado = num1 + num2
    return resultado

#Função que retorna a subtração
def subtracao (num1, num2): 
    resultado = num1 - num2
    return resultado

#Função que retorna a multiplicação
def multiplicacao (num1, num2): 
    resultado = num1 * num2
    return resultado

#Função que retorna a divisão
def divisao (num1, num2): 
    if num1 % num2 == 0:
        resultado = num1 / num2
        return resultado
    else:
        print("Não foi possível realizar a divisão por 0!")
        resultado = "Erro"
        return resultado

#Função calculadora
def calculadora(num1, operacao, num2): 
    if operacao == "+":
       resultado = adicao(num1, num2)
       return resultado
    if operacao == "-":
       resultado = subtracao(num1, num2)
       return resultado
    if operacao == "*":
       resultado = multiplicacao(num1, num2)
       return resultado
    if operacao == "/":
       resultado = divisao(num1, num2)
       return resultado
    #Caso a operação seja digitada errada
    else:
        return print("Operação não existente") 


while saida != "n":
      #Entrada dos valores da operação
      num1 = int(input("Digite o primeiro número da operação: \n"))
      operacao = input("Digite a operação que deseja: (Adição (+), Subtração (-), Multiplicação (*), Divisão (/)) \n")
      num2 = int(input("Digite o segundo número da operação: \n"))

      #Chamada da função calculadora
      resultado = calculadora(num1, operacao, num2) 

      #Caso tenha digitado o sinal de operação errado, apareçe uma mensagem de erro
      if (operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/"): 
        print("Digite a operação corretamente na próxima!")
      else:
        print("Resultado da operação: ", resultado)

      #Decidir fazer outra operação ou sair
      saida = input("Deseja fazer outra operação? 'S' ou qualquer valor para 'SIM', ou 'N' para 'NÃO' \n") 
      saida = saida.lower()

      #Se decidir sair, apenas uma mensagem de encerramento  
      if saida.lower() == "n": 
          print("Calculadora Encerrada!")

#5 segundos para a tela fechar, ou o script encerrar
time.sleep(5)
exit


