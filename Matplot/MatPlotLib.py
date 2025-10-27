#!/usr/bin/env -S uv run marimo edit

import marimo

__generated_with = "0.17.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Intro to Matplotlib

    In this notebook I am going to use matplot lib to display some charts and images.
    """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    # lets do a simple simple plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    return np, plt, x, y


@app.cell
def _(plt, x, y):
    cm = 1 / 2.54
    figsize = (5 * cm, 5 * cm)
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.show()
    return (figsize,)


@app.cell
def _(figsize, plt, x, y):
    plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.show()
    return


@app.cell
def _(plt, x, y):
    # we can change line style and colours
    plt.plot(x, y, color="purple", linestyle="dotted")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Plot types

    1. Line Plots
    2. scatter plots
    3. Bar plots
    4. Histogram
    """
    )
    return


@app.cell
def _(np, plt, y):
    _x = np.linspace(0, 10, 100)
    _y = np.random.rand(100)
    fig, axs = plt.subplots(2, 2, figsize=(7, 7))
    axs[0, 0].plot(_x, _y)
    axs[0, 1].scatter(_x, _y)
    axs[1, 0].bar(_x, _y)
    axs[1, 1].hist(y)
    plt.show()
    return


@app.cell
def _(np, plt, x, y):
    _x = np.linspace(0, 10, 100)
    _y = np.random.rand(100)
    plt.plot(x, y)
    plt.xlabel("x - axis")
    plt.ylabel("y axis")
    plt.title("Random values in y")
    plt.show()
    return


@app.cell
def _(plt):
    from PIL import Image

    _fig, _ax = plt.subplots(3, 3, figsize=(10, 10), constrained_layout=True)
    [axi.set_axis_off() for axi in _ax.ravel()]

    curr_row = 0
    index = 0
    for row in range(0, 3):
        for col in range(0, 3):
            try:
                a = Image.open(f"images/test.{index:04}.png")
                index += 1
                _ax[col, row].imshow(a)
                _ax[col, row].set_title(f"test.{index:04}.png")
            except FileNotFoundError:
                pass

    plt.show()
    return


@app.cell
def _(np):
    def rand_colour():
        return np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)
    return (rand_colour,)


@app.cell
def _(plt, rand_colour):
    colours = [rand_colour() for _ in range(0, 30)]
    # the above is the same as
    # colours=[]
    # for _ in range(0,20) :
    #     colours.append(rand_colour())

    _f, _ax = plt.subplots(1, len(colours), figsize=(20, 20))
    for _index, c in enumerate(colours):
        _ax[_index].set_axis_off()
        _ax[_index].imshow([[c]])

    plt.show()
    return


@app.cell
def _(np, plt):
    img = np.random.randint(0, 255, (20, 20, 4))
    plt.imshow(img)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
