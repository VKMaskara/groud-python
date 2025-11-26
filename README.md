# groud-python
                                        -- REPOSITÓRIO ATIVIDADE FINAL (Python) --
-------------------------------------------------------COLABORADORES--------------------------------------------------

Cordenador(s): Vitor Kauê / Glauber
Revisor(s):  Luiz Henrique / Luiz Carlos

Login: Diego

Menu: Edneuza

Designer: Nicolas Breno

Telas (inicio/Fim): Samara

-----# JOGOS #----
Jesse: Jogo do 21
Ana: Termo
Renato: 

-----# CALCULOS #----
Gustavo Santos:
Gustavo Silva: Calculo de Área
Christian: Conversor de Medida
Vinnicios Ribeiro:

-----# ESPORTE #----
Gustavo Valim: Torneio de Skate
Vinicios Oliveira: Quiz do Corinthians
Thiago: IMC
Vinicios de Paula:

-----# FINANCEIRO #----
Arthur Lima:Bolsa de Valores
Maycon: Imposto
Mikaelly:

-----# OUTROS #----
Rodrigo: Rotas de Filmes/Series
Juliana: Verificador de Senha
Kaique: IA de Estudos
Camilly: Playlist 
-----------------------------------------------------------------------------------------------------------------------
                                Critérios Avaliativos Obrigatórios em todos os programas:
-----------------------------------------------------------------------------------------------------------------------
Cores (Iremos utilizar um módulo que está em desenvolvimento, logo será disponibilizado)
Pelo menos uma biblioteca Python
Tratamento de caracteres (Exemolo: Strip(), Upper(), Capitalize())
Condição (If, Else ou While)
Lista, Tupla ou dicionário
Função
                                                  SISTEMA DE NOMENCLATURA      
-----------------------------------------------------------------------------------------------------------------------
## 🔑 Sistema de Nomenclatura Simplificado

Adotaremos o padrão **`snake_case`** para quase tudo, exceto para Classes, que usarão **`PascalCase`** (ou `CapWords`).

### 1. Nomes de Módulos (Códigos) 📂

Para os arquivos (`.py`), utilize nomes curtos, descritivos e em **`snake_case`** (minúsculas com *underscore*).

* **Regra:** `nome_descritivo_em_snake_case`
* **Foco:** O arquivo deve indicar a **funcionalidade** principal.
* **Exemplos:**
    * `dados_iniciais.py` (Em vez de `data_ingestion.py`)
    * `estimativa_estado.py` (Em vez de `state_estimation_model.py`)
    * `filtros.py`
    * `utilitarios_geo.py`

***

### 2. Funções e Métodos ⚙️

Para todas as funções e métodos de classe, utilize **`snake_case`**. Comece o nome com um **verbo de ação** para indicar o que a função faz.

* **Regra:** `verbo_de_acao_em_snake_case()`
* **Foco:** Clareza na **ação** realizada.
* **Exemplos:**
    * `calcular_distancia()`
    * `carregar_configuracao()`
    * `atualizar_vetor_estado()`
    * `processar_leitura_sensor()`

***

### 3. Variáveis e Constantes 🏷️

#### **Variáveis (Valores Mutáveis)**

Use **`snake_case`**. Use nomes completos para evitar dúvidas.

* **Regra:** `nome_completo_em_snake_case`
* **Foco:** O que o valor **representa**.
* **Exemplos:**
    * `tempo_atual` (Em vez de `t` ou `current_time`)
    * `dados_brutos`
    * `indice_medicao`
    * `eh_valido` (Para booleanos: prefixo `eh_`)

#### **Constantes (Valores Fixos e Globais)**

Use **`ALL_CAPS_WITH_UNDERSCORES`** (todas as letras maiúsculas com *underscore*).

* **Regra:** `MAIUSCULAS_COM_UNDERSCORE`
* **Foco:** Devem ser valores que **NÃO** mudam durante a execução do programa.
* **Exemplos:**
    * `TAXA_MAXIMA_ERRO`
    * `VALOR_DEFAULT`
    * `LIMITE_ITERACAO`

***

### 📝 Resumo Rápido para Distribuição

| Componente           |       Regra Simplificada                          |         Exemplo        |
| :---                 | :---                                              | :---                   |
| **Códigos (.py)**    | `snake_case` (minúsculas)                         | `calculo_principal.py` |
| **Classes**          | `PascalCase` (Primeira Letra Maiúscula)           | `AlgoritmoGerenciador` |
| **Funções/Métodos**  | `snake_case` (verbo de ação)                      | `validar_dados()`      |
| **Variáveis**        | `snake_case` (descritivo)                         | `vetor_entrada`        |
| **Constantes**       | `ALL_CAPS` (maiúsculas)                           | `VALOR_PI`             |
