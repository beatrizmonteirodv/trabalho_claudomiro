"""
Atividade 2.1 - Simulador de Memoria RAM

Discente: Ana Beatriz Monteiro da Silva
Curso: Inteligencia Artificial
Docente: Claudomiro de Souza Sales Junior
"""

# A memoria possui 16 posicoes.
# Cada posicao comeca com o valor 00000000.
memoria = ["00000000"] * 16

print("SIMULADOR DE MEMORIA RAM")
print("A memoria possui 16 enderecos e cada endereco guarda 8 bits.")

while True:
    print()
    print("Digite W para escrever.")
    print("Digite R para ler.")
    print("Digite L para listar toda a memoria.")
    print("Digite qualquer outra tecla para sair.")

    opcao = input("Escolha uma opcao: ").strip().upper()

    if opcao == "W":
        endereco = input("Digite um endereco de 4 bits: ").strip()

        # O endereco deve possuir 4 caracteres, todos iguais a 0 ou 1.
        if len(endereco) == 4 and endereco.count("0") + endereco.count("1") == 4:
            dado = input("Digite um dado de 8 bits: ").strip()

            # O dado deve possuir 8 caracteres, todos iguais a 0 ou 1.
            if len(dado) == 8 and dado.count("0") + dado.count("1") == 8:
                posicao = int(endereco, 2)
                memoria[posicao] = dado
                print("Dado gravado com sucesso.")
            else:
                print("Dado invalido. Digite exatamente 8 bits.")
        else:
            print("Endereco invalido. Digite exatamente 4 bits.")

    elif opcao == "R":
        endereco = input("Digite um endereco de 4 bits: ").strip()

        if len(endereco) == 4 and endereco.count("0") + endereco.count("1") == 4:
            posicao = int(endereco, 2)
            print("Conteudo do endereco", endereco, ":", memoria[posicao])
        else:
            print("Endereco invalido. Digite exatamente 4 bits.")

    elif opcao == "L":
        print("Endereco : Conteudo")

        for posicao in range(16):
            endereco = format(posicao, "04b")
            print(endereco, ":", memoria[posicao])

    else:
        print("Simulador encerrado.")
        break

