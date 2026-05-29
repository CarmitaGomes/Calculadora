import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    
    elif operador == '-':
        result = num1 - num2

    elif operador == '*':
        result = num1 * num2

    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif operador == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif operador == '**':
        result = num1 ** num2



    return result

def calculadora_alternativa(num1: float, num2: float, operador: str) -> float:
    """
    Segunda versão
    """
    if operador == '+':
        return num1 + num2 
    
    elif operador == '-':
        return num1 - num2
    
    elif operador == '*':
        return num1 * num2
    
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif operador == '%':
        if num2 != 0:
            return num1 % num2
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif operador == '**':
        return num1 ** num2

    return float("nan")


if __name__ == "__main__":

            
    print('Calculadora')

    continuar = 's'

    while continuar.lower() == 's': 
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')

            n1 = float(input('Introduza o 1º número: ')) 
            op = input('Escolha o operador (+, -, *, /, %, **): ')
            n2 = float(input('Introduza o 2º número: ')) 

            res = calculadora(n1, n2, op)
            
            print(f'\nResultado: {res}')

        except ValueError:
            print('Dados inválidos! Tente novamente!')
            time.sleep(2)

            
        continuar = input("\nDeseja continuar a calcular? (s/n): ")

    print('\nVolte sempre!\n')