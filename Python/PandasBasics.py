# DataFrame is a table
# Series is a column in DataFrame

# %%
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

df

# %%
print(type(df))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())