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
git clone https://github.com/seu_usuario/nome_projeto.git
cd nome_projeto
```
### Execute o notebook principal main.ipynb:

```bash
jupyter notebook main.ipynb
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

## Resultados dos Modelos

### Sem Amenities

| Modelo               | Melhor R² Score | R² Score do Modelo Otimizado | MSE                 | MAE do Modelo Otimizado | MAPE | RMSPE |
|----------------------|-----------------|------------------------------|---------------------|-------------------------|------|-------|
| Ridge Regression     | 0.792           | 0.780                        | 12,669,986,389.93   | 86,608.95               | 0.211| 0.091 |
| Polynomial Regression| 0.806           | 0.800                        | 11,536,512,920.42   | 81,908.46               | 0.202| 0.086 |
| Multi Linear Regression | 0.792        | 0.780                        | 12,670,333,734.46   | 86,607.93               | 0.211| 0.091 |
| Decision Tree        | 0.721           | 0.623                        | 21,720,147,637.76   | 104,144.21              | 0.253| 0.070 |
| CatBoost Regressor   | 0.853           | 0.841                        | 9,186,180,086.49    | 71,517.73               | 0.175| 0.069 |
| XGBoost Regressor    | 0.847           | 0.835                        | 9,529,034,273.81    | 73,203.43               | 0.183| 0.071 |

### Com Amenities

| Modelo               | Melhor R² Score | R² Score do Modelo Otimizado | MSE                 | MAE do Modelo Otimizado | MAPE | RMSPE |
|----------------------|-----------------|------------------------------|---------------------|-------------------------|------|-------|
| Polynomial Regression| 0.856           | 0.872                        | 7,426,317,142.71    | 64,388.44               | 0.162| 0.039 |
| Multi Linear Regression | 0.860        | 0.874                        | 7,327,966,323.42    | 64,058.30               | 0.161| 0.043 |
| Decision Tree        | 0.617           | 0.616                        | 22,341,980,635.17   | 95,334.10               | 0.250| 0.124 |

## Visualização dos Resultados

Aqui está um gráfico de distribuição entre os valores reais e previstos usando o modelo CatBoost Regressor:

![Gráfico de Distribuição](URL_DO_GRÁFICO)

## Conclusão

O modelo que apresentou os melhores resultados foi o Polynomial Regression com amenities, com um R² de 0.872 e MAPE de 0.162.

## Próximos Passos
- Testar mais técnicas de regularização para evitar overfitting.
- Explorar redes neurais para realizar a predição.
- Melhorar a manipulação de outliers no conjunto de dados.

## Contato

Para mais informações, entre em contato: seu-email@dominio.com


## Próximos Passos
- Testar mais técnicas de regularização para evitar overfitting.
- Explorar redes neurais para realizar a predição.
- Melhorar a manipulação de outliers no conjunto de dados.

## Contato

Para mais informações, entre em contato: seu-email@dominio.com

