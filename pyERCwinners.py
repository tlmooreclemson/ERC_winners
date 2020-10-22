#!/usr/bin/env python3
"""
Created on: Wed Sep 21 11:49 2020
Created by: Thomas Moore
"""

# Load modules
from tabula import read_pdf
import pandas as pd


# Import the data for ERC StG 2020 Winners
file_path = "https://erc.europa.eu/sites/default/files/document/file/erc_2020_stg_results_all_domains.pdf"

df = read_pdf(file_path, pages = "all")
df = df[0::10] # extract only the relevant lists
df = pd.concat(df) # concantate all the data frames into a single large one

# Remove irrelevant rows
df = df[~df['Last name'].isin(['Last name'])] # drop rows with 'last name'
df = df[df['Last name'].notna()] # drop rows with NaN in 'last name' column

