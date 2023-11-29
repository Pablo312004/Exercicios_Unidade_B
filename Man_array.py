def main():
  # Criando um array de inteiros vazio
  array = []

  # Pedindo ao usuário para inserir 5 números inteiros
  for i in range(5):
    array.append(int(input("Digite um número inteiro: ")))

  # Exibindo o array resultante
  print("Array:", array)

  # Calculando a soma de todos os números no array
  soma = 0
  for numero in array:
    soma += numero
  print("Soma:", soma)

  # Encontrando o valor mínimo e o valor máximo no array
  minimo = array[0]
  maximo = array[0]
  for numero in array:
    if numero < minimo:
      minimo = numero
    elif numero > maximo:
      maximo = numero
  print("Mínimo:", minimo)
  print("Máximo:", maximo)

  # Removendo o último elemento do array
  array.pop()
  print("Array após remover o último elemento:", array)

  # Inverting a ordem dos elementos no array
  array.reverse()
  print("Array após inverter a ordem:", array)

if __name__ == "__main__":
  main()
