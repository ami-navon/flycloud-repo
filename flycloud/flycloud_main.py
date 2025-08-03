# python flycloud/flycloud_main.py s3://centrical-data-bucket/tracking_video/20250731/debug.mp4
import os
import sys
import boto3
from urllib.parse import urlparse
from google.cloud import storage


def fly_download(url, local_folder="."):
    """
    Download files from AWS S3 or GCP storage based on URL prefix.
    
    Args:
        url (str): The storage URL (s3:// or gs://)
        local_folder (str): Local destination folder (default: current directory)
    
    Returns:
        str: Path to the downloaded file
    """
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
    
    if url.startswith("s3://"):
        return _download_from_s3(url, local_folder)
    elif url.startswith("gs://"):
        return _download_from_gcs(url, local_folder)
    else:
        raise ValueError("URL must start with 's3://' or 'gs://'")


def _download_from_s3(s3_url, local_folder):
    """Download file from AWS S3 using boto3."""
    parsed = urlparse(s3_url)
    bucket_name = parsed.netloc
    object_key = parsed.path.lstrip('/')
    
    filename = os.path.basename(object_key)
    local_path = os.path.join(local_folder, filename)
    
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket_name, object_key, local_path)
    
    return local_path


def _download_from_gcs(gcs_url, local_folder):
    """Download file from GCP storage using Google Cloud Storage Python library."""
    parsed = urlparse(gcs_url)
    bucket_name = parsed.netloc
    blob_name = parsed.path.lstrip('/')
    
    filename = os.path.basename(blob_name)
    local_path = os.path.join(local_folder, filename)
    
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(local_path)
    
    return local_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python flycloud_main.py <s3://bucket/file or gs://bucket/file> [local_folder]")
        sys.exit(1)
    
    url = sys.argv[1]
    local_folder = sys.argv[2] if len(sys.argv) > 2 else "."
    
    try:
        downloaded_file = fly_download(url, local_folder)
        print(f"Successfully downloaded: {downloaded_file}")
    except Exception as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)