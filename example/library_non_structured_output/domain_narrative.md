## Domain Narrative
### 1. Contexto do Sistema
O sistema tem como objetivo gerenciar o funcionamento de uma biblioteca, controlando o acervo (livros e seus exemplares físicos), os usuários da biblioteca, e os processos de empréstimo e devolução de exemplares. Ele visa otimizar a gestão do inventário de livros, garantir a conformidade com as regras de negócio da biblioteca e fornecer informações em tempo real sobre a disponibilidade do acervo e o histórico de uso para fins de auditoria e acompanhamento.
### 2. Usuários do Sistema
*   **Usuários (Membros/Leitores):** Pessoas cadastradas na biblioteca que realizam empréstimos e devoluções de exemplares.
*   **Funcionários da Biblioteca:** Responsáveis por gerenciar o acervo (cadastro de livros e exemplares), cadastrar e gerenciar usuários, registrar empréstimos e devoluções, atualizar o estado de conservação e a situação dos exemplares, e realizar consultas sobre o uso do acervo.
### 3. Funcionalidades do Sistema
*   **Gestão de Livros:**
    *   Manter um catálogo de livros, incluindo informações cadastrais como título, autor, editora, edição, ISBN, categoria e ano de publicação.
    *   Permitir que um mesmo livro possua múltiplos exemplares físicos associados.
*   **Gestão de Exemplares:**
    *   Cadastrar exemplares físicos, registrando informações como código de patrimônio, estado de conservação, localização na biblioteca e situação atual.
    *   Registrar e atualizar o estado de conservação do exemplar (e.g., novo, bom, regular, danificado, inutilizável).
    *   Gerenciar a situação do exemplar, que pode ser: disponível para empréstimo, emprestado, reservado, em manutenção, ou indisponível.
    *   Permitir a reavaliação do estado de conservação de um exemplar no momento da devolução.
    
*   **Gestão de Empréstimos:**
    *   Registrar empréstimos, associando o usuário responsável, o exemplar emprestado, a data do empréstimo, a data prevista de devolução, a data efetiva de devolução e a situação do empréstimo.
    *   Atualizar a situação do exemplar para \"emprestado\" e considerá-lo indisponível para novos empréstimos enquanto o empréstimo estiver ativo.
    *   Aplicar regras de negócio para autorização de empréstimos:
        *   Impedir empréstimos de livros que possuam 5 exemplares ou menos no acervo total.
        *   Autorizar empréstimos somente quando a quantidade total de exemplares do livro for superior a 5.
        *   Manter um histórico detalhado de todos os empréstimos.

*   **Gestão de Devoluções:**
    *   Registrar a devolução de exemplares.
    *   Atualizar automaticamente a situação do exemplar para \"disponível\" após a devolução, desde que ele não esteja reservado ou em manutenção.
    *   Permitir a reavaliação e atualização do estado de conservação do exemplar no momento da devolução.
    *   Manter um histórico detalhado de todas as devoluções.
    
*   **Consultas e Informações em Tempo Real:**
    *   Consultar quais exemplares estão atualmente emprestados.
    *   Consultar quais usuários possuem empréstimos ativos.
    *   Consultar as datas previstas de devolução.
    *   Consultar os exemplares disponíveis para empréstimo.
    *   Consultar o histórico de empréstimos de um exemplar específico.
    *   Consultar o histórico de empréstimos de um usuário específico.
    *   Informar em tempo real:
        *   A quantidade total de exemplares de cada livro.
        *   A quantidade de exemplares disponíveis para empréstimo.
        *   A quantidade de exemplares emprestados.
        *   A quantidade de exemplares em manutenção.
        *   Quais livros estão temporariamente bloqueados para empréstimo devido à quantidade insuficiente de exemplares (5 ou menos).

*   **Regras de Negócio e Validações:**
    *   Garantir que cada livro possua, no mínimo, 5 exemplares cadastrados no acervo.
    *   Impedir a realização de empréstimos que violem a regra da quantidade mínima de exemplares disponíveis por livro.

*   **Auditoria:**
    *   Manter registros históricos de empréstimos e devoluções para fins de auditoria e acompanhamento do uso do acervo.

### 4. Perguntas
Nenhuma pergunta foi identificada, pois todas as informações necessárias para a criação desta versão do Domain Narrative foram extraídas do texto fornecido.