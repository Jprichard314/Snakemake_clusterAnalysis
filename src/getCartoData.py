from pyUtils.apis.phillyOpenData import cartoApi
import pyUtils.apis.phillyOpenData
import requests
import pandas as pd
import datetime


def snakemake__cartoApi(query,outpath):
    data = cartoApi(query).queryDataframe()
    data.to_excel(
          outpath
        , sheet_name = 'queryData'
    )

# Get Shooting Data
snakemake__cartoApi(
        query = pyUtils.apis.phillyOpenData.writeDateTimeFilter(
              datetime.datetime.now().strftime('%m/%d/%Y')
            , 13
            , "select * from shootings"
            , "date_"
        )
        , outpath = snakemake.output[0]
        )

# Get Crimes Data
snakemake__cartoApi(
        query = pyUtils.apis.phillyOpenData.writeDateTimeFilter(
              datetime.datetime.now().strftime('%m/%d/%Y')
            , 13
            , "select * from incidents_part1_part2"
            , "dispatch_date_time"
        )
        , outpath = snakemake.output[1]
        )

# Get arrests Data
snakemake__cartoApi(
        query = pyUtils.apis.phillyOpenData.writeDateTimeFilter(
              datetime.datetime.now().strftime('%m/%d/%Y')
            , 13
            , "select * from arrests_census"
            , "day"
        )
        , outpath = snakemake.output[2]
        )

