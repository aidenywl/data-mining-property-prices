import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV
from typing import List

"""
To deal with NaN Values, we use imputation.
"""
def imputer_fit_transform_for_areasize(df: pd.DataFrame) -> (KNNImputer, pd.DataFrame):
    temp_df = df.drop(columns=['bathrooms', 'no_of_units'])
    # Drop rows with bedroom nan. We can do this because
    # all rows with nan area_size has a non-nan bedroom field.
    temp_df = temp_df[~temp_df['bedrooms'].isna()]
    # Assert no other nulls besides area_size
    assert not any(temp_df.drop(columns=['area_size']).isna().any())
    imputer = KNNImputer(n_neighbors=3)
    imputer.fit(temp_df)
    temp_df[:] = imputer.transform(temp_df)
    result_df = df.copy()
    result_df.update(temp_df)
    return imputer, result_df
    
def imputer_fit_dataframe(df: pd.DataFrame, target_col: str, cols_to_ignore: List[str]=['bedrooms', 'bathrooms', 'no_of_units', 'price']) -> (KNNImputer, pd.DataFrame):
    """
    This function is called to impute values for the target column passed as argument.
    
    We impute without columns that have nulls.
    
    Args:
        df (pd.DataFrame): Dataframe to be processed.
        target_col (str): Column to impute.
    
    Returns:
        pd.DataFrame: Returns a dataframe with the imputed values.
    """
    temp_df = remove_null_col_df(df, target_col, cols_to_ignore)
    # Impute and fit.
    imputer = KNNImputer(n_neighbors=3)
    imputer.fit(temp_df)
    return imputer, temp_df    
    
def imputer_predict(df: pd.DataFrame, target_col: str, imputer: KNNImputer, cols_to_ignore: List[str] = ['bedrooms', 'bathrooms', 'no_of_units']) -> pd.DataFrame:
    # Transform
    temp_df = remove_null_col_df(df, target_col, cols_to_ignore)
    temp_df[:] = imputer.transform(temp_df)
    result_df = df.copy()
    result_df.update(temp_df)
    result_df[target_col] = result_df[target_col].round()
    return result_df
    
def remove_null_col_df(df: pd.DataFrame, target_col: str, cols_to_ignore: List[str]) -> pd.DataFrame:
    if target_col in cols_to_ignore: cols_to_ignore.remove(target_col)
    temp_df = df.drop(columns=cols_to_ignore)
    assert not all(temp_df.isna().any()), "Other dataframe rows should not have any null values for imputation"
    return temp_df
    