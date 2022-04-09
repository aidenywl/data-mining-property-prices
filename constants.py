# Columns to ignore
TO_IGNORE = [
    "subszone",
    "street", # we simply go by lat and long
    "listing_id", # don't think it affects the price
    "name",
    "model", # we drop this because type is more than enough.
    "market_segment", # Only one value, ocr.
    "type_of_area", # Only one value, strata.
    "eco_category", # only one value, uncategorized.
    "accessibility", # only one value, guarded.
    "date_listed", # Redundant information,
    "built_year" # drop as there's too many missing cols, 10043
]