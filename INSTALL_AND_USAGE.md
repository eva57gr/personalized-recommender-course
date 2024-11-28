# Installation and Usage Guide

This guide will help you set up and run a machine learning pipeline that includes feature engineering, model training, and deployment using Hopsworks and OpenAI.

# Prerequisites

## Local Tools
You'll need the following tools installed locally:
- [Python v3.11](https://www.python.org/downloads/)
- [uv v0.4.30](https://github.com/astral-sh/uv) - Python package installer and virtual environment manager
- [GNU Make 3.81](https://www.gnu.org/software/make/) - Build automation tool

## Cloud Services
The project requires access to these cloud services:

| Service | Purpose | Cost | Required Credentials | Setup Guide |
|---------|---------|------|---------------------|-------------|
| [Hopsworks](https://rebrand.ly/serverless-github) | AI Lakehouse for feature store, model registry, and serving | Free tier available | `HOPSWORKS_API_KEY` | [Create API Key](https://docs.hopsworks.ai/latest/user_guides/projects/api_key/create_api_key/) |
| [OpenAI API](https://openai.com/index/openai-api/) | LLM API for recommender system | Pay-per-use | `OPENAI_API_KEY`<br>`OPENAI_MODEL_ID` | [Quick Start Guide](https://platform.openai.com/docs/quickstart) |

# Getting Started

## 1. Installation

Set up the project environment by running:
```bash
make install
```

This command will:
- Create a virtual environment using `uv`
- Activate the virtual environment
- Install all dependencies from `pyproject.toml`

## 2. Environment Configuration

Before running any components:
1. Create your environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and configure the required credentials following the inline comments.

# Running the Pipeline

You can run the entire pipeline at once or execute individual components.

## Running the Complete Pipeline

Execute all components in sequence:
```bash
make all
```

This runs the following steps:
1. Feature engineering
2. Retrieval model training
3. Ranking model training
4. Candidate embeddings creation
5. Inference pipeline deployment
6. Materialization job scheduling

## Running Individual Components

Each component can be run separately:

1. **Feature Engineering**
   ```bash
   make feature-engineering
   ```
   View results in [Hopsworks](https://rebrand.ly/serverless-github): **Feature Store → Feature Groups**

2. **Retrieval Model Training**
   ```bash
   make train-retrieval
   ```
   View results in [Hopsworks](https://rebrand.ly/serverless-github): **Data Science → Model Registry**

3. **Ranking Model Training**
   ```bash
   make train-ranking
   ```
   View results in [Hopsworks](https://rebrand.ly/serverless-github): **Data Science → Model Registry**

4. **Embeddings Creation**
   ```bash
   make create-embeddings
   ```
   View results in [Hopsworks](https://rebrand.ly/serverless-github): **Feature Store → Feature Groups**

5. **Deployment Creation**
   ```bash
   make create-deployments
   ```
   View results in [Hopsworks](https://rebrand.ly/serverless-github): **Data Science → Deployments**

6. **Materialization Job Scheduling**
   ```bash
   make schedule-materialization-jobs
   ```
   View results in [Hopsworks](https://rebrand.ly/serverless-github): **Compute → Ingestions**

## Important Notes
- All notebooks are executed using IPython through the UV virtual environment
- Components should be run in the specified order when executing individually
- Ensure UV is properly installed and configured before running any commands

# Additional Operations

## Launch Frontend Application
Start the Streamlit UI that interfaces with [Hopsworks](https://rebrand.ly/serverless-github):
```bash
make start-ui
```

## Clean Up Resources
Remove all created resources from [Hopsworks](https://rebrand.ly/serverless-github):
```bash
make clean-hopsworks-resources
```
