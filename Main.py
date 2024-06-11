import datetime

# Arrays
nome_usuarios = ["helena", "ana", "raissa"]
id_usuarios = [1, 2, 3]
senha_usuarios = ["1234", "5678", "91011"]
creditos_usuarios = [100, 200, 300]
relatorios_usuarios = {1: [], 2: [], 3: []}

# Control Variables
verifica_usuario = False
verifica_senha = False
id_usuario_logado = 0
index_senha = ""
index_usuario = ""
contador_login = 0

Entrada = False


# Methods
def ver_creditos(id_usuario_logado):
    indice = id_usuarios.index(id_usuario_logado)
    print(f"----- Você tem {creditos_usuarios[indice]} créditos -----")

def adicionar_creditos(id_usuario_logado, valor):
    indice = id_usuarios.index(id_usuario_logado)
    creditos_usuarios[indice] += valor
    data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    relatorios_usuarios[id_usuario_logado].append(f"----- {data_hora_atual} - Adicionado {valor} créditos -----")
    print(f"{valor} créditos adicionados. Você agora tem {creditos_usuarios[indice]} créditos.")

def remover_creditos(id_usuario_logado, valor):
    indice = id_usuarios.index(id_usuario_logado)
    if creditos_usuarios[indice] >= valor:
        creditos_usuarios[indice] -= valor
        data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        relatorios_usuarios[id_usuario_logado].append(f"----- {data_hora_atual} - Removido {valor} créditos -----")
        print(f"{valor} créditos removidos. Você agora tem {creditos_usuarios[indice]} créditos.")
    else:
        print("Créditos insuficientes.")

def gerar_relatorio(id_usuario_logado):
    print("\nRelatório de uso:\n")
    if relatorios_usuarios[id_usuario_logado] == []:
        print("Realize alguma operação dentro do aplicativo para que possa gerar um relatório de uso")

    for registro in relatorios_usuarios[id_usuario_logado]:
        print(registro)

    data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y às %H:%M:%S")
    print(f"\nRelatório gerado dia {data_hora_atual}.\n")


# "Main Function" of Program
while True:
    if contador_login > 0:
        continuar = int(input("0 - Sair\n1 - Tentar novamente\n"))
        if continuar == 0:
            break

    # Auth      
    usuario_entrada = input("\nDigite o nome de usuário:\n").lower()
    senha_entrada = input("\nSenha:\n").lower()

    for i in nome_usuarios:
        if i == usuario_entrada:
            index_usuario = nome_usuarios.index(i)
            id_usuario_logado = id_usuarios[index_usuario]
            verifica_usuario = True
            break

    for i in senha_usuarios:
        if i == senha_entrada:
            index_senha = senha_usuarios.index(i)
            verifica_senha = True
            break

    if not verifica_usuario:
        if not verifica_senha:
            print("\nUsuário e senha inválidos!\n")
        else:
            print("\nUsuário inválido!\n")
    # End Auth

    else:
        if index_usuario == index_senha:
            Entrada = True
            while Entrada: # Enter options
                print("\nSelecione a opção desejada:") 
                print("1 - Ver Créditos")
                print("2 - Adicionar Créditos")
                print("3 - Remover Créditos")
                print("4 - Gerar Relatório")
                print("0 - Sair")
                opcao = int(input("Opção: "))

                if opcao == 1:
                    ver_creditos(id_usuario_logado)
                elif opcao == 2:
                    valor = int(input("Digite o valor de créditos a adicionar: "))
                    adicionar_creditos(id_usuario_logado, valor)
                elif opcao == 3:
                    valor = int(input("Digite o valor de créditos a remover: "))
                    remover_creditos(id_usuario_logado, valor)
                elif opcao == 4:
                    gerar_relatorio(id_usuario_logado)
                elif opcao == 0:
                    print("Saindo...")
                    Entrada = False
                else:
                    print("Opção inválida.")
        else:
            print("\nSenha incorreta!\n")

    contador_login += 1
