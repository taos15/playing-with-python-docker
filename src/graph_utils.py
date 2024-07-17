import numpy as np
import numpy.typing as npt  # numpy typing method
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns
from typing import Any, Union


def gender_boxplot_graph(
    df: pd.DataFrame,
    gender: str = "male",
    title: Union[str, None] = None,
    **kwargs: Any,
):
    """This function geranate a boxplot base on the geder passed, it defaults to male.

    Args:
        df (pd.DataFrame): The dataframe with the data
        gender (str, optional): The gender to create the table. Defaults to "male".
        kwargs (Any, optional): Any argument to be passed to the boxplot
    """
    ax: Axes

    fig, ax = plt.subplots(figsize=(12, 20))
    if "male" in gender.lower():
        sns.boxplot(
            data=df[df["Gender"] == 1].drop("Gender", axis=1),
            **kwargs,
        )
    else:
        sns.boxplot(
            data=df[df["Gender"] == 0].drop("Gender", axis=1),
            legend=True,
            **kwargs,
        )

    ax.set_title(title if title else f"{gender.capitalize()} Graph")

    plt.show()


if __name__ == "__main__":
    pass
