Aqui estão os Casos de Uso atualizados, com seus atores, eventos e sequências de passos, baseados no texto fornecido, na Domain Narrative e nos Requisitos.

**Atores Identificados:**

*   **Funcionário da Biblioteca:** Responsável por gerenciar o acervo (livros e exemplares), cadastrar e gerenciar usuários, registrar empréstimos e devoluções, atualizar estados de conservação e situações dos exemplares, e realizar consultas detalhadas sobre o acervo e o histórico.
*   **Usuário da Biblioteca:** Membro cadastrado da biblioteca que pode consultar o acervo disponível, seus próprios empréstimos ativos e seu histórico de empréstimos.

---

### Casos de Uso para o Ator: Funcionário da Biblioteca

#### Use Case: Cadastrar Livro
*   **Descrição:** Permite ao Funcionário da Biblioteca registrar um novo livro no catálogo do sistema.
*   **Eventos:**
    1.  **Funcionário solicita cadastro de novo livro.**
        *   Passo 1: Funcionário acessa a funcionalidade de cadastro de livros.
    2.  **Sistema exibe formulário de cadastro de livro.**
        *   Passo 1: Sistema apresenta um formulário com campos para as informações do livro.
    3.  **Funcionário preenche informações do livro.**
        *   Passo 1: Funcionário insere Título, Autor, Editora, Edição, ISBN, Categoria e Ano de Publicação.
    4.  **Funcionário confirma cadastro do livro.**
        *   Passo 1: Funcionário aciona o comando para salvar o livro.
    5.  **Sistema valida informações do livro.**
        *   Passo 1: Sistema verifica a integridade e unicidade dos dados (e.g., ISBN).
        *   Passo 2: Se os dados forem inválidos, Sistema informa o erro e retorna ao evento 3.
    6.  **Sistema registra o livro.**
        *   Passo 1: Sistema persiste as informações do livro no catálogo.
    7.  **Sistema exige cadastro inicial de exemplares (FR-028).**
        *   Passo 1: Sistema notifica o Funcionário que o livro recém-cadastrado precisa de no mínimo 5 exemplares (BR-002).
    8.  **Funcionário cadastra os exemplares iniciais.**
        *   Passo 1: Funcionário é guiado para a funcionalidade de \"Cadastrar Exemplar\" para adicionar os exemplares necessários até atingir o mínimo de 5.

#### Use Case: Atualizar Livro
*   **Descrição:** Permite ao Funcionário da Biblioteca modificar as informações de um livro existente no catálogo.
*   **Eventos:**
    1.  **Funcionário busca livro para atualização.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de livros.
        *   Passo 2: Funcionário utiliza critérios de busca (e.g., título, autor, ISBN) para localizar o livro.
    2.  **Sistema exibe resultados da busca e detalhes do livro.**
        *   Passo 1: Sistema apresenta uma lista de livros correspondentes ou os detalhes do livro selecionado.
    3.  **Funcionário seleciona livro e solicita edição.**
        *   Passo 1: Funcionário escolhe o livro desejado e aciona a opção de edição.
    4.  **Sistema exibe formulário de edição pré-preenchido.**
        *   Passo 1: Sistema carrega as informações atuais do livro no formulário de edição.
    5.  **Funcionário edita informações do livro.**
        *   Passo 1: Funcionário modifica os campos desejados (e.g., título, editora).
    6.  **Funcionário confirma atualização do livro.**
        *   Passo 1: Funcionário aciona o comando para salvar as alterações.
    7.  **Sistema valida e atualiza o livro.**
        *   Passo 1: Sistema verifica a integridade dos dados atualizados.
        *   Passo 2: Se os dados forem válidos, Sistema persiste as alterações.
        *   Passo 3: Se os dados forem inválidos, Sistema informa o erro e retorna ao evento 5.

#### Use Case: Excluir Livro
*   **Descrição:** Permite ao Funcionário da Biblioteca remover um livro do catálogo do sistema.
*   **Eventos:**
    1.  **Funcionário busca livro para exclusão.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de livros.
        *   Passo 2: Funcionário utiliza critérios de busca para localizar o livro.
    2.  **Sistema exibe resultados da busca e detalhes do livro.**
        *   Passo 1: Sistema apresenta uma lista de livros correspondentes ou os detalhes do livro selecionado.
    3.  **Funcionário seleciona livro e solicita exclusão.**
        *   Passo 1: Funcionário escolhe o livro desejado e aciona a opção de exclusão.
    4.  **Sistema verifica se o livro possui exemplares associados.**
        *   Passo 1: Sistema consulta o número de exemplares vinculados ao livro.
        *   Passo 2: Se o livro possuir exemplares, Sistema impede a exclusão e informa o Funcionário que todos os exemplares devem ser excluídos primeiro.
    5.  **Funcionário confirma exclusão do livro.**
        *   Passo 1: Funcionário confirma a intenção de excluir o livro.
    6.  **Sistema remove o livro do catálogo.**
        *   Passo 1: Sistema exclui o registro do livro.

#### Use Case: Cadastrar Exemplar
*   **Descrição:** Permite ao Funcionário da Biblioteca registrar um novo exemplar físico para um livro existente.
*   **Eventos:**
    1.  **Funcionário seleciona livro para associar exemplar.**
        *   Passo 1: Funcionário busca e seleciona um livro existente no catálogo.
    2.  **Funcionário solicita cadastro de novo exemplar.**
        *   Passo 1: Funcionário aciona a funcionalidade para adicionar um exemplar a este livro.
    3.  **Sistema exibe formulário de cadastro de exemplar.**
        *   Passo 1: Sistema apresenta um formulário com campos para as informações do exemplar.
    4.  **Funcionário preenche informações do exemplar.**
        *   Passo 1: Funcionário insere Código de Patrimônio, Estado de Conservação inicial (e.g., \"novo\"), Localização na biblioteca e Situação inicial (\"disponível para empréstimo\").
    5.  **Funcionário confirma cadastro do exemplar.**
        *   Passo 1: Funcionário aciona o comando para salvar o exemplar.
    6.  **Sistema valida informações do exemplar.**
        *   Passo 1: Sistema verifica a integridade e unicidade do Código de Patrimônio.
        *   Passo 2: Se os dados forem inválidos, Sistema informa o erro e retorna ao evento 4.
    7.  **Sistema registra o exemplar e atualiza contagem.**
        *   Passo 1: Sistema persiste as informações do exemplar, associando-o ao livro.
        *   Passo 2: Sistema atualiza a contagem total de exemplares para o livro correspondente.

#### Use Case: Atualizar Exemplar
*   **Descrição:** Permite ao Funcionário da Biblioteca modificar as informações de um exemplar físico existente.
*   **Eventos:**
    1.  **Funcionário busca exemplar para atualização.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de exemplares.
        *   Passo 2: Funcionário utiliza critérios de busca (e.g., código de patrimônio, título do livro) para localizar o exemplar.
    2.  **Sistema exibe resultados da busca e detalhes do exemplar.**
        *   Passo 1: Sistema apresenta uma lista de exemplares correspondentes ou os detalhes do exemplar selecionado.
    3.  **Funcionário seleciona exemplar e solicita edição.**
        *   Passo 1: Funcionário escolhe o exemplar desejado e aciona a opção de edição.
    4.  **Sistema exibe formulário de edição pré-preenchido.**
        *   Passo 1: Sistema carrega as informações atuais do exemplar no formulário de edição.
    5.  **Funcionário edita informações do exemplar.**
        *   Passo 1: Funcionário modifica os campos desejados (e.g., localização, estado de conservação).
    6.  **Funcionário confirma atualização do exemplar.**
        *   Passo 1: Funcionário aciona o comando para salvar as alterações.
    7.  **Sistema valida e atualiza o exemplar.**
        *   Passo 1: Sistema verifica a integridade dos dados atualizados.
        *   Passo 2: Se os dados forem válidos, Sistema persiste as alterações.
        *   Passo 3: Se os dados forem inválidos, Sistema informa o erro e retorna ao evento 5.

#### Use Case: Excluir Exemplar
*   **Descrição:** Permite ao Funcionário da Biblioteca remover um exemplar físico do acervo.
*   **Eventos:**
    1.  **Funcionário busca exemplar para exclusão.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de exemplares.
        *   Passo 2: Funcionário utiliza critérios de busca para localizar o exemplar.
    2.  **Sistema exibe resultados da busca e detalhes do exemplar.**
        *   Passo 1: Sistema apresenta uma lista de exemplares correspondentes ou os detalhes do exemplar selecionado.
    3.  **Funcionário seleciona exemplar e solicita exclusão.**
        *   Passo 1: Funcionário escolhe o exemplar desejado e aciona a opção de exclusão.
    4.  **Sistema verifica se a exclusão viola a regra BR-002 (FR-027).**
        *   Passo 1: Sistema calcula a quantidade de exemplares restantes para o livro após a exclusão.
        *   Passo 2: Se a quantidade for menor que 5, Sistema impede a exclusão e informa o Funcionário.
    5.  **Sistema verifica se o exemplar está emprestado ou reservado.**
        *   Passo 1: Sistema consulta a situação atual do exemplar.
        *   Passo 2: Se o exemplar estiver emprestado ou reservado, Sistema impede a exclusão e informa o Funcionário.
    6.  **Funcionário confirma exclusão do exemplar.**
        *   Passo 1: Funcionário confirma a intenção de excluir o exemplar.
    7.  **Sistema remove o exemplar do acervo.**
        *   Passo 1: Sistema exclui o registro do exemplar.
        *   Passo 2: Sistema atualiza a contagem total de exemplares para o livro correspondente.

#### Use Case: Registrar Manutenção de Exemplar
*   **Descrição:** Permite ao Funcionário da Biblioteca registrar que um exemplar está em manutenção e, posteriormente, removê-lo desse estado.
*   **Eventos:**
    1.  **Funcionário busca exemplar para manutenção.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de exemplares.
        *   Passo 2: Funcionário utiliza critérios de busca para localizar o exemplar.
    2.  **Sistema exibe detalhes do exemplar.**
        *   Passo 1: Sistema apresenta os detalhes do exemplar selecionado.
    3.  **Funcionário solicita registro de manutenção.**
        *   Passo 1: Funcionário aciona a opção para colocar o exemplar em manutenção.
    4.  **Sistema verifica situação atual do exemplar.**
        *   Passo 1: Se o exemplar estiver emprestado ou reservado, Sistema impede a manutenção e informa o Funcionário.
    5.  **Sistema atualiza situação do exemplar para \"em manutenção\".**
        *   Passo 1: Sistema altera o estado do exemplar para \"em manutenção\".
        *   Passo 2: Sistema registra a data de início da manutenção.
    6.  **Funcionário solicita remoção da manutenção.** (Fluxo de Continuação)
        *   Passo 1: Funcionário busca exemplar que está em manutenção.
        *   Passo 2: Funcionário aciona a opção para remover o exemplar da manutenção.
    7.  **Sistema atualiza situação do exemplar para \"disponível\".**
        *   Passo 1: Sistema altera o estado do exemplar para \"disponível para empréstimo\".
        *   Passo 2: Sistema registra a data de fim da manutenção.

#### Use Case: Registrar Empréstimo
*   **Descrição:** Permite ao Funcionário da Biblioteca registrar o empréstimo de um exemplar a um usuário.
*   **Eventos:**
    1.  **Funcionário seleciona usuário e exemplar.**
        *   Passo 1: Funcionário acessa a funcionalidade de empréstimos.
        *   Passo 2: Funcionário busca e seleciona um Usuário da Biblioteca.
        *   Passo 3: Funcionário busca e seleciona um Exemplar.
    2.  **Sistema verifica a elegibilidade para empréstimo.**
        *   Passo 1: Sistema verifica se o exemplar está \"disponível para empréstimo\".
        *   Passo 2: Sistema verifica a regra BR-001 (quantidade total de exemplares do livro > 5).
        *   Passo 3: Se o exemplar não estiver disponível ou a regra BR-001 for violada, Sistema informa o impedimento e retorna ao evento 1.
    3.  **Sistema exibe informações do empréstimo e solicita data de devolução.**
        *   Passo 1: Sistema exibe a data atual como data do empréstimo.
        *   Passo 2: Sistema solicita a data prevista para devolução.
    4.  **Funcionário informa data prevista de devolução.**
        *   Passo 1: Funcionário insere a data prevista.
    5.  **Funcionário confirma empréstimo.**
        *   Passo 1: Funcionário aciona o comando para registrar o empréstimo.
    6.  **Sistema registra empréstimo e atualiza estados.**
        *   Passo 1: Sistema cria um novo registro de empréstimo com usuário, exemplar, data de empréstimo, data prevista de devolução e situação \"ativo\".
        *   Passo 2: Sistema atualiza a situação do exemplar para \"emprestado\".
        *   Passo 3: Sistema registra o evento no histórico de empréstimos.

#### Use Case: Registrar Devolução
*   **Descrição:** Permite ao Funcionário da Biblioteca registrar a devolução de um exemplar.
*   **Eventos:**
    1.  **Funcionário busca empréstimo ativo para devolução.**
        *   Passo 1: Funcionário acessa a funcionalidade de devoluções.
        *   Passo 2: Funcionário busca o empréstimo por Usuário ou por Exemplar.
    2.  **Sistema exibe detalhes do empréstimo.**
        *   Passo 1: Sistema apresenta as informações do empréstimo ativo encontrado.
    3.  **Funcionário confirma devolução.**
        *   Passo 1: Funcionário aciona o comando para registrar a devolução.
    4.  **Sistema registra data efetiva de devolução e atualiza situação do empréstimo.**
        *   Passo 1: Sistema preenche a data efetiva de devolução com a data atual.
        *   Passo 2: Sistema atualiza a situação do empréstimo para \"concluído\".
    5.  **Sistema verifica e atualiza situação do exemplar.**
        *   Passo 1: Sistema verifica se o exemplar está \"reservado\" ou \"em manutenção\".
        *   Passo 2: Se não estiver reservado nem em manutenção, Sistema atualiza a situação do exemplar para \"disponível para empréstimo\".
        *   Passo 3: Se estiver reservado ou em manutenção, a situação do exemplar permanece a mesma (reservado ou em manutenção).
    6.  **Sistema permite reavaliar estado de conservação do exemplar.**
        *   Passo 1: Sistema exibe o estado de conservação atual do exemplar e oferece opção para alterá-lo.
    7.  **Funcionário pode atualizar estado de conservação.**
        *   Passo 1: Funcionário seleciona um novo estado de conservação, se necessário.
    8.  **Sistema registra histórico de devolução.**
        *   Passo 1: Sistema registra o evento no histórico de devoluções.

#### Use Case: Cadastrar Usuário
*   **Descrição:** Permite ao Funcionário da Biblioteca registrar um novo usuário no sistema.
*   **Eventos:**
    1.  **Funcionário solicita cadastro de novo usuário.**
        *   Passo 1: Funcionário acessa a funcionalidade de cadastro de usuários.
    2.  **Sistema exibe formulário de cadastro de usuário.**
        *   Passo 1: Sistema apresenta um formulário com campos para as informações do usuário.
    3.  **Funcionário preenche informações do usuário.**
        *   Passo 1: Funcionário insere nome, endereço, contato, etc.
    4.  **Funcionário confirma cadastro do usuário.**
        *   Passo 1: Funcionário aciona o comando para salvar o usuário.
    5.  **Sistema valida e registra o usuário.**
        *   Passo 1: Sistema verifica a integridade e unicidade dos dados.
        *   Passo 2: Se os dados forem inválidos, Sistema informa o erro e retorna ao evento 3.
        *   Passo 3: Sistema persiste as informações do usuário.

#### Use Case: Atualizar Usuário
*   **Descrição:** Permite ao Funcionário da Biblioteca modificar as informações de um usuário existente.
*   **Eventos:**
    1.  **Funcionário busca usuário para atualização.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de usuários.
        *   Passo 2: Funcionário utiliza critérios de busca (e.g., nome, ID) para localizar o usuário.
    2.  **Sistema exibe resultados da busca e detalhes do usuário.**
        *   Passo 1: Sistema apresenta uma lista de usuários correspondentes ou os detalhes do usuário selecionado.
    3.  **Funcionário seleciona usuário e solicita edição.**
        *   Passo 1: Funcionário escolhe o usuário desejado e aciona a opção de edição.
    4.  **Sistema exibe formulário de edição pré-preenchido.**
        *   Passo 1: Sistema carrega as informações atuais do usuário no formulário de edição.
    5.  **Funcionário edita informações do usuário.**
        *   Passo 1: Funcionário modifica os campos desejados.
    6.  **Funcionário confirma atualização do usuário.**
        *   Passo 1: Funcionário aciona o comando para salvar as alterações.
    7.  **Sistema valida e atualiza o usuário.**
        *   Passo 1: Sistema verifica a integridade dos dados atualizados.
        *   Passo 2: Se os dados forem válidos, Sistema persiste as alterações.
        *   Passo 3: Se os dados forem inválidos, Sistema informa o erro e retorna ao evento 5.

#### Use Case: Excluir Usuário
*   **Descrição:** Permite ao Funcionário da Biblioteca remover um usuário do sistema.
*   **Eventos:**
    1.  **Funcionário busca usuário para exclusão.**
        *   Passo 1: Funcionário acessa a funcionalidade de gerenciamento de usuários.
        *   Passo 2: Funcionário utiliza critérios de busca para localizar o usuário.
    2.  **Sistema exibe resultados da busca e detalhes do usuário.**
        *   Passo 1: Sistema apresenta uma lista de usuários correspondentes ou os detalhes do usuário selecionado.
    3.  **Funcionário seleciona usuário e solicita exclusão.**
        *   Passo 1: Funcionário escolhe o usuário desejado e aciona a opção de exclusão.
    4.  **Sistema verifica empréstimos ativos do usuário.**
        *   Passo 1: Sistema consulta se o usuário possui empréstimos ativos.
        *   Passo 2: Se o usuário possuir empréstimos ativos, Sistema impede a exclusão e informa o Funcionário.
    5.  **Funcionário confirma exclusão do usuário.**
        *   Passo 1: Funcionário confirma a intenção de excluir o usuário.
    6.  **Sistema remove o usuário.**
        *   Passo 1: Sistema exclui o registro do usuário.

#### Use Case: Consultar Exemplares Emprestados
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar uma lista de todos os exemplares que estão atualmente emprestados.
*   **Eventos:**
    1.  **Funcionário solicita consulta de exemplares emprestados.**
        *   Passo 1: Funcionário acessa a funcionalidade de consulta de empréstimos.
    2.  **Sistema exibe lista de exemplares emprestados.**
        *   Passo 1: Sistema recupera e apresenta uma lista de exemplares com situação \"emprestado\", incluindo detalhes como título do livro, código do exemplar, usuário, data de empréstimo e data prevista de devolução.

#### Use Case: Consultar Usuários com Empréstimos Ativos
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar uma lista de usuários que possuem empréstimos ativos.
*   **Eventos:**
    1.  **Funcionário solicita consulta de usuários com empréstimos ativos.**
        *   Passo 1: Funcionário acessa a funcionalidade de consulta de usuários.
    2.  **Sistema exibe lista de usuários com empréstimos ativos.**
        *   Passo 1: Sistema recupera e apresenta uma lista de usuários que possuem pelo menos um empréstimo ativo, incluindo nome do usuário e, opcionalmente, a quantidade de empréstimos ativos.

#### Use Case: Consultar Datas Previstas de Devolução
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar as datas de devolução previstas para os empréstimos ativos.
*   **Eventos:**
    1.  **Funcionário solicita consulta de datas previstas de devolução.**
        *   Passo 1: Funcionário acessa a funcionalidade de consulta de empréstimos.
    2.  **Sistema exibe datas previstas de devolução.**
        *   Passo 1: Sistema recupera e apresenta uma lista de empréstimos ativos, mostrando o exemplar, o usuário e a respectiva data prevista de devolução.

#### Use Case: Consultar Exemplares Disponíveis
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar uma lista de exemplares que estão disponíveis para empréstimo.
*   **Eventos:**
    1.  **Funcionário solicita consulta de exemplares disponíveis.**
        *   Passo 1: Funcionário acessa a funcionalidade de consulta de acervo.
    2.  **Sistema exibe lista de exemplares disponíveis.**
        *   Passo 1: Sistema recupera e apresenta uma lista de exemplares com situação \"disponível para empréstimo\", incluindo título do livro e código do exemplar.

#### Use Case: Consultar Histórico de Empréstimos por Exemplar
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar o histórico completo de empréstimos e devoluções de um exemplar específico.
*   **Eventos:**
    1.  **Funcionário busca exemplar para histórico.**
        *   Passo 1: Funcionário acessa a funcionalidade de consulta de histórico.
        *   Passo 2: Funcionário utiliza critérios de busca (e.g., código de patrimônio) para localizar o exemplar.
    2.  **Sistema exibe histórico de empréstimos do exemplar.**
        *   Passo 1: Sistema recupera e apresenta todos os registros de empréstimo e devolução associados ao exemplar, incluindo usuário, datas de empréstimo e devolução, e estado de conservação no momento da devolução.

#### Use Case: Consultar Histórico de Empréstimos por Usuário
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar o histórico completo de empréstimos e devoluções de um usuário específico.
*   **Eventos:**
    1.  **Funcionário busca usuário para histórico.**
        *   Passo 1: Funcionário acessa a funcionalidade de consulta de histórico.
        *   Passo 2: Funcionário utiliza critérios de busca (e.g., nome, ID) para localizar o usuário.
    2.  **Sistema exibe histórico de empréstimos do usuário.**
        *   Passo 1: Sistema recupera e apresenta todos os registros de empréstimos e devoluções associados ao usuário, incluindo exemplares, datas de empréstimo e devolução.

#### Use Case: Consultar Status do Acervo
*   **Descrição:** Permite ao Funcionário da Biblioteca visualizar informações em tempo real sobre o estado geral do acervo.
*   **Eventos:**
    1.  **Funcionário solicita consulta de status do acervo.**
        *   Passo 1: Funcionário acessa a funcionalidade de painel de controle ou consulta de status do acervo.
    2.  **Sistema exibe informações em tempo real do acervo.**
        *   Passo 1: Sistema apresenta:
            *   Quantos exemplares existem de cada livro.
            *   Quantos exemplares estão disponíveis para empréstimo.
            *   Quantos exemplares estão emprestados.
            *   Quantos exemplares estão em manutenção.
            *   Quais livros estão temporariamente bloqueados para empréstimo devido à quantidade insuficiente de exemplares (5 ou menos).

---

### Casos de Uso para o Ator: Usuário da Biblioteca

#### Use Case: Consultar Acervo Disponível
*   **Descrição:** Permite ao Usuário da Biblioteca pesquisar e visualizar livros e seus exemplares disponíveis para empréstimo.
*   **Eventos:**
    1.  **Usuário solicita consulta do acervo.**
        *   Passo 1: Usuário acessa a interface de consulta do acervo.
    2.  **Sistema exibe livros disponíveis para consulta.**
        *   Passo 1: Sistema apresenta uma lista de livros.
    3.  **Usuário pode pesquisar/filtrar livros.**
        *   Passo 1: Usuário insere termos de busca (e.g., título, autor, categoria).
        *   Passo 2: Sistema filtra e exibe os resultados.
    4.  **Usuário seleciona um livro para ver detalhes.**
        *   Passo 1: Usuário clica em um livro da lista.
    5.  **Sistema exibe detalhes do livro e exemplares disponíveis.**
        *   Passo 1: Sistema mostra informações do livro e lista os exemplares com situação \"disponível para empréstimo\".

#### Use Case: Consultar Meus Empréstimos Ativos
*   **Descrição:** Permite ao Usuário da Biblioteca visualizar os exemplares que ele tem atualmente emprestados.
*   **Eventos:**
    1.  **Usuário solicita consulta de seus empréstimos ativos.**
        *   Passo 1: Usuário acessa a funcionalidade de \"Meus Empréstimos\" (assumindo que ele está autenticado e o sistema sabe quem ele é).
    2.  **Sistema exibe lista de empréstimos ativos do usuário.**
        *   Passo 1: Sistema recupera e apresenta uma lista de todos os empréstimos ativos associados ao usuário, incluindo o exemplar, data de empréstimo e data prevista de devolução.

#### Use Case: Consultar Meu Histórico de Empréstimos
*   **Descrição:** Permite ao Usuário da Biblioteca visualizar todo o seu histórico de empréstimos e devoluções.
*   **Eventos:**
    1.  **Usuário solicita consulta de seu histórico de empréstimos.**
        *   Passo 1: Usuário acessa a funcionalidade de \"Meu Histórico de Empréstimos\".
    2.  **Sistema exibe histórico completo de empréstimos do usuário.**
        *   Passo 1: Sistema recupera e apresenta todos os registros de empréstimos e devoluções (ativos e concluídos) associados ao usuário, incluindo exemplares, datas de empréstimo e devolução efetiva.

---

### Perguntas

*   **Q1: Reserva de Exemplar:** O sistema permite a reserva de exemplares? Se sim, qual ator realiza a reserva (Usuário da Biblioteca ou Funcionário da Biblioteca) e quais são os eventos e passos para realizar e gerenciar uma reserva?
    *   *Justificativa:* A situação \"reservado\" é mencionada para os exemplares, mas não há descrição explícita de uma funcionalidade de reserva ou de como um exemplar entra ou sai desse estado.