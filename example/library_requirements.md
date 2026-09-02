# Functional Requirements (FRs)
## FR001

Objective: Permitir ao usuário consultar o catálogo completo de livros da biblioteca.

Description: O Usuário deve ser capaz de visualizar todo o acervo de livros disponível na biblioteca.

Usuário

Priority: must do

### **Depends on**



## FR002

Objective: Informar ao usuário quais livros podem ser emprestados no momento.

Description: O Usuário deve ser capaz de verificar quais livros estão disponíveis para empréstimos.

Usuário

Priority: must do

### **Depends on**

* FR001


## FR003

Objective: Formalizar a retirada de um livro por um usuário, controlando o processo de empréstimo.

Description: O Bibliotecário deve ser capaz de registrar um empréstimo de livro para um usuário.

Bibliotecário

Priority: must do

### **Depends on**

* FR009
* FR008
* BR001


## FR004

Objective: Fornecer ao bibliotecário detalhes específicos sobre cada livro e suas cópias.

Description: O Bibliotecário deve ser capaz de consultar livros e seus exemplares individualmente.

Bibliotecário

Priority: must do

### **Depends on**

* FR008


## FR005

Objective: Permitir ao bibliotecário acessar informações detalhadas sobre cada usuário.

Description: O Bibliotecário deve ser capaz de consultar usuários individualmente.

Bibliotecário

Priority: must do

### **Depends on**

* FR009


## FR006

Objective: Oferecer ao bibliotecário uma visão completa das transações de empréstimo de um usuário.

Description: O Bibliotecário deve ser capaz de consultar o histórico de empréstimos de um usuário, sejam eles ativos ou passados.

Bibliotecário

Priority: must do

### **Depends on**

* FR005
* FR010


## FR007

Objective: Garantir a aplicação das políticas de multa da biblioteca de forma consistente.

Description: O sistema deve aplicar multas automaticamente aos usuários que não devolverem os livros dentro do prazo estipulado.

Sistema

Priority: must do

### **Depends on**

* FR010
* BR003


## FR008

Objective: Manter um registro atualizado e organizado de todos os livros disponíveis na biblioteca.

Description: O sistema deve gerenciar o catálogo completo de livros, incluindo adição, remoção e atualização de informações de títulos e exemplares.

Sistema

Priority: must do

### **Depends on**

* BR002


## FR009

Objective: Manter um registro atualizado e preciso de todos os usuários da biblioteca.

Description: O sistema deve gerenciar os registros dos usuários, incluindo cadastro, atualização e remoção de dados.

Sistema

Priority: must do

### **Depends on**



## FR010

Objective: Manter um controle eficiente sobre o status de todos os livros emprestados e seus prazos.

Description: O sistema deve gerenciar todos os empréstimos realizados, desde o registro até a devolução.

Sistema

Priority: must do

### **Depends on**

* FR008
* FR009




# Non Functional Requirements (NFRs)


# Business Rules (BRs)
## BR001

Um usuário pode pegar apenas um livro emprestado por vez.

## BR002

A biblioteca deve ter, ao menos, 3 exemplares de todos os livros a todo momento, exceto pelos livros que a biblioteca possui menos de 3 exemplares.

## BR003

Caso um livro emprestado não seja devolvido dentro da data limite, o usuário que emprestou o livro deve pagar uma multa.



# Questions
