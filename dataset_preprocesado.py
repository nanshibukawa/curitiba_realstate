import pandas as pd
import numpy as np
import re
import plotly.express as px

# Load Data
df1 = pd.read_csv(r"curitiba_apartment_real_estate_data.csv")

# Data Cleaning: Dropping Unnecessary Features
df_without_features = df1.drop(['description', 'title', 'zipCode', 'lon', 'lat', 'street', 'poisList', 'yearlyIptu'], axis='columns')

# Data Cleaning: Handle 'usableAreas' NaN Values and Outliers
df_usable_areas = df_without_features.copy()
min_value_usableAreas = df_usable_areas.usableAreas.min()
q1_usableAreas, q3_usableAreas = np.percentile(df_usable_areas.usableAreas, [25, 75])
iqr_usableAreas = q3_usableAreas - q1_usableAreas
upper_boundry_usableAreas = q3_usableAreas + 1.5 * iqr_usableAreas

print(f'Usable Areas: Min {min_value_usableAreas}, Q1 {q1_usableAreas}, Q3 {q3_usableAreas}, Upper Boundary {upper_boundry_usableAreas}')

df_usable_areas = df_usable_areas[(df_usable_areas['usableAreas'] <= upper_boundry_usableAreas) & 
                                   (df_usable_areas['usableAreas'] > 15)]
df_usable_areas = df_usable_areas[df_usable_areas['usableAreas'] < 235]

print(f'Rows after filtering usableAreas: {df_usable_areas.shape[0]}')

# Data Cleaning: Handle 'totalAreas' NaN Values and Outliers
df_total_areas = df_usable_areas.copy()
df_total_areas.dropna(subset=['totalAreas'], inplace=True)

q1_totalAreas, q3_totalAreas = np.percentile(df_total_areas.totalAreas, [25, 75])
iqr_totalAreas = q3_totalAreas - q1_totalAreas
upper_boundry_totalAreas = q3_totalAreas + 1.5 * iqr_totalAreas

df_total_areas = df_total_areas[(df_total_areas['totalAreas'] <= upper_boundry_totalAreas) & 
                                 (df_total_areas['totalAreas'] >= df_total_areas['usableAreas'])]
df_total_areas = df_total_areas[df_total_areas['totalAreas'] < 327]

print(f'Rows after filtering totalAreas: {df_total_areas.shape[0]}')

# Data Cleaning: Handle NA Values in 'suites'
df_suites = df_total_areas.copy()
df_suites['suites'] = df_suites['suites'].fillna(df_suites.apply(lambda row: 1 if row['bathrooms'] > 1 else 0, axis=1))

# Data Cleaning: Handle NA Values and Outliers in 'bedrooms'
df_bedrooms = df_suites.copy()
df_bedrooms = df_bedrooms[df_bedrooms['bedrooms'] < 5]

print(f'Rows after filtering bedrooms: {df_bedrooms.shape[0]}')

# Data Cleaning: Handle 'neighborhood' Outliers
df2 = df_bedrooms.copy()
neighborhood_percent = df2['neighborhood'].value_counts(normalize=True) * 100
neighborhood_percent_less_than_2 = neighborhood_percent[neighborhood_percent < 2]
df2['neighborhood'] = df2['neighborhood'].apply(lambda x: 'outros' if x in neighborhood_percent_less_than_2 else x)

# Data Cleaning: Handle 'monthlyCondoFee' Outliers and NA Values
df3 = df2.copy()
df_fillna_bigger_10 = df3[df3['monthlyCondoFee'] >= 50]
q1, q3 = np.percentile(df_fillna_bigger_10['monthlyCondoFee'], [25, 75])
iqr = q3 - q1
upper_boundry = q3 + 1.5 * iqr

mean_values = df_fillna_bigger_10.groupby('neighborhood')['monthlyCondoFee'].mean()
df3['monthlyCondoFee'] = df3.apply(
    lambda row: mean_values[row['neighborhood']] if row['monthlyCondoFee'] < 50 or row['monthlyCondoFee'] >= upper_boundry or pd.isna(row['monthlyCondoFee']) else row['monthlyCondoFee'],
    axis=1
)
df3 = df3[df3['monthlyCondoFee'] < 1167]

print(f'Rows after filtering monthlyCondoFee: {df3.shape[0]}')

# Data Cleaning: Handle 'parkingSpaces' NaN Values
df_parking_spaces = df3.copy()
df_parking_spaces['parkingSpaces'] = df_parking_spaces['parkingSpaces'].fillna(df_parking_spaces.apply(
    lambda row: 1 if row['totalAreas'] > row['usableAreas'] else 0,
    axis=1
))
df_parking_spaces = df_parking_spaces[df_parking_spaces['parkingSpaces'] <= 6]

print(f'Rows after filtering parkingSpaces: {df_parking_spaces.shape[0]}')

# Data Cleaning: Process 'amenities' Column
df_amenities = df_parking_spaces.copy()

def clean_amenity(amenity):
    amenity = re.sub(r"[^\w\s]", "", amenity)
    amenity = re.sub(r"\d+_", "", amenity)
    amenity = amenity.strip()
    amenity = re.sub(r"^0_|^''$|^$", "", amenity)
    amenity = re.sub(r".*pool.*", "pool", amenity, flags=re.IGNORECASE)
    amenity = re.sub(r".*kitchen.*", "kitchen", amenity, flags=re.IGNORECASE)
    return amenity if amenity else ""

df_amenities['amenities'] = df_amenities['amenities'].apply(clean_amenity)

print("Valores únicos na coluna 'amenities' após a limpeza:")
print(df_amenities['amenities'].unique())

# Criar dummies para a coluna 'amenities'
amenities_dummies = pd.get_dummies(df_amenities['amenities'].str.split(expand=True))
amenities_dummies.columns = [re.sub(r"^\d+_", "", col) for col in amenities_dummies.columns]

print("Primeiras linhas do DataFrame de dummies de amenities:")
print(amenities_dummies.head())

# Agrupar e combinar colunas com o mesmo nome
def group_columns(cols):
    grouped_cols = {}
    for col in cols:
        clean_col = re.sub(r"^\d+_", "", col.lower())
        if clean_col not in grouped_cols:
            grouped_cols[clean_col] = []
        grouped_cols[clean_col].append(col)
    return grouped_cols

grouped_columns = group_columns(amenities_dummies.columns)
new_df = pd.concat({group_name: amenities_dummies[cols].max(axis=1) for group_name, cols in grouped_columns.items()}, axis=1)

# Filtrar colunas de amenities com menos de 2% de presença
df_amenities_columns = new_df.replace({True: 1, False: 0}).reset_index(drop=True)
df_amenities_columns = df_amenities_columns.loc[:, df_amenities_columns.sum() / len(df_amenities_columns) * 100 > 2]

print("Colunas após filtrar amenities com mais de 2% de presença:")
print(df_amenities_columns.head())

# Excluir colunas com impacto insignificante
df_amenities_columns = df_amenities_columns.drop(labels='kitchen', axis=1, errors='ignore')
df_amenities_columns = df_amenities_columns.astype('bool')

# Concatenar colunas de amenities com o DataFrame principal
df_concat = pd.concat([df_amenities.drop('amenities', axis='columns'), df_amenities_columns], axis='columns')

print("Primeiras linhas do DataFrame final antes da filtragem de preço:")
print(df_concat.head())

# Data Cleaning: Handle 'price' Column
df_price = df_concat.copy()
q1_price, q3_price = np.percentile(df_price.price, [25, 75])
iqr_price = q3_price - q1_price
upper_boundry_price = q3_price + 1.5 * iqr_price

df_price = df_price[(df_price['price'] <= upper_boundry_price) & (df_price['price'] > 120000) & (df_price['price'] < 1000000)].reset_index(drop=True)

print(f'Rows after filtering price: {df_price.shape[0]}')

# Data Cleaning: Calculate 'price_per_sqft' and Handle Outliers
df_sqft_price = df_price.copy()
df_sqft_price['price_per_sqft'] = df_price['price'] / df_price['totalAreas']
neighborhood_stats = df_sqft_price.groupby('neighborhood')['price_per_sqft'].agg(['min', 'median', 'max'])
neighborhood_stats['q1'] = df_sqft_price.groupby('neighborhood')['price_per_sqft'].quantile(0.25)
neighborhood_stats['q3'] = df_sqft_price.groupby('neighborhood')['price_per_sqft'].quantile(0.75)
neighborhood_stats['iqr'] = neighborhood_stats['q3'] - neighborhood_stats['q1']
neighborhood_stats['upper_boundry'] = neighborhood_stats['q3'] + 1.5 * neighborhood_stats['iqr']

for neighborhood, upper_boundry in neighborhood_stats['upper_boundry'].items():
    df_sqft_price = df_sqft_price[(df_sqft_price['neighborhood'] != neighborhood) | 
                                  (df_sqft_price['price_per_sqft'] <= upper_boundry)]

df_sqft_price = df_sqft_price[df_sqft_price['price_per_sqft'] < 12715.91]

def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('neighborhood'):
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('bedrooms'):
            bhk_stats[bhk] = {
                'mean': np.mean(bhk_df.price_per_sqft),
                'std': np.std(bhk_df.price_per_sqft),
                'count': bhk_df.shape[0]
            }
        for bhk, bhk_df in location_df.groupby('bedrooms'):
            stats = bhk_stats.get(bhk - 1)
            if stats and stats['count'] > 5:
                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft < stats['mean']].index.values)
    return df.drop(exclude_indices, axis='index')

df4 = remove_bhk_outliers(df_sqft_price)

print("Primeiras linhas do DataFrame final após a remoção de outliers:")
print(df4.head())

# Save pre-processing data
df4.to_csv('dataset_preprocessado.csv', index=False)
print("Número final de linhas no DataFrame processado:", df4.shape[0])
