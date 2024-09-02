# config.py

import os

POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'lambdadb')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'lambdapsql')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
