def carregar_tarefas():
    try:
        with open('tarefas.txt', 'r') as file:
            tarefas = [line.strip() for line in file.readlines()]
        return tarefas
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.txt', 'w') as file:
        for tarefa in tarefas:
            file.write(tarefa + '/n')

def adicionar_tarefa(tarefas):
    nome = input('Digite o nome da tarefa: ')
    data = input('Digite a data de conclusão (dd/mm/aaaa): ')
    prioridade = input('Digite a prioridade (baixa/media/alta): ')
    tarefa = f"{nome} | {data} | {prioridade}"
    tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')

def listar_tarefas(tarefas):
    if not tarefas:
        print('Não há tarefas cadastradas.')
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f'{i}. {tarefa}')

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input('Escolha o número da tarefa para editar: ')) - 1
        if 0 <= indice < len(tarefas):
            nome = input('Novo nome da tarefa: ')
            data = input('Nova data de conclusão: ')
            prioridade = input('Nova prioridade: ')
            tarefas[indice] = f'{nome} | {data} | {prioridade}'
            print('Tarefa atualizada com sucesso!')
        else:
            print('Tarefa inválida!')
    except ValueError:
        print('Valor inválido!')

def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input('Escolha o número da tarefa para excluir: ')) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print('Tarefa excluida com sucesso!')
        else:
            print('Tarefa inválida!')
    except ValueError:
        print('Valor inválido!')

def main():
    tarefas = carregar_tarefas()

    while True:
        print('\n=== Menu ===')
        print('1. Adicionar tarefa')
        print('2. Listar tarefa')
        print('3. Editar tarefa')
        print('4. Excluir tarefa')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            editar_tarefa(tarefas)
        elif opcao == '4':
            excluir_tarefa(tarefas)
        elif opcao == '5':
            salvar_tarefas(tarefas)
            print('Saindo...')
            break
        else:
            print('Opção invalida!')

if __name__ == '__main__':
    main()
