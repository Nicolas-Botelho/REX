from langgraph.graph import START, END, StateGraph

from ai_gen.state import State
from ai_gen.agents.class_agent import call_llm as call_class
from ai_gen.agents.usecase_agent import call_llm as call_usecase

# Full Workflow and Graph
full_workflow = StateGraph(State)

full_workflow.add_node("uc_node", call_usecase)
full_workflow.add_node("cls_node", call_class)

full_workflow.add_edge(START, "uc_node")
full_workflow.add_edge("uc_node", "cls_node")
full_workflow.add_edge("cls_node", END)

full_graph = full_workflow.compile()

# Usecase Workflow and Graph
usecase_workflow = StateGraph(State)

usecase_workflow.add_node("uc_node", call_usecase)

usecase_workflow.add_edge(START, "uc_node")
usecase_workflow.add_edge("uc_node", END)

usecase_graph = usecase_workflow.compile()

# Class Workflow and Graph
class_workflow = StateGraph(State)

class_workflow.add_node("cls_node", call_class)

class_workflow.add_edge(START, "cls_node")
class_workflow.add_edge("cls_node", END)

class_graph = class_workflow.compile()

# print(full_graph.invoke({"InputText": """
# O sistema a ser desenvolvido tem como objetivo central integrar, automatizar e otimizar processos internos de uma organização que atualmente dependem de controles manuais e ferramentas desconectadas. A proposta consiste na criação de uma plataforma web responsiva, acessível em diferentes dispositivos, capaz de centralizar informações estratégicas, operacionais e gerenciais em um único ambiente seguro e intuitivo. Esse sistema deverá atender às necessidades de diferentes perfis de usuários, com níveis de permissão bem definidos, garantindo que cada colaborador visualize e manipule apenas os dados pertinentes às suas responsabilidades.

# A arquitetura do sistema será baseada em uma estrutura moderna, com separação clara entre front-end e back-end, permitindo escalabilidade e manutenção facilitada. O back-end será responsável pelo processamento das regras de negócio, integração com banco de dados relacional e possíveis integrações externas por meio de APIs. Já o front-end será desenvolvido com foco na experiência do usuário, priorizando navegação simples, clareza visual e eficiência na execução das tarefas. A segurança será um dos pilares do projeto, contemplando autenticação robusta, criptografia de dados sensíveis e registros de auditoria para rastreamento de ações críticas realizadas na plataforma.

# Entre as principais funcionalidades previstas estão o cadastro e gerenciamento de usuários, controle de processos internos, acompanhamento de solicitações, geração de relatórios personalizados e painéis gerenciais com indicadores de desempenho em tempo real. O sistema também permitirá a configuração de fluxos de trabalho automatizados, reduzindo retrabalho e minimizando falhas humanas. Notificações automáticas por e-mail ou dentro da própria plataforma manterão os usuários informados sobre prazos, pendências e atualizações relevantes, promovendo maior transparência e agilidade na comunicação interna.

# Outro aspecto essencial será a possibilidade de parametrização, permitindo que administradores ajustem regras, categorias e permissões conforme a evolução das demandas organizacionais. Dessa forma, o sistema não será uma solução rígida, mas sim uma ferramenta adaptável ao crescimento e às mudanças estratégicas da instituição. Além disso, o projeto considerará boas práticas de usabilidade e acessibilidade, garantindo que diferentes perfis de usuários consigam utilizar a plataforma de forma eficiente, independentemente de seu nível de familiaridade com tecnologia.

# O desenvolvimento seguirá metodologia ágil, com entregas incrementais que possibilitem validações constantes junto aos stakeholders. Essa abordagem permitirá ajustes rápidos e maior alinhamento entre as expectativas da organização e as funcionalidades implementadas. Também serão realizados testes rigorosos, incluindo testes funcionais, de desempenho e de segurança, assegurando que o sistema seja estável, confiável e preparado para operar em ambiente produtivo.

# Ao final, espera-se que o sistema proporcione ganhos significativos em produtividade, redução de custos operacionais e melhoria na qualidade das informações disponíveis para tomada de decisão. A centralização de dados e a automação de processos contribuirão para maior controle, rastreabilidade e eficiência organizacional, consolidando a tecnologia como um recurso estratégico para o crescimento sustentável da instituição.
# """}))