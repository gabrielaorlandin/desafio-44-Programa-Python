# Faça um programa que mostre a mensagem "hello world" cinco vezes.
for i in range(5):
    print("hello world")


# 2) Faça um programa que mostre todos os números de 1 até 150.
for i in range(1, 151):
    print(i)




# 3) Faça um programa que mostre uma contagem regressiva que inicia em 10 e termina em 0
for i in range(10, -1, -1):
    print(i)


# 4) Faça um programa que mostre todos os números pares de 1 até 200. 
for i in range(2, 201, 2):
    print(i)




# 5) Faça um programa que gere as tabuadas do 1 até o 10.
for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

#Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.
numero = int(input("Digite um número inteiro: "))

print(f"Números ímpares de 1 até {numero}:")
for i in range(1, numero + 1, 2):
    print(i)

