# Usecases
## Consultar Acervo

### Events

#### Visualizar Acervo Completo

Performed by: Usuário

Related to: FR001

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Usuário solicita a visualização do acervo completo. | Input: Usuário informa a intenção de visualizar o acervo. | S002|
| S002 | Sistema recupera todos os livros do catálogo. | Read titulo, autor, isbn (Livro);  | S003|
| S003 | Sistema exibe a lista completa de livros ao Usuário. | Output: A lista de livros é apresentada ao Usuário. | |
#### Visualizar Livros Disponíveis para Empréstimo

Performed by: Usuário

Related to: FR002

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Usuário solicita a visualização de livros disponíveis para empréstimo. | Input: Usuário informa a intenção de visualizar os livros disponíveis. | S002|
| S002 | Sistema recupera os livros do catálogo que possuem exemplares disponíveis para empréstimo. | Read status (Exemplar);  | S003|
| S003 | Sistema exibe a lista de livros disponíveis para empréstimo ao Usuário. | Output: A lista de livros disponíveis é apresentada ao Usuário. | |
## Realizar Empréstimo

### Events

#### Registrar Empréstimo

Performed by: Bibliotecário

Related to: FR003

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Bibliotecário inicia o processo de registro de empréstimo. | Input: Bibliotecário acessa a funcionalidade de registro de empréstimo. | S002|
| S002 | Bibliotecário informa o ID do Usuário e o ID do Livro a ser emprestado. | Input: Dados do Usuário e do Livro são informados. | S003|
| S003 | Sistema valida se o Usuário já possui um livro emprestado. | decision | S004; S005|
| S004 | Sistema exibe mensagem de erro informando que o Usuário já possui um livro emprestado. | Output: Mensagem de erro de validação apresentada. | |
| S005 | Sistema valida se há exemplares disponíveis para o Livro. | decision | S006; S007|
| S006 | Sistema exibe mensagem de erro informando que não há exemplares disponíveis para o livro. | Output: Mensagem de erro de validação apresentada. | |
| S007 | Sistema registra um novo Empréstimo associando o Usuário e um Exemplar disponível do Livro. | Create usuario, exemplar, dataEmprestimo, dataDevolucaoPrevista, status (Empréstimo);  | S008|
| S008 | Sistema atualiza o status do Exemplar para "emprestado". | Update status (Exemplar);  | S009|
| S009 | Sistema informa ao Bibliotecário que o empréstimo foi registrado com sucesso. | Output: Confirmação de empréstimo bem-sucedido. | |
## Consultar Informações Administrativas

### Events

#### Consultar Livro e Exemplares

Performed by: Bibliotecário

Related to: FR004

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Bibliotecário solicita a consulta de um livro. | Input: Bibliotecário acessa a funcionalidade de consulta de livros. | S002|
| S002 | Bibliotecário informa o ID ou título do Livro. | Input: Dados do livro são informados para busca. | S003|
| S003 | Sistema recupera as informações do Livro e seus Exemplares. | Read id, status, livro (Exemplar);  | S004|
| S004 | Sistema exibe os detalhes do Livro e a lista de seus Exemplares ao Bibliotecário. | Output: Detalhes do livro e exemplares são apresentados. | |
#### Consultar Usuário

Performed by: Bibliotecário

Related to: FR005

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Bibliotecário solicita a consulta de um Usuário. | Input: Bibliotecário acessa a funcionalidade de consulta de usuários. | S002|
| S002 | Bibliotecário informa o ID ou nome do Usuário. | Input: Dados do usuário são informados para busca. | S003|
| S003 | Sistema recupera as informações do Usuário. | Read id, nome, endereco, telefone, email (Usuário);  | S004|
| S004 | Sistema exibe os detalhes do Usuário ao Bibliotecário. | Output: Detalhes do usuário são apresentados. | |
#### Consultar Histórico de Empréstimos do Usuário

Performed by: Bibliotecário

Related to: FR006

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Bibliotecário solicita a consulta do histórico de empréstimos de um Usuário. | Input: Bibliotecário acessa a funcionalidade de histórico de empréstimos. | S002|
| S002 | Bibliotecário informa o ID ou nome do Usuário. | Input: Dados do usuário são informados para busca do histórico. | S003|
| S003 | Sistema recupera o histórico de Empréstimos (ativos e passados) do Usuário. | Read id (Usuário);  | S004|
| S004 | Sistema exibe o histórico de Empréstimos do Usuário ao Bibliotecário. | Output: Histórico de empréstimos do usuário é apresentado. | |
## Processar Multas

### Events

#### Aplicar Multa por Atraso

Performed by: Sistema

Related to: FR007

Steps:

| Code | Description | Category | Next Step |
| --- | --- | --- | --- |
| S001 | Sistema verifica periodicamente os Empréstimos com data limite de devolução vencida. | Read dataDevolucaoPrevista, dataDevolucaoReal, status, multa (Empréstimo);  | S002|
| S002 | Para cada Empréstimo vencido, o sistema verifica se uma Multa já foi aplicada. | decision | S003; S001|
| S003 | Sistema calcula o valor da Multa com base nos dias de atraso. | Complex operation (math): Cálculo do valor da multa com base na data de devolução. | S004|
| S004 | Sistema registra uma nova Multa para o Usuário associado ao Empréstimo. | Create valor, dataAplicacao, status, emprestimo, usuario (Multa);  | S005|
| S005 | Sistema atualiza o status do Empréstimo para indicar que a multa foi aplicada e associa a multa. | Update multa (Empréstimo);  | S001|


# Questions
Quais são os atributos das classes Livro, Exemplar, Usuário, Empréstimo e Multa? (Consultar Acervo; Realizar Empréstimo; Consultar Informações Administrativas; Processar Multas)

Como a regra de negócio 'A biblioteca deve ter, ao menos, 3 exemplares de todos os livros a todo momento, exceto pelos livros que a biblioteca possui menos de 3 exemplares.' (BR002) é monitorada e aplicada pelo sistema? Existe um evento específico para isso, ou é uma validação durante a adição/remoção de livros? ()

Quais eventos e atores são responsáveis pela criação, atualização e exclusão de Livros e Usuários no sistema, conforme descrito em FR008 e FR009? ()

