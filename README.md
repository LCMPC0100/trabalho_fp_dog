# trabalho_fp_dog
Descrição do Problema:
Um centro de adoção de animais precisa controlar cães, gatos e outros pets, além de
gerenciar informações sobre adoções, cuidados, vacinas e atividades diárias.
Atualmente, o processo é manual e confuso, tornando difícil acompanhar saúde,
histórico e adoções dos animais. Pensando nisso, vamos criar o sistema “Adoção+”,
que ajudará a equipe a organizar todos os registros de forma prática e eficiente.

Requisitos Funcionais:
1. CRUD de Animais:
O usuário poderá adicionar, visualizar, editar e excluir animais, com
informações como: nome, espécie, raça, idade, estado de saúde, data de
chegada e comportamento.

2. Cadastro de Cuidados e Atividades:
O usuário poderá registrar tarefas para cada animal, como vacinas, banhos,
consultas veterinárias, treino e etc. Cada tarefa com data prevista e
responsável.

3. Contagem Regressiva e Alertas:
Ao visualizar o cadastro de um animal, o sistema exibirá quantos dias faltam
para as próximas vacinas, consultas ou tarefas importantes cadastradas no
item anterior.

4. Armazenamento de Dados:
Todos os registros serão salvos em arquivo .csv ou .txt, garantindo histórico
completo de animais, tarefas e adoções.

5. Sugestões Personalizadas:
Com base na idade, espécie e comportamento do animal, o sistema poderá
sugerir possíveis adotantes, cuidados especiais, compatibilidade com outros
animais, atividades de socialização e etc.

6. Funcionalidade Extra:
Sejam Criativos.

Requisitos não funcionais:
1. Deve ser feito em Python sem o uso de bibliotecas adicionais.
Utilizar a linha de comando para entrada e saída (interação pelo terminal);
a. Exceções de bibliotecas:
os -> os.system("clear") ou “cls”.
datetime
random
Se precisar de outra biblioteca, verifique antes com os professores.

2. O trabalho deve ser feito em grupo.
a. Trabalhos individuais perderão 50% da nota.
3. O código deve estar organizado, portanto, deve conter:
a. Funções para dividir o código de forma lógica e evitar repetições;
b. Tratamento de exceções, para garantir que seu código esteja pronto para
tratar casos inesperados.
c. Legibilidade do código, incluindo nomeação de variáveis e funções.
4. Deve ser feito um manual do usuário, explicando como utilizar a ferramenta e
restrições gerais que a aplicação tenha.
a. Fiquem à vontade para escolher como será feito esse manual. Pode ser um
pdf, site, vídeo, carta...
b. O manual é o readme que pode estar disponível no github do projeto (caso o
grupo utilize o github, opcional, não será visto em sala de aula).
5. Não será aceito entregas atrasadas.
6. Apresentação:
a. A equipe deve apresentar o projeto feito para os professores.
b. Todos envolvidos da equipe devem explicar alguma parte, e perguntas
direcionadas serão feitas durante a apresentação.
7. A entrega será em uma atividade do classroom
a. O que deve ser entregue: Código da aplicação e Manual do usuário.

Critérios de avaliação:
● Apresentação (50 pontos - nota individual):
○ Participação durante a apresentação do projeto;
○ Perguntas durante a apresentação.
● Código (50 pontos - nota por grupo):
○ Legibilidade e Organização do código;
○ Tratamento de erros e Utilização de Arquivos;
○ Apresentação da ferramenta e manual do usuário;
○ Funcionalidade extra.
