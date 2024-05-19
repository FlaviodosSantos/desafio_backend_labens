# Seleção Labens 2024 - Desafio Backend

### Desafio
Criar uma API para o Gerenciamento de Tarefas (to-do list)

### Descrição do Projeto
API para gerenciar uma lista de tarefas (to-do list). A API deve permitir que os usuários criem, atualizem, excluam e visualizem tarefas. Cada tarefa deve ter um título, uma descrição, um prazo (data planejada para conclusão), uma data da conclusão, e uma situação (nova, em andamento, concluída ou cancelada).

#

### Rotas

- /docs - Documentação da api (com a instalação da biblioteca 'coreapi')

- /todo/ - GET - lista todas as tarefas
- /todo/ - POST - cria nova tarefa
- /todo/{id} - GET - detalhe de uma tarefa
- /todo/{id} - PUT - edita uma tarefa
- /todo/{id} - DELETE - exclui uma tarefa

#
### Inserir dados automaticamente
Dados aleatórios gerados no [Generatedata](https://generatedata.com/generator) e salvos em .csv . 

Para chamar a função, no terminal do projeto, abra o terminal python digitando "python"(win) ou "python3"(linux). Importe a função e chame-a:
```python
from todo.views import inserir_dados

inserir_dados()
```

