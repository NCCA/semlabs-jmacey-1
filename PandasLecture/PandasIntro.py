import marimo

__generated_with = "0.17.2"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    ages = pd.Series([22,35,58,34,23,35,23,34,23,23,45,34,45,34,45,34,45,34,45],name="Ages")
    print(ages)
    return (ages,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can process this data by running functions on it""")
    return


@app.cell
def _(ages):
    print(f"{ages.max()=}")
    print(f"{ages.min()=}")
    print(f"{ages.mean()=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Data Frames

    These can be built directly using a json dictionary
    """
    )
    return


@app.cell
def _(pd):
    data={}
    data["Name"]=["Tom","Jon","Jess"]
    data["Age"]=[22,55,6]
    data["Sex"]=["Male","Male","Female"]
    print(data)
    df = pd.DataFrame(data)
    print(df)
    return (df,)


@app.cell
def _(df):
    print(df["Name"])
    print(df["Name"][0])
    return


@app.cell
def _(df):
    print(df.loc[2])
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.sum()
    return


if __name__ == "__main__":
    app.run()
