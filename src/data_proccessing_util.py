"""Utilities fuction to proccess data"""

from typing import Union
from pandas import DataFrame
import numpy as np
import pandas as pd


from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def filtered_df(
    df: pd.DataFrame,
    columns: Union[None, list[str]] = None,
    rm_columns: Union[None, list[str]] = None,
) -> pd.DataFrame:
    """This function return a pandaas dataframe with the passed columns or
    the original columns without the rm_column.

    Args:
        df (pd.DataFrame): _description_
        columns (Union[None, list[str]], optional): The columns that you want
        to have in the dataframe. Defaults to None.
        rm_columns (Union[None, list[str]], optional): The columns to be remove
        from the original dataframe. Defaults to None.

    Returns:
        pd.DataFrame: A pandas dataframe with the filtered columns,
        or the original dataframe if neither `columns` or `rm_columns` was passed.
    """
    # set the columns to be modified based on the comlumns passed.
    if columns:
        df_columns = columns
    else:
        df_columns = df.columns.to_list()

    if rm_columns:
        for col_to_remove in rm_columns:
            if col_to_remove in df_columns:
                df_columns.remove(col_to_remove)

        # return df[df_columns]

    # if not columns:
    #     return df

    return df[df_columns]


def one_shot_encode_categorical_columns(df: DataFrame) -> DataFrame:
    """This function convert the dataframe's categorical data to numerical using one-hot encoding

    Args:
        df (DataFrame): The pandas dataframe to be converted

    Returns:
        (DataFrame): Converted dataframe
    """
    encoder = OneHotEncoder(sparse_output=False)
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

    # One-hot encode the categorical columns
    one_hot_encoded = encoder.fit_transform(df[categorical_columns])

    # Create a DataFrame with the one-hot encoded columns
    one_hot_encoded_df = pd.DataFrame(
        one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns)
    )

    # Drop the original categorical columns and concatenate the new one-hot encoded columns
    df = pd.concat([df, one_hot_encoded_df], axis=1)
    df = df.drop(columns=categorical_columns)

    return df


def label_encode_categorical_columns(df: DataFrame) -> DataFrame:
    """This function convert the dataframe's categorical data to numerical using label encoding

    Args:
        df (DataFrame): The pandas dataframe to be converted

    Returns:
        (DataFrame): Converted dataframe
    """
    label_encoders = {}
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

    for column in categorical_columns:
        label_encoder = LabelEncoder()
        df[column] = label_encoder.fit_transform(df[column])
        label_encoders[column] = label_encoder
    return df


def get_df_info(df: DataFrame):
    """This function take a pandas dataframe and display information about it


    Args:
        df (Dataframe): Th dataframe that will be inspected
    """
    print("Shape: ", df.shape, "\n")
    print("Columns: ", df.columns.to_list(), "\n")
    print(
        "Categorical columns: ",
        df.select_dtypes(include=["object"]).columns.tolist(),
        "\n",
    )

    print("Information: ")
    df.info()
    print("\n")

    print("Unique values in each column: ")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()}")
    print("\n")

    print("Null values in each column: ", df.isnull().sum(), "\n")

    print("Duplicate rows: ", df.duplicated().sum(), "\n")

    print("Statistics: ", df.describe().transpose(), "\n")


if __name__ == "__main__":
    pass
