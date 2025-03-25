# 📌 Gerenciador de Tarefas

Este projeto é um **Gerenciador de Tarefas** simples, feito em Python. Ele permite adicionar, listar, editar e excluir tarefas, salvando os dados em um arquivo (`tarefas.txt`) para que as informações persistam entre execuções.

## 📥 Instalação

Certifique-se de ter o **Python 3** instalado no seu computador. Para verificar, execute:
```sh
python --version
```
Caso o Python não esteja instalado, baixe-o em [python.org](https://www.python.org/).

### 🔽 Baixando o Projeto
Clone este repositório ou baixe os arquivos manualmente:
```sh
git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas
```

## 🚀 Como Usar
Execute o script principal com o seguinte comando:
```sh
python main.py
```
O menu interativo será exibido:
```
=== Menu ===
1. Adicionar tarefa
2. Listar tarefas
3. Editar tarefa
4. Excluir tarefa
5. Sair
Escolha uma opção:
```

### 1️⃣ Adicionar uma Tarefa
Escolha a opção **1** e insira os detalhes da tarefa:
```
Digite o nome da tarefa: Estudar Python
Digite a data de conclusão (dd/mm/aaaa): 30/04/2025
Digite a prioridade (baixa, média, alta): alta
Tarefa adicionada com sucesso!
```

### 2️⃣ Listar Tarefas
Escolha a opção **2** para exibir as tarefas cadastradas:
```
1. Estudar Python | 30/04/2025 | alta
2. Fazer exercícios | 01/05/2025 | média
```

### 3️⃣ Editar uma Tarefa
Escolha a opção **3** e selecione a tarefa para edição:
```
Escolha o número da tarefa para editar: 1
Novo nome da tarefa: Praticar Python
Nova data de conclusão: 02/05/2025
Nova prioridade: alta
Tarefa atualizada com sucesso!
```

### 4️⃣ Excluir uma Tarefa
Escolha a opção **4** e remova a tarefa desejada:
```
Escolha o número da tarefa para excluir: 2
Tarefa excluída com sucesso!
```

### 5️⃣ Sair e Salvar
Escolha **5** para salvar as tarefas e sair do programa.

## 🛠 Estrutura do Código
- `main.py` - Arquivo principal contendo a lógica do programa.
- `tarefas.txt` - Armazena as tarefas salvas (criado automaticamente).

## 🔄 Como Contribuir
1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua feature:
   ```sh
   git checkout -b minha-feature
   ```
3. Faça suas alterações e **commite**:
   ```sh
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Faça um **push** para sua branch:
   ```sh
   git push origin minha-feature
   ```
5. Abra um **Pull Request** no GitHub.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar! 🚀

