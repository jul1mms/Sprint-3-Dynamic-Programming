# Projeto de Treinamento em Realidade Virtual para Médicos

## Introdução
Este projeto visa desenvolver uma plataforma de treinamento em realidade virtual (VR) para médicos, com foco na prática de laparoscopia. A proposta é criar um ambiente simulado que permite aos profissionais realizar procedimentos de forma segura, aprimorando suas habilidades e a precisão cirúrgica. Para isso, foi realizada uma simulação do histórico de cirurgias performadas por um jogador. O objetivo foi analisar o tempo de resposta ao carregar dados armazenados em diferentes formatos: JSON, CSV e SQLite.

O jogador deve consultar seu histórico, visualizar seu progresso e revisitar notas de procedimentos realizados, tornando a eficiência no carregamento de dados crucial para a experiência do usuário. Essa simulação se mostra útil para o projeto final, permitindo entender como diferentes métodos de armazenamento afetam a performance e a interatividade do jogo.

## Metodologia
Através de medições de tempo precisas, utilizando a função `time.perf_counter()`, avaliamos o desempenho de cada abordagem de armazenamento. Os resultados obtidos revelaram os seguintes tempos de carregamento:
- **Tempo de carregamento dos dados JSON:** 0.0000476000 segundos.
- **Tempo de carregamento dos dados CSV:** 0.0000308000 segundos.
- **Tempo de carregamento dos dados SQLite:** 0.0000321000 segundos.

Embora os dados utilizados para os testes não estivessem muito populados, os resultados ainda são representativos e se aplicam a cenários mais amplos, onde a estrutura e a eficiência dos métodos de armazenamento podem impactar o desempenho geral do sistema.

## Vantagens e Desvantagens dos Métodos

1. **JSON**
   - **Vantagens:** Estrutura intuitiva e legível, fácil de manipular em JavaScript e outras linguagens. Ideal para dados hierárquicos.
   - **Desvantagens:** Pode ser mais lento para carregar grandes volumes de dados devido à sua complexidade estrutural.

2. **CSV**
   - **Vantagens:** Estrutura simples, de fácil leitura e escrita. Tempos de carregamento rápidos para dados tabulares, como estatísticas de jogos.
   - **Desvantagens:** Não suporta hierarquia de dados, tornando-o inadequado para estruturas mais complexas.

3. **SQLite**
   - **Vantagens:** Capaz de gerenciar grandes volumes de dados de forma eficiente. Suporta consultas complexas, permitindo manipulação avançada. Garante integridade e consistência através de transações, o que é crucial em aplicações que exigem precisão. Além disso, sua escalabilidade permite que o desempenho se mantenha sólido à medida que o volume de dados cresce.
   - **Desvantagens:** Pode ser mais lento que formatos mais simples em operações de leitura, especialmente com dados pequenos, devido à sobrecarga do gerenciamento do banco de dados.

## Resultados e Análise
Os dados em formato CSV apresentaram o melhor desempenho, seguidos pelo SQLite e, por último, o JSON. O CSV, ao utilizar uma estrutura de dados mais simples e diretamente acessível, mostrou-se ligeiramente mais rápido, sendo benéfico em situações que exigem carregamentos frequentes e rápidos. Portanto, o CSV se mostra uma escolha ideal para cenários com dados menos complexos.

Por outro lado, se o projeto final envolver um grande volume de dados, o SQLite se torna a opção mais adequada, oferecendo escalabilidade, integridade dos dados e a capacidade de realizar consultas complexas que tornam a manipulação de grandes conjuntos de informações mais eficiente.

## Considerações Finais
Este estudo é fundamental para orientar futuras decisões de design em jogos, onde a eficiência no carregamento de dados impacta diretamente a experiência do usuário. A medição precisa dos tempos de resposta destacou a importância de considerar não apenas a simplicidade de implementação, mas também a performance dos métodos de armazenamento, especialmente em projetos que lidam com grandes volumes de dados e necessitam de respostas ágeis.

Em suma, o projeto não só contribuiu para a compreensão do impacto dos diferentes formatos de dados na performance de aplicativos, mas também proporcionou uma experiência prática valiosa em técnicas de análise de dados e otimização de sistemas. As conclusões tiradas aqui servirão como base para futuras otimizações, sempre visando aprimorar a interação do jogador com o jogo.

## Requisitos
- Python 3.x
- pandas

## Instruções
- Executar `main.py`

## Autores
- Júlia Masson (RM 98134)
- Julia Ortiz (RM 550204)
- Julia Palomari (RM 551910)
- Juliana Maita (RM 99224)
- Letícia Baptista (RM 550289)
