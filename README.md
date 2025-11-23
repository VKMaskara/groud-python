# groud-python
                                        -- REPOSITÓRIO ATIVIDADE FINAL (Python) --
-------------------------------------------------------COLABORADORES--------------------------------------------------

Cordenador(s): Vitor Kauê / Glauber
Revisor(s):  Luiz Henrique / Luiz Carlos
Login: Diego
Menu: Edneusa
Designer: Bruno
Telas (inicio/Fim): Samara

-----# JOGOS #----
Jesse: Jogo do 21
Ana: 

-----# CALCULOS #----
Gustavo Santos:
Christian:

-----# ESPORTE #----
Gustavo:
Vinicios:

-----# FINANCEIRO #----
Arthur Lima:
Maycon: Imposto

-----# OUTROS #----
Rodrigo: Rotas de Filmes/Series
Juliana:
Kaique: IA de Estudos
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
