import pandas as pd
import os

curr_dir = os.path.dirname(__file__)

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_deals = pd.read_csv(curr_dir+"/flight_deal_prices.csv")

    def get_flight_deals(self):
        print(self.flight_deals.head())

FlightData().get_flight_deals()