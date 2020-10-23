#!/usr/bin/env python3
"""
Created on: Wed Sep 21 11:49 2020
Created by: Thomas Moore
"""

# Load modules
from tabula import read_pdf
import pandas as pd
#from pybliometrics.scopus import AuthorSearch, AuthorRetrieval, CitationOverview
from scholarly import scholarly


# Import the data for ERC StG 2020 Winners
file_path2020 = "https://erc.europa.eu/sites/default/files/document/file/erc_2020_stg_results_all_domains.pdf"
"""
paths for other years
"""
file_path2019 = "https://erc.europa.eu/sites/default/files/document/file/erc_2019_stg_results_all_domains.pdf"
file_path2018 = "https://erc.europa.eu/sites/default/files/document/file/erc_2018_stg_results_all_domains.pdf"
file_path2017 = "https://erc.europa.eu/sites/default/files/document/file/erc_2017_stg_results_pe.pdf"
file_path2016 = "https://erc.europa.eu/sites/default/files/document/file/erc_2016_stg_results_all_domains.pdf"
file_path2015 = "https://erc.europa.eu/sites/default/files/document/file/erc_2015_stg_results_all_domains.pdf"
file_path2014 = "https://erc.europa.eu/sites/default/files/document/file/erc_2014_stg_results_all_domains.pdf"
file_path2013 = "https://erc.europa.eu/sites/default/files/document/file/erc_2013_stg_results_all_domains.pdf"
file_path2012 = "https://erc.europa.eu/sites/default/files/document/file/erc_2012_stg_results_all_domains.pdf"
file_path2011 = "https://erc.europa.eu/sites/default/files/document/file/erc_2011_stg_results_all_domains.pdf"
file_path2010 = "https://erc.europa.eu/sites/default/files/document/file/erc_2010_stg_results_all%20domains.pdf"


df_2020 = read_pdf(file_path2020, pages = "all")
# df = df[0::10] # extract only the relevant lists
df_2020 = pd.concat(df_2020) # concantate all the data frames into a single large one
df_2020 = df_2020.replace({'-\r': ' '}, regex=True) # remove these separators from file
df_2020.columns = df_2020.columns.str.replace('\r', ' ') # remove \r from column names

# Remove irrelevant rows
df_2020 = df_2020[~df_2020['Last name'].isin(['Last name'])] # drop rows with 'last name'
df_2020 = df_2020[df_2020['Last name'].notna()] # drop rows with NaN in 'last name' column

# Get the list of 2020 winner names
winnerList_2020 = df_2020['First name']+' '+df_2020['Last name']
winnerList_2020 = winnerList_2020.to_list()

# Citation data library

