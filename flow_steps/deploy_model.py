from os import path

import boto3
import click
import mlflow

from constants import ML_MODEL_NAME, H5_MODEL_NAME


@click.command(help="Deploy trained model to S3 bucket")
@click.option("--model-dir", type=str)
@click.option("--bucket-name", type=str)
def deploy_model(model_dir: str, bucket_name: str):
    with mlflow.start_run(run_name="deploy"):
        s3 = boto3.client("s3",
                          aws_access_key_id="AKIAIP7CJ7NG2LXDCV2A",
                          aws_secret_access_key="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"
                          )
        s3.create_bucket(Bucket=bucket_name)

        ml_model_dir = path.join(model_dir, ML_MODEL_NAME)
        h5_model_dir = path.join(model_dir, H5_MODEL_NAME)
        s3.upload_file(ml_model_dir, bucket_name, ml_model_dir)
        s3.upload_file(h5_model_dir, bucket_name, h5_model_dir)
        print("File uploaded on S3")


if __name__ == '__main__':
    deploy_model()
