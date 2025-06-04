def exibir_menu():
    print("\nMenu de Tarefas")
    print("1 - Adicionar nova tarefa;")
    print("2 - Listar todas as tarefas;")
    print("3 - Marcar tarefa como concluída")
    print("0 - Sair do programa")
    return input("Escolha uma opção:\t")

def criar_tarefa(descricao):
    codigo = len(tarefas) + 1
    tarefa = {'codigo': codigo, 'descricao': descricao, 'status': 'pendente'}
    tarefas.append(tarefa)
    return tarefa

tarefa = None

while True:
    opcao = exibir_menu()
    if opcao == "1":
        print("Opção 1 selecionada: Adicionar nova tarefa")
        descricao = input("Informe a descrição da tarefa:\t")
        if 'tarefas' not in globals():
            tarefas = []
        tarefa = criar_tarefa(descricao)
        print(f"Tarefa adicionada: {tarefa['codigo']} - {tarefa['descricao']} (Status: {tarefa['status']})")

    elif opcao == "2":
        print("Opção 2 selecionada: Listar todas as tarefas")
        if 'tarefas' in globals() and tarefas:
            for tarefa in tarefas:
                print(f"Código: {tarefa['codigo']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}")
        else:
            print("Nenhuma tarefa cadastrada.")
    elif opcao == "3":
        print("Opção 3 selecionada: Marcar tarefa como concluída")
        codigo = int(input("Informe o código da tarefa a ser marcada como concluída:\t"))
        if 'tarefas' in globals() and tarefas:
            tarefa_encontrada = next((t for t in tarefas if t['codigo'] == codigo), None)
            if tarefa_encontrada:
                tarefa_encontrada['status'] = 'concluída'
                print(f"Tarefa {codigo} marcada como concluída.")
            else:
                print(f"Tarefa com código {codigo} não encontrada.")
        else:
            print("Nenhuma tarefa cadastrada.")
    elif opcao == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida, tente novamente.")