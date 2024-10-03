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
| Ridge Regression           | 0.761 | 14,548,515,721.72   | 95,959.10             | 0.227  | 0.077 |
| Polynomial Regression      | 0.766 | 14,246,342,540.56   | 92,722.98             | 0.214  | 0.059 |
| Multi Linear Regression    | 0.766 | 14,267,190,898.42   | 92,872.71             | 0.214  | 0.060 |
| Decision Tree              | 0.732 | 16,372,773,983.58   | 90,171.15             | 0.224  | 0.061 |
| CatBoost Regressor         | 0.861 | 8,471,992,036.09    | 67,306.37             | 0.160  | 0.042 |
| XGBoost Regressor          | 0.847 | 9,529,034,273.81    | 73,203.43             | 0.183  | 0.071 |


### Com Amenities

| Modelo                    | R²   | MSE                 | MAE                   | MAPE   | RMSPE |
|---------------------------|------|---------------------|-----------------------|--------|-------|
| Ridge Regression           | 0.789 | 12,884,054,099.78   | 87,069.25             | 0.199  | 0.052 |
| Polynomial Regression      | 0.789 | 12,884,054,099.78   | 87,069.25             | 0.199  | 0.052 |
| Multi Linear Regression    | 0.786 | 13,069,612,291.80   | 87,649.85             | 0.200  | 0.052 |
| Decision Tree              | 0.592 | 24,967,098,916.85   | 107,187.45            | 0.248  | 0.055 |
| CatBoost Regressor         | 0.866 | 8,205,694,862.16    | 63,408.75             | 0.145  | 0.037 |
| XGBoost Regressor          | 0.847 | 9,529,034,273.81    | 73,203.43             | 0.183  | 0.071 |

## Visualização dos Resultados

Em construção

### Análise dos Resultados

Com base nos resultados apresentados:

- **Melhor Desempenho Geral:**
  - **Com Amenities:** O **CatBoost Regressor** apresenta o melhor desempenho geral com o maior \( R^2 \) (0.866), o menor MAE (63,408.75), MAPE (0.145) e RMSPE (0.037), indicando que o modelo otimizado com amenities é mais preciso e explica melhor a variabilidade dos dados.
  - **Sem Amenities:** O **CatBoost Regressor** também se destaca, com o maior \( R^2 \) (0.861), além de apresentar os menores valores de MAE (67,306.37), MAPE (0.160) e RMSPE (0.042).

- **Modelos com Pior Desempenho:**
  - **Sem Amenities:** O **Decision Tree** tem o pior desempenho com o menor \( R^2 \) (0.732), além de apresentar MAE e MAPE relativamente altos, sugerindo que é menos eficaz.
  - **Com Amenities:** O **Decision Tree** continua a ter o pior desempenho, com o menor \( R^2 \) (0.592) e os maiores valores de MAE (107,187.45) e MAPE (0.248), apesar da inclusão de amenities.

Esses resultados sugerem que a inclusão de amenities melhora o desempenho dos modelos, principalmente em termos de MAE, MAPE e RMSPE, além de reduzir a variabilidade dos erros nos modelos mais avançados.

---

## Conclusão

Baseado nas métricas de erro (MAE, MAPE e RMSPE), o modelo que apresentou os melhores resultados foi o **CatBoost Regressor** tanto com quanto sem amenities. Esse modelo teve o menor MAE, MAPE e RMSPE em ambas as configurações, confirmando sua superioridade na precisão das predições.

Entre os modelos com amenities, o **CatBoost Regressor** é o mais eficaz, com o menor erro absoluto e percentual, sugerindo que é o mais adequado para capturar a relação entre as variáveis preditoras e o target. Para os modelos sem amenities, o **CatBoost Regressor** também supera os demais.

## Próximos Passos

- **Refinamento dos Modelos:**
  - Explorar ajustes adicionais nos hiperparâmetros do **CatBoost** e do **XGBoost** para potencialmente melhorar ainda mais o desempenho.
  - Investigar técnicas de regularização em modelos lineares para evitar overfitting em datasets maiores.

- **Exploração de Modelos Alternativos:**
  - Testar redes neurais, que podem ser particularmente eficazes ao capturar interações complexas entre as variáveis.
  
- **Tratamento de Outliers:**
  - Melhorar a identificação e remoção de outliers, que podem estar influenciando os resultados dos modelos de regressão.

- **Análise dos Atributos:**
  - Avaliar mais profundamente o impacto de diferentes amenities sobre o modelo, possivelmente através de feature importance ou SHAP values, para identificar quais características têm maior influência nas predições.
## Contato

Para mais informações, entre em contato: shibukawa@alunos.utfpr.edu.br
