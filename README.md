# FlyCloud

A cloud storage utility library for downloading files from AWS S3 and Google Cloud Storage.

## Installation

```bash
pip install flycloud
```

## Usage

```python
from flycloud import fly_download

# Download from S3
fly_download("s3://bucket/file.txt", "./downloads")

# Download from GCS
fly_download("gs://bucket/file.txt", "./downloads")
```