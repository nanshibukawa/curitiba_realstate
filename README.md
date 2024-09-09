# Projeto de Predição de Preços de Apartamentos de Curitiba

Este projeto foi desenvolvido para prever os preços de apartamentos na cidade de Curitiba, utilizando diferentes algoritmos de regressão e técnicas de seleção de features. O conjunto de dados utilizado foi extraído do [Kaggle](https://www.kaggle.com/datasets/wittmannf/curitiba-apartment-prices).

## Objetivo

O objetivo principal deste projeto é construir um modelo preditivo que possa estimar o preço dos apartamentos com base em diversas variáveis, como localização, número de quartos, área total, entre outras, com ou sem a inclusão de *amenities* (características adicionais).

## Modelos Utilizados

Testamos diversos modelos de regressão e ajustamos seus hiperparâmetros com `RandomizedSearchCV`. Aqui estão os modelos testados:

1. **Regressão Linear Simples**
2. **Regressão Polinomial**
3. **Ridge Regression**
4. **Árvore de Decisão**
5. **CatBoost Regressor**
6. **XGBoost Regressor**

## Estrutura do Projeto

O pipeline segue as seguintes etapas:

1. **Carregamento e Pré-processamento dos Dados:**
   - Remoção de valores nulos e tratamento de outliers.
   - Normalização/Padronização de features.
   
2. **Seleção de Features:**
   - Utilizamos `SmartCorrelatedSelection` para eliminar features altamente correlacionadas, evitando multicolinearidade.
   
3. **Criação dos Pipelines:**
   - Cada modelo foi inserido dentro de um pipeline que inclui a seleção de features e o ajuste dos hiperparâmetros.

4. **Validação e Avaliação:**
   - A validação foi feita com `RandomizedSearchCV` utilizando a métrica `r2_score`.
   - Métricas calculadas: R², MAE, MSE, MAPE, RMSPE.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.7+
- Instalar os pacotes listados no `requirements.txt`:

```bash
pip install -r requirements.txt
```
## Rodando o Projeto

Após instalar os pacotes, você pode rodar os notebooks para executar a análise e treinar os modelos.

### Clone o repositório:

```bash
git clone https://github.com/nanshibukawa/curitiba_realstate
cd curitiba_realstate
```
### Execute o notebook principal main.ipynb:

```bash
jupyter notebook real_state_curitiba_regression.ipynb.ipynb
```

# Análise de Preços de Apartamentos em Curitiba

O dataset foi obtido do Kaggle e contém informações de preços de apartamentos em Curitiba. Para mais informações, visite a [Kaggle Dataset Page](https://www.kaggle.com/datasets/wittmannf/curitiba-apartment-prices).

## Variáveis Principais
- **price (target)**: Preço do apartamento.
- **area**: Área total do apartamento.
- **rooms**: Número de quartos.
- **bathrooms**: Número de banheiros.
- **garages**: Número de vagas de garagem.
- **neighborhood**: Bairro onde o apartamento está localizado.
- **amenities**: Diferentes amenities como academia, piscina, entre outros (quando incluídos).

## Avaliação de Desempenho do Modelo

Para avaliar o desempenho dos modelos de regressão, utilizamos diversas métricas. Cada métrica fornece uma perspectiva diferente sobre a precisão e a eficácia do modelo. A seguir, detalhamos as principais métricas usadas e como interpretá-las.

## Avaliação de Desempenho do Modelo

Para avaliar o desempenho dos modelos de regressão, utilizamos diversas métricas. Cada métrica fornece uma perspectiva diferente sobre a precisão e a eficácia do modelo. A seguir, detalhamos as principais métricas usadas e como interpretá-las.

### Métricas de Avaliação

#### 1. Mean Absolute Error (MAE)

- **Definição:** A média das diferenças absolutas entre os valores previstos e os valores reais.
- **Fórmula:** 
  ![MAE](https://mariofilho.com/img/mae/0.png)
- **Interpretação:** O MAE fornece a magnitude média dos erros em unidades da variável dependente. Valores menores indicam melhor desempenho, com menos discrepância média entre previsões e valores reais.

#### 2. Mean Squared Error (MSE)

- **Definição:** A média dos quadrados das diferenças entre os valores previstos e os valores reais.
- **Fórmula:** 
  ![MSE](url-da-imagem-da-fórmula-MSE)
- **Interpretação:** O MSE penaliza erros maiores mais severamente devido ao quadrado das diferenças. Menores valores indicam um melhor ajuste do modelo. O MSE é sensível a outliers.

#### 3. Mean Absolute Percentage Error (MAPE)

- **Definição:** A média dos erros absolutos expressos como uma porcentagem dos valores reais.
- **Fórmula:** 
  ![MAPE](url-da-imagem-da-fórmula-MAPE)
- **Interpretação:** O MAPE fornece uma visão percentual do erro, útil para comparar a precisão entre diferentes escalas de dados. Menor MAPE indica melhor precisão.

#### 4. Root Mean Squared Percentage Error (RMSPE)

- **Definição:** A raiz quadrada da média dos quadrados dos erros percentuais.
- **Fórmula:** 
  ![RMSPE](url-da-imagem-da-fórmula-RMSPE)
- **Interpretação:** Penaliza mais os erros percentuais grandes, útil quando os erros percentuais são mais relevantes.

#### 5. Coeficiente de Determinação (R²)

- **Definição:** A proporção da variância nos valores dependentes que é explicada pelo modelo.
- **Fórmula:** 
  ![R²](url-da-imagem-da-fórmula-R2)
- **Interpretação:** Variando de 0 a 1, valores mais próximos de 1 indicam que o modelo explica bem a variabilidade dos dados. Valores negativos podem ocorrer se o modelo é muito ruim em comparação com uma linha de base simples.



## Resultados dos Modelos

### Sem Amenities

| Modelo                    | R²   | MSE                 | MAE                   | MAPE   | RMSPE |
|---------------------------|------|---------------------|-----------------------|--------|-------|
| Ridge Regression          | 0.792 | 12,669,986,389.93   | 86,608.95             | 0.211  | 0.091 |
| Polynomial Regression     | 0.806 | 11,536,512,920.42   | 81,908.46             | 0.202  | 0.086 |
| Multi Linear Regression   | 0.792 | 12,670,333,734.46   | 86,607.93             | 0.211  | 0.091 |
| Decision Tree             | 0.721 | 21,720,147,637.76   | 104,144.21            | 0.253  | 0.070 |
| CatBoost Regressor        | 0.853 | 9,186,180,086.49    | 71,517.73             | 0.175  | 0.069 |
| XGBoost Regressor         | 0.847 | 9,529,034,273.81    | 73,203.43             | 0.183  | 0.071 |

### Com Amenities

| Modelo                    | R²   | MSE                 | MAE                   | MAPE   | RMSPE |
|---------------------------|------|---------------------|-----------------------|--------|-------|
| Polynomial Regression     | 0.856 | 7,426,317,142.71    | 64,388.44             | 0.162  | 0.039 |
| Multi Linear Regression   | 0.860 | 7,327,966,323.42    | 64,058.30             | 0.161  | 0.043 |
| Decision Tree             | 0.617 | 22,341,980,635.17   | 95,334.10             | 0.250  | 0.124 |

## Visualização dos Resultados

Em construção

### Análise dos Resultados

Com base nos resultados apresentados:

- **Melhor Desempenho Geral:**
  - **Com Amenities:** A **Multi Linear Regression** apresenta o melhor desempenho geral com o maior \( R^2 \) e os menores valores de MAE, MAPE e RMSPE, indicando que o modelo ajustado com amenities é mais preciso e explica melhor a variabilidade dos dados.
  - **Sem Amenities:** O **CatBoost Regressor** mostra o melhor desempenho, com o maior \( R^2 \) e os menores MAE e RMSPE.

- **Modelos com Pior Desempenho:**
  - **Sem Amenities:** O **Decision Tree** tem o menor \( R^2 \) e os maiores valores de MAE e MAPE, indicando que este modelo é menos eficaz comparado aos outros.
  - **Com Amenities:** O **Decision Tree** continua a ter o menor \( R^2 \), mas a inclusão de amenities melhorou o desempenho geral em comparação com o modelo sem amenities.

Esses resultados sugerem que a inclusão de amenities melhora o desempenho dos modelos, especialmente em termos de \( R^2 \) e erros percentuais.




## Conclusão

Baseado nas métricas de erro (MSE, MAPE e RMSPE), o modelo que apresentou os melhores resultados foi o **Polynomial Regression com amenities**, com o menor MSE, MAPE e RMSPE. O **CatBoost Regressor** também se destacou entre os modelos sem amenities, especialmente pela sua performance superior em termos de MSE e MAPE.

## Próximos Passos
- Testar mais técnicas de regularização para evitar overfitting.
- Explorar redes neurais para realizar a predição.
- Melhorar a manipulação de outliers no conjunto de dados.

## Contato

Para mais informações, entre em contato: shibukawa@alunos.utfpr.edu.br

## Próximos Passos
- Testar mais técnicas de regularização para evitar overfitting.
- Explorar redes neurais para realizar a predição.
- Melhorar a manipulação de outliers no conjunto de dados.

## Contato

Para mais informações, entre em contato: seu-email@dominio.com

