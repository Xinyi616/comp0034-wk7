# Add code to create the chart here
from pathlib import Path

import pandas as pd
import plotly.express as px

event_data = Path(__file__).parent.parent.joinpath("data", "paralympic_events.csv")


def line_chart(feature):
    """ Creates a line chart with data from paralympics_events.csv

    Data is displayed over time from 1960 onwards.
    The figure shows separate trends for the winter and summer events.

     Parameters
     feature: events, sports or participants

     Returns
     fig: Plotly Express line figure
     """

    # take the feature parameter from the function and check it is valid
    if feature not in ["sports", "participants", "events", "countries"]:
        raise ValueError(
            'Invalid value for "feature". Must be one of ["sports", "participants", "events", "countries"]')
    else:
        # Make sure it is lowercase to match the dataframe column names
        feature = feature.lower()

    # Read the data from pandas into a dataframe
    cols = ["type", "year", "host", "events", "sports", "participants", "countries"]
    line_chart_data = pd.read_csv(event_data, usecols=cols)

    # Create a Plotly Express line chart with the following parameters
    #  line_chart_data is the DataFrane
    #  x="year" is the column to use as a x-axis
    #  y=feature is the column to use as the y-axis
    # color="type" indicates if winter or summer
    fig = px.line(line_chart_data, x="year", y=feature, color="type")
    return fig