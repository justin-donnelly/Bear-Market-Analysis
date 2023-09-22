import pandas as pd 

class BearMarket:
    def __init__(self, sp500_df):
        self.sp500_df = sp500_df
        self.bear_data = {}
        self.return_data = {}
        
        self.start_dates = [
            pd.to_datetime('1973-01-01').date(),
            pd.to_datetime('1980-11-24').date(),
            pd.to_datetime('2000-03-20').date(),
            pd.to_datetime('2007-07-12').date(),
            pd.to_datetime('2020-02-19').date(),
            pd.to_datetime('2022-01-04').date(),
        ]

        self.end_dates = [
            pd.to_datetime('1974-09-30').date(),
            pd.to_datetime('1982-08-09').date(),
            pd.to_datetime('2002-09-30').date(),
            pd.to_datetime('2009-03-02').date(),
            pd.to_datetime('2020-03-23').date(),
            pd.to_datetime('2022-10-12').date(),
        ]

    def process_period(self, start_date, end_date, label):
        bear_df = self.sp500_df.loc[start_date:end_date]
        bear_returns = bear_df.pct_change().dropna()

        self.bear_data[label] = bear_df
        self.return_data[label] = bear_returns

    def process_periods(self, labels):
        for start, end, label in zip(self.start_dates, self.end_dates, labels):
            self.process_period(start, end, label)

    def get_data(self, label):
        bear_df = self.bear_data.get(label, pd.DataFrame())
        bear_returns_df = self.return_data.get(label, pd.DataFrame())
        return bear_df, bear_returns_df
    
class YieldProcessor:
    def __init__(self, yield_df):
        self.yield_df = yield_df
        self.yield_data = {}
        self.return_data = {}
        
        self.start_dates = [
            '1973-01-01',
            '1980-11-24',
            '2000-03-20',
            '2007-07-12',
            '2020-02-19',
            '2022-01-04',
        ]

        self.end_dates = [
            '1974-09-30',
            '1982-08-09',
            '2002-09-30',
            '2009-03-02',
            '2020-03-23',
            '2022-10-12',
        ]

    def process_period(self, start_date, end_date, label):
        yield_period = self.yield_df.loc[start_date:end_date]
        yield_returns = yield_period.pct_change().dropna()

        self.yield_data[label] = yield_period
        self.return_data[label] = yield_returns

    def process_periods(self, labels):
        for start, end, label in zip(self.start_dates, self.end_dates, labels):
            self.process_period(start, end, label)

    def get_data(self, label):
        yield_df = self.yield_data.get(label, pd.DataFrame())
        yield_returns_df = self.return_data.get(label, pd.DataFrame())
        return yield_df, yield_returns_df
