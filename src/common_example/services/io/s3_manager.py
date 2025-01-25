import boto3


class S3Manager:
    """
    S3Manager class to upload and download files from S3 bucket
    """

    def __init__(self):
        pass

    def upload_file(self, bucket_name: str, file_path: str, key: str):
        """_summary_

        Args:
            bucket_name (str): _description_
            file_path (str): _description_
            key (str): _description_
        """
        s3 = boto3.client("s3")
        try:
            s3.upload_file(file_path, bucket_name, key)
            print(f"File uploaded successfully to S3 bucket: {bucket_name}")
        except Exception as e:
            print(f"Error uploading file to S3 bucket: {e}")

    def download_file(self, bucket_name, key, file_path):
        """_summary_

        Args:
            bucket_name (_type_): _description_
            key (_type_): _description_
            file_path (_type_): _description_
        """
        s3 = boto3.client("s3")
        try:
            s3.download_file(bucket_name, key, file_path)
            print(f"File downloaded successfully from S3 bucket: {bucket_name}")
        except Exception as e:
            print(f"Error downloading file from S3 bucket: {e}")
