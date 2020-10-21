#!/usr/bin/env python3
"""
Created on: Wed Sep 21 11:49 2020
Created by: Thomas Moore
"""

# Load modules
from tabula import read_pdf

# Import the data for ERC StG 2020 Winners
file_path = "https://erc.europa.eu/sites/default/files/document/file/erc_2020_stg_results_all_domains.pdf"

df = read_pdf(file_path, pages = "all")
df = df[0::10]

# Each page is on a multiple of 10, i.e. df[0], df[10], df[20]... etc.
