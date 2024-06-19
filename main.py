from project import criar_blocos, alocar_horario, cancelar_alocacao, mostrar_blocos_disponiveis

def main():
    blocos = criar_blocos()
    while True:
        print("\nOpções disponíveis:")
        print("1. Alocar horário")
        print("2. Cancelar alocação")
        print("3. Consultar horários disponíveis")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Qual o seu nome? ")
            horario = input("Qual o horário (HH:MM)? ")
            if alocar_horario(blocos, nome, horario):
                print(f"Horário {horario} alocado para {nome}")
            else:
                print(f"Horário {horario} não está disponível")
        elif opcao == "2":
            horario = input("Qual o horário a ser cancelado (HH:MM)? ")
            if cancelar_alocacao(blocos, horario):
                print(f"Horário {horario} foi cancelado")
            else:
                print(f"Horário {horario} não pôde ser cancelado")
        elif opcao == "3":
            horarios_disponiveis = mostrar_blocos_disponiveis(blocos)
            print("Horários disponíveis:")
            for horario in horarios_disponiveis:
                print(horario)
        elif opcao == "4":
            print("Saindo do sistema de agendamento.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
