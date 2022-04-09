from typing import List
import pandas as pd
import re
from datetime import datetime
from dateutil import relativedelta


def process_bedroom_sum(expr) -> int:
    """
    Cleans the bedroom column by summing up + values.
    """
    if pd.isna(expr):
        return expr
    if str(expr) == '10+':
        return 10
    return eval(str(expr))


def process_bedroom_half(expr) -> int:
    """
    Cleans the bedroom column by summing half the additional value
    so 4+1 becomes 4.5, 4+2 becomes 5. This is to account for the nuance that 
    the additional room is reported separately because it may not hold the same value as
    a traditional bedroom (it could be a small bedroom, a servant quarter, an additional study or living room, etc)
    """
    if (type(expr) == str):
        if (len(expr) == 1):
            return int(expr)
        elif (len(expr) > 1):
            # assuming all values are of the type operand_1 + operand_2
            op_1, op_2 = int(expr[0]), int(expr[2])
            return op_1 + (op_2 / 2)
        else:
            # null value, returning NaN for completion sake
            return expr
    else:
        return expr


def categorical_to_onehot(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    one_hot = pd.get_dummies(df[cols])
    df = df.drop(columns=cols)
    df = df.join(one_hot)
    return df


def tenure_to_ratio_var(expr: str) -> str:
    """
    Convert tenure to a ratio variable: 
        999: 999 years or freehold
        99: start date of tenure unkown, so leaving it as is
        X: if start date is available, we calculate number of years left
    """
    if pd.isna(expr):
        return '99'  # assume standard 99
    # get number of years
    res = re.search(r'(\d+)[^\d]+[yY]ears', expr)
    if res is None:
        return 999
    years = int(res.group(1))
    start_date = re.search(r'\d{2}/\d{2}/\d{4}', expr)
    if start_date is None:
        return years
    else:
        # calculate already used up tenure
        date_info = start_date.group().split('/')
        start_year, start_month, start_date = int(
            date_info[2]), int(date_info[1]), int(date_info[0])
        start_date = datetime(start_year, start_month, start_date)
        curr_date = datetime(2022, 3, 31)
        diff = relativedelta.relativedelta(curr_date, start_date)
        years_left = years - diff.years
        return years_left


def tenure_to_binary(expr: str) -> str:
    """
    Convert tenure to two one-hot columns:
        tenure_freehold: 999 years or freehold
        tenure_60: houses that are only 60 years.
        tenure_99: houses that have a 99 years leasehold.

    If the tenure is missing, we assume a standard 99 as that is the most frequent housing tenure model in Singapore.
    """
    if pd.isna(expr):
        return '99'  # assume standard 99
    # get number of years
    res = re.search(r'(\d+)[^\d]+[yY]ears', expr)
    if res is None:
        return 'freehold'
    years = int(res.group(1))
    if years > 100:
        return 'freehold'
    elif years > 70:
        return '99'
    else:
        return '60'


print(tenure_to_ratio_var('leasehold/99 years'))
