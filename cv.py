import pandas as pd

from types import GeneratorType

class NestedCV:
    def __init__(self, k):
        self.k = k

    def split(self, data, date_column):
        # Write Nested Cross validation for time series
        # logic here and return the train and validate dataframes
        # return a generator object for the splits

if __name__ == "__main__":
    # load dataset
    data = pd.read_csv("paht to dataset")
    data["date"] = pd.to_datetime(data["date"])

    # nested cv
    k = 3
    cv = NestedCV(k)
    splits = cv.split(data, "date")

    # check return type
    assert isinstance(splits, GeneratorType)

    # check return types, shapes, and data leaks
    count = 0
    for train, validate in splits:
        
        # types
        assert isinstance(train, pd.DataFrame)
        assert isinstance(validate, pd.DataFrame)

        # shape
        assert train.shape[1] == validate.shape[1]

        # data leak
        assert train["date"].max() <= validate["date"].min()

        count += 1

    # check number of splits returned
    assert count == k