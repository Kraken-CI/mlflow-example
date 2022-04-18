import csv
from os import path
import datetime
from tempfile import mkdtemp as create_tmp_dir

import click
import mlflow
import requests
import pandas_datareader as web

from constants import DATASET_ARTIFACT_DIR, DATASET_NAME


@click.command(help="Downloads the stock market dataset for given company. Saves it as an mlflow artifact")
@click.option("--company-abbreviation", type=str)
def download_csv(company_abbreviation: str):
    with mlflow.start_run(run_name="download"):
        today = datetime.datetime.today()
        begin = today - datetime.timedelta(weeks=10*54)  # 10 years back
        data_frame = web.DataReader(company_abbreviation, data_source='yahoo', start=begin, end=today)

        local_dir = create_tmp_dir()
        local_filename = path.join(local_dir, DATASET_NAME)
        print(f"Downloading {company_abbreviation} to {local_filename}")

        data_frame.to_csv(local_filename)

        print(f"Uploading stock market data: {local_filename}")
        mlflow.log_artifact(local_filename, DATASET_ARTIFACT_DIR)


if __name__ == '__main__':
    download_csv()
