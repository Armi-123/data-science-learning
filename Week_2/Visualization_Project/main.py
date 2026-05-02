from charts import line_plot, bar_chart, scatter_plot
import pandas as pd

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [120, 150, 170, 160, 210],
    "Visitors": [200, 240, 245, 260, 300]
}

df = pd.DataFrame(data)

line_plot(df)
bar_chart(df)
scatter_plot(df)
