Aqui estão as classes de domínio identificadas, seus atributos, associações e heranças, com base na descrição fornecida e nos Casos de Uso.

---

### Classes de Domínio

**1. Classe: Livro**
*   **Descrição:** Representa uma obra literária no catálogo da biblioteca, que pode ter múltiplos exemplares físicos.
*   **Atributos:**
    *   `ISBN: String {unique, primary key}`
    *   `titulo: String`
    *   `autor: String`
    *   `editora: String`
    *   `edicao: String`
    *   `categoria: String`
    *   `anoPublicacao: Integer`
*   **Associações:**
    *   `possui` `Exemplar` [5..*]
        *   Um `Livro` possui no mínimo 5 e muitos `Exemplar`es.
        *   (Reflete a regra de negócio: \"cada livro possua sempre, no mínimo, 5 exemplares cadastrados no acervo\")

**2. Classe: Exemplar**
*   **Descrição:** Representa uma unidade física específica de um `Livro`, disponível para empréstimo ou consulta.
*   **Atributos:**
    *   `codigoPatrimonio: String {unique, primary key}`
    *   `estadoConservacao: EstadoConservacao` (Enum)
    *   `localizacao: String`
    *   `situacao: SituacaoExemplar` (Enum)
*   **Associações:**
    *   `éUm` `Livro` [1]
        *   Cada `Exemplar` é uma cópia de exatamente um `Livro`.
    *   `temHistoricoDe` `Empréstimo` [*]
        *   Um `Exemplar` pode ter um histórico de muitos `Empréstimo`s.

**3. Classe: Usuário**
*   **Descrição:** Representa uma pessoa cadastrada na biblioteca que pode realizar empréstimos.
*   **Atributos:**
    *   `idUsuario: String {unique, primary key}`
    *   `nome: String`
    *   `endereco: String`
    *   `contato: String`
*   **Associações:**
    *   `realiza` `Empréstimo` [*]
        *   Um `Usuário` pode realizar muitos `Empréstimo`s.

**4. Classe: Empréstimo**
*   **Descrição:** Registra a transação de um `Exemplar` sendo emprestado a um `Usuário`, incluindo datas e status.
*   **Atributos:**
    *   `idEmprestimo: String {unique, primary key}`
    *   `dataEmprestimo: Date`
    *   `dataPrevistaDevolucao: Date`
    *   `dataEfetivaDevolucao: Date {nullable}`
    *   `situacaoEmprestimo: SituacaoEmprestimo` (Enum)
*   **Associações:**
    *   `emprestadoPor` `Usuário` [1]
        *   Cada `Empréstimo` é realizado por exatamente um `Usuário`.
    *   `refereSeA` `Exemplar` [1]
        *   Cada `Empréstimo` refere-se a exatamente um `Exemplar`.

---

### Enums

**1. Enum: EstadoConservacao**
*   **Descrição:** Descreve o estado físico de um exemplar.
*   **Valores:**
    *   `NOVO`
    *   `BOM`
    *   `REGULAR`
    *   `DANIFICADO`
    *   `INUTILIZAVEL`

**2. Enum: SituacaoExemplar**
*   **Descrição:** Descreve a disponibilidade e o status atual de um exemplar.
*   **Valores:**
    *   `DISPONIVEL`
    *   `EMPRESTADO`
    *   `RESERVADO`
    *   `EM_MANUTENCAO`
    *   `INDISPONIVEL`

**3. Enum: SituacaoEmprestimo**
*   **Descrição:** Descreve o status de um registro de empréstimo.
*   **Valores:**
    *   `ATIVO`
    *   `CONCLUIDO`

---

### Perguntas

*   **Q1: Reserva de Exemplar:** O sistema permite a reserva de exemplares? Se sim, qual ator realiza a reserva (Usuário da Biblioteca ou Funcionário da Biblioteca) e quais são os eventos e passos para realizar e gerenciar uma reserva?
    *   *Justificativa:* A situação \"reservado\" é mencionada para os exemplares no texto e na enumeração `SituacaoExemplar`, mas não há descrição explícita de uma funcionalidade de reserva, de como um exemplar entra ou sai desse estado, ou de qual ator seria responsável por essa ação nos Casos de Uso.