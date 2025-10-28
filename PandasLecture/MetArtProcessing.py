import marimo

__generated_with = "0.17.2"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Met Art Dataset processing

    In this notebook we will download and process the data from the met museum of art in America. We will download the data set locally and then process it. 
    """
    )
    return


@app.cell
def _():
    data_dir="./data/met_objects"
    from pathlib import Path
    Path(data_dir).mkdir(parents=True,exist_ok=True)
    return Path, data_dir


@app.cell
def _(Path, data_dir):
    import requests

    def download(url : str , fname : str) :
        resp = requests.get(url,stream=True, verify=False)
        total = int(resp.headers.get("content-lenght",0))
        with open(fname,"wb") as file :
            for data in resp.iter_content(chunk_size=1024) :
                file.write(data)

    url = (
        "https://nccastaff.bournemouth.ac.uk/jmacey/SEForMedia/DataSets/MetObjects.zip"
    )

    zip_file = f"{data_dir}/MetObjects.zip"
    csv_file = f"{data_dir}/MetObjects.csv"
    if not Path(zip_file).exists() :
        download(url,zip_file)
    else :
        print("file already there")
    return csv_file, zip_file


@app.cell
def _(Path, csv_file, data_dir, zip_file):
    import zipfile

    if not Path(csv_file).exists() :
        with zipfile.ZipFile(zip_file,"r") as zip_ref :
            print(f"extracting {zip_file}")
            zip_ref.extractall(data_dir)
    return


@app.cell
def _(csv_file):
    import pandas as pd
    import matplotlib.pyplot as plt

    dataset = pd.read_csv(csv_file,sep=",")
    dataset



    return (dataset,)


@app.cell
def _(dataset):
    # get rows 29 - 35
    _int_indexing = dataset.iloc[29:35]
    _int_indexing
    return


@app.cell
def _(dataset):
    # Boolean data series 
    medieval_art_bool_series = dataset["Department"] == "Medieval Art"
    dataset.loc[medieval_art_bool_series]
    return


@app.cell
def _(dataset):
    departments = dataset["Department"]
    departments=departments.unique()
    for _i,_v in enumerate(departments) :
        print(f"{_i} {_v}")

    photos = dataset["Department"] == departments[11]
    instruments = dataset["Department"] == departments[17]
    dataset.loc[photos | instruments]

    return


@app.cell
def _(dataset):
    _g = dataset.groupby(["Object Name","Culture"])
    _g = _g.size().reset_index(name="Counts")
    _g=_g.where(_g["Counts"] > 1 )
    _g.dropna()
    _g.sort_values("Counts",ascending = False)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
