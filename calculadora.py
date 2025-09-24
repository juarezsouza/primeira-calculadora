numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
    print(f'Resultado: {resultado}')

elif operacao == '-':
    resultado = numero1 - numero2
    print(f'Resultado: {resultado}')

elif operacao == '*':
    resultado = numero1 * numero2
    print(f'Resultado: {resultado}')

elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f'Resultado: {resultado}')
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Operação inválida. Por favor, use +, -, * ou /.")