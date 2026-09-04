título: 'Aeternvm Vacuvm: Uma estrutura computacional para física de depleção do vácuo, blindagem de Vainshtein e emuladores cosmológicos de MCMC'
tags:

cosmologia
gravidade modificada
Triagem de Vainshtein
MCMC
DESI

Autores da energia escura :
nome: Gustavo Alves Condé
orcid: 0000-0003-0000-0000
afiliação: 1
afiliações:
nome: Pesquisador Independente, Baixo Guandu, ES, Brasil
índice: 1
data: 04 de setembro de 2026
bibliografia: paper.bib
Resumo
Aeternvm Vacuvm é uma estrutura computacional de código aberto projetada para resolver, emular e testar teorias de gravidade modificada, transições de fase do vácuo em tempos tardios e mecanismos de blindagem de Vainshtein em conjuntos de dados cosmológicos de alta precisão (como Planck CMB, DESI Y1/Y3 e Pantheon+ BAO) [@Conde2026]. Os pipelines cosmológicos tradicionais frequentemente carecem de ferramentas unificadas e acessíveis para acoplar a dinâmica escalar-tensorial não linear com inferência Bayesiana rápida. Aeternvm Vacuvm preenche essa lacuna, fornecendo solucionadores numéricos de alta precisão para equações de campo hiperbólicas, juntamente com emuladores de Processos Gaussianos (GP) integrados e pipelines MCMC.

Declaração de Necessidade
Na cosmologia de precisão moderna, testar modelos dinâmicos de energia escura e cenários de depleção do vácuo exige cálculos numéricos complexos, envolvendo a solução simultânea da evolução do fundo, equações de perturbação e efeitos de blindagem local. As bibliotecas de software existentes ou estão restritas ao modelo ΛCDM padrão ou fragmentadas em códigos especializados que são difíceis de integrar com amostradores Bayesianos modernos.

Aeternvm Vacuvm fornece a pesquisadores e cientistas independentes um mecanismo Python autocontido e modular para: 1. Resolver deterministicamente a evolução não linear de campos escalares e a dinâmica de fundo. 2. Avaliar a supressão gravitacional local por meio de mecanismos de blindagem de Vainshtein. 3. Acelerar a inferência de parâmetros cosmológicos usando emuladores de Processos Gaussianos otimizados integrados a frameworks como Cobaya e EFTCAMB.

Arquitetura Matemática e Física
A estrutura é construída sobre fundamentos teóricos rigorosos que ligam o eletromagnetismo de laboratório à aceleração cósmica tardia.

Potencial de depleção de vácuo e acoplamento de impedância
O campo de depleção $$\chi$$ é governado por um potencial da forma:

$$V(\chi) = V_0 \left[1 - \exp\left(-\frac{\lambda \chi}{M_{\rm Pl}}\right)\right]^2$$

Fundamentalmente, a escala de energia $$V_0$$ não é tratada como um parâmetro de ajuste livre. Em vez disso, ela é analiticamente limitada pela impedância do vácuo $$Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 376.73 \Omega$$:

$$V_0 = \frac{h}{2 Z_0 c e_0^2} \left(1 - e^{-S_{\rm inst}}\right)$$

onde $$S_{\rm inst} \approx 280$$ representa uma ação não perturbativa do tipo instanton. Isso resulta em $$V_0 \sim 10^{-47} {\rm GeV}^4$$, que corresponde naturalmente à escala de densidade de energia escura observada sem ajuste fino [@Conde2026].

Equações de Friedmann e de Campo Modificadas
A dinâmica de expansão do meio circundante, incluindo a matéria e o campo de depleção, é governada pelas equações de Friedmann modificadas:

$$H^2 = \frac{8\pi G}{3} \left(\rho_m + \frac{1}{2}\dot{\chi}^2 + V(\chi)\right), \quad \dot{H} = -4\pi G (\rho_m + \dot{\chi}^2)$$

A equação de Klein-Gordon que descreve a evolução de $$\chi$$ é resolvida numericamente por meio de rotinas adaptativas de EDO/EDP de alta precisão (como LSODA e DOP853):

$$\ddot{\chi} + 3H\dot{\chi} + V'(\chi) = 0$$

Projeto e implementação de software
O repositório está organizado em pacotes modulares no seguinte src/diretório:

solver_lsoda.py: Integradores de EDP hiperbólica de alta precisão e EDO de fundo com tolerâncias de erro rigorosas ($$rtol \le 10^{-10}$$).
vainshtein_screening.py: Rotinas para avaliar a supressão gravitacional local dentro do Sistema Solar e em escalas astrofísicas, garantindo a compatibilidade com testes de gravidade local.
mcmc_pipeline.py: Wrappers de inferência Bayesiana otimizados com decomposição de Cholesky e lemas de matriz de Woodbury para avaliações rápidas de verossimilhança.
Controle de qualidade
O AETERNVMVACUVM inclui um conjunto de testes automatizados (pytest) que abrange a triagem de Vainshtein, solvers, transições de fase de depleção do vácuo e consistência do emulador MCMC cosmológico. Os testes incluem verificações de importação, consistência numérica em dados sintéticos e casos extremos. A integração contínua via GitHub Actions executa o conjunto de testes no Python 3.9, 3.10 e 3.11 a cada push e pull request. Conjuntos de dados de exemplo estão incluídos; grandes resultados de simulação estão arquivados no Zenodo (DOI: 10.5281/zenodo.22166663).

Disponibilidade
Código-fonte: https://github.com/gustavosouzaconde40-ai/AETERNVMVACUVM
Licença: MIT
Instalação: pip install -e . ou pip install -e .[test]para desenvolvimento
Versões do Python suportadas: 3.9, 3.10, 3.11
Documentação: Consulte o arquivo README.md e as docstrings.
Versão arquivada (Zenodo): 10.5281/zenodo.22166663 (v1.1.0-complete) - Conceito DOI (todas as versões): 10.5281/zenodo.21856036
Estado atual da área
A inferência de parâmetros cosmológicos para modelos de gravidade modificada e decaimento do vácuo com blindagem geralmente depende de solucionadores de Boltzmann computacionalmente dispendiosos (por exemplo, CLASS, CAMB) e simulações de N-corpos. As ferramentas existentes em Python para blindagem de Vainshtein focam em modelos específicos (por exemplo, hi_class, MG-CAMB), mas carecem de uma estrutura unificada para a física de depleção do vácuo e avaliação rápida da verossimilhança. A amostragem MCMC nesses espaços de alta dimensionalidade permanece proibitiva sem emulação.

O AETERNVM VACUVM preenche essa lacuna ao fornecer uma estrutura computacional que integra (i) modelos analíticos para depleção do vácuo e blindagem de Vainshtein, (ii) um módulo de verossimilhança com correções de $$\mu_{\rm eff}$$ e (iii) emuladores cosmológicos treinados para acelerar o MCMC. Comparado aos emuladores existentes que visam apenas o modelo $$\Lambda$$CDM ou $$w_0w_a$$CDM, este pacote foi projetado para mecanismos de blindagem onde o acoplamento gravitacional efetivo $$\mu_{\rm eff}(k, a)$$ é dependente da escala e do tempo.

Declaração de impacto da pesquisa
O software permite a pesquisa reproduzível em física alternativa da gravidade e do vácuo, áreas relevantes para as análises do DESI, Euclid e LSST. Ao fornecer uma função de verossimilhança testada ( likelihood/probabilidade_mu_eff.py) e uma interface de emulador, ele reduz a barreira para que os cosmólogos testem modelos com blindagem de Vainshtein em relação aos dados sem precisar reimplementar as fórmulas de blindagem. O design modular também serve como ferramenta pedagógica para cursos de pós-graduação em análise de dados cosmológicos.

A adoção inicial inclui o uso nas análises MCMC do autor sobre o esgotamento do vazio, com potencial impacto nas restrições para teorias de gravidade modificadas.

divulgação do uso de IA
Durante a preparação deste trabalho, foram utilizadas ferramentas de IA generativa (GitHub Copilot e ChatGPT) para:

Correção de erros de indentação em Python e erros E999 do flake8
Elaboração de docstrings e código padrão para fluxo de trabalho de CI.github/workflows/python-package.yml
Sugestões para estruturar este artigo de forma a atender aos requisitos do JOSS
Todo o conteúdo científico, as derivações do modelo de depleção de vácuo, a implementação da triagem de Vainshtein e os testes de validação foram elaborados e verificados pelo autor humano. Nenhuma inteligência artificial foi utilizada para gerar resultados ou figuras científicas.

Referências
