import plotly.express as px
import pandas as pd

df = pd.read_csv("8/data_country.csv")

min_health = df["health"].min()
max_health = df["health"].max()
delta_health = max_health - min_health
k_health = 100 / delta_health
df["health_relative"] = (delta_health - max_health + df["health"]) * k_health

min_income = df["income"].min()
max_income = df["income"].max()
delta_income = max_income - min_income
k_income = 100 / delta_income
df["income_relative"] = (delta_income - max_income + df["income"]) * k_income

min_inflation = df["inflation"].min()
max_inflation = df["inflation"].max()
delta_inflation = max_inflation - min_inflation
k_inflation = 100 / delta_inflation
df["inflation_relative"] = (delta_inflation - max_inflation + df["inflation"]) * k_inflation

min_life_expectancy = df["life_expectancy"].min()
max_life_expectancy = df["life_expectancy"].max()
delta_life_expectancy = max_life_expectancy - min_life_expectancy
k_life_expectancy = 100 / delta_life_expectancy
df["life_expectancy_relative"] = (delta_life_expectancy - max_life_expectancy + df["life_expectancy"]) * k_life_expectancy

fig = px.imshow(df[["health_relative", "income_relative", "inflation_relative", "life_expectancy_relative"]],
                labels = dict(x = "Stats", y = "Countries", color = "Legend"),
                x = ['health_relative', 'income_relative', 'inflation_relative', 'life_expectancy_relative'],
                y = df["country"])

fig.show() 
 
 

