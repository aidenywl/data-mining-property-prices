from geopy import distance
import pandas as pd

def distance_ll(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    return distance.distance((lat1, lng1), (lat2, lng2))

def dist_to_nearest_item(expr: pd.DataFrame, aux_df: pd.DataFrame) -> str:
    return round(min(aux_df.apply(lambda x: distance_ll(expr['lat'], expr['lng'], x['lat'], x['lng']), axis=1)), 1)
    