# Title: Factorio Calculator
# Author: Melody Musmacker
# Description: Takes the desired output quantity + resource desired and recursively run down the tree that forms to return all required inputs.
# Note: Assumes first-craft ingredients are the most atomic form of ingredient & that their inputs are infinite.

# Required Packages
import pandas as pd

# Load up base Factorio item information.
items = pd.read_csv('Factorio.csv')


def beginCalculation(desiredQuant,desiredResource):
    items.loc[items["Name"] ==]
    if items.loc["Input"] == desiredResource:
        return 0
    else:
        return "Error: Item Not Found."
        # items[items['Name'] == desiredResource]


def output2Input(desiredQuant,desiredResource):
    if items['Input'] == "Null":
        return 0