"""
FlyCloud - A cloud storage utility library for AWS S3 and GCP.
"""

from .flycloud_main import fly_download
from .flyclass import GCPFly,AWSFly

__version__ = "1.0.0"
__all__ = ["fly_download"]