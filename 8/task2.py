import plotly.express as px
import pandas as pd

df = pd.read_csv("8/udemy_courses_extended.csv")

free = df[df["is_paid"] == False]
paid = df[df["is_paid"] == True]

def process(_df):
    amount = len(_df)
    max_subs = _df["num_subscribers"].max()
    min_subs = _df["num_subscribers"].min()
    avg_subs = _df["num_subscribers"].mean()
    all = len(_df[_df["level"] == "All Levels"])
    beginner = len(_df[_df["level"] == "Beginner Level"])
    intermediate = len(_df[_df["level"] == "Intermediate Level"])
    expert = len(_df[_df["level"] == "Expert Level"])

    _df = pd.DataFrame(dict(
        group = ["amount", "max", "min", "avg", "all", "beginner", "intermediate", "expert"],
        value = [amount, max_subs, min_subs, avg_subs, all, beginner, intermediate, expert]))

    fig = px.bar(_df, x = "group", y = "value")

    fig.show()

try:
    ispaid = int(input("Is paid? (0/1): "))
except TypeError as e:
    print(e)

if ispaid:
    data = paid
else:
    data = free

process(data)