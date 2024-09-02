# Auth Serverless App

A serverless authentication service built using AWS Lambda, PostgreSQL, and Python. This project includes functionalities for user registration, login, fetching user details, and a health check endpoint.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Clone the Repository](#2-clone-the-repository)
  - [3. Setup PostgreSQL Database](#3-setup-postgresql-database)
  - [4. Configure Environment Variables](#4-configure-environment-variables)
  - [5. Install Python Dependencies](#5-install-python-dependencies)
  - [6. Populate the Database](#6-populate-the-database)
- [Running the Application Locally](#running-the-application-locally)
- [Deploying to AWS](#deploying-to-aws)
  - [1. Setup AWS CLI](#1-setup-aws-cli)
  - [2. Deploy with AWS SAM](#2-deploy-with-aws-sam)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Auth Serverless App is designed to provide a robust, scalable authentication service using serverless architecture. It leverages AWS Lambda for executing functions and PostgreSQL for storing user data. The application exposes several RESTful API endpoints to handle user authentication and data retrieval.

## Architecture

- **AWS Lambda**: Handles the serverless execution of user registration, login, and data retrieval functions.
- **PostgreSQL**: Used as the relational database to store user information.
- **AWS SAM (Serverless Application Model)**: Manages deployment, versioning, and aliasing of Lambda functions.
- **GitHub Actions**: Automates the deployment process upon code changes.

## Setup and Installation

### 1. Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [PostgreSQL 14+](https://www.postgresql.org/download/)
- [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate access
- [AWS SAM CLI](https://aws.amazon.com/serverless/sam/) for deployment
- [Git](https://git-scm.com/downloads) for version control

### 2. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/auth-serverless-app.git
cd auth-serverless-app
```

### 3. Setup PostgreSQL Database

1. **Install PostgreSQL**: Follow the instructions for your operating system to install PostgreSQL.
2. **Start PostgreSQL Service**:
    - **Linux**: `sudo systemctl start postgresql`
    - **macOS (Homebrew)**: `brew services start postgresql`
    - **Windows**: Use the PostgreSQL service manager.
3. **Access PostgreSQL**:
    ```bash
    psql -U postgres
    ```
4. **Create a Database and User**:
    ```sql
    CREATE DATABASE authdb;
    CREATE USER authuser WITH PASSWORD 'yourpassword';
    GRANT ALL PRIVILEGES ON DATABASE authdb TO authuser;
    ```

### 4. Configure Environment Variables

Create a `.env` file in the root directory to store your database credentials and other configuration settings:

```plaintext
POSTGRES_HOST=localhost
POSTGRES_DB=authdb
POSTGRES_USER=authuser
POSTGRES_PASSWORD=yourpassword
```

### 5. Install Python Dependencies

It’s recommended to use a virtual environment for Python dependencies.

1. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### 6. Populate the Database

Run the `populate_db.py` script to create the necessary tables and insert initial data into your PostgreSQL database:

```bash
python populate_db.py
```

## Running the Application Locally

To run the application locally for testing, you can use AWS SAM's local capabilities.

1. **Start the SAM local API**:
    ```bash
    sam local start-api
    ```

2. **Invoke a function locally**:
    ```bash
    sam local invoke "FunctionName" -e events/event.json
    ```

## Deploying to AWS

### 1. Setup AWS CLI

Configure the AWS CLI with your credentials:

```bash
aws configure
```

### 2. Deploy with AWS SAM

1. **Build the SAM application**:
    ```bash
    sam build
    ```

2. **Deploy the application**:
    ```bash
    sam deploy --guided
    ```

    Follow the prompts to set parameters and deploy the stack. Once deployed, note the API endpoint for testing.

## API Endpoints

1. **Register User**: `POST /register`
2. **Login User**: `POST /login`
3. **Get Single User**: `GET /user/{user_id}`
4. **Get All Users**: `GET /users`
5. **Health Check**: `GET /health`

## Testing

Use tools like Postman or curl to test the API endpoints. For example, to register a user:

```bash
curl --request POST 'http://localhost:3000/register' \
--header 'Content-Type: application/json' \
--data-raw '{"username": "testuser", "password": "testpassword"}'
```
