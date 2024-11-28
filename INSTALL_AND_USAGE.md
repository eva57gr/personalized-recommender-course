# Dependencies

- [Python v3.11](https://www.python.org/downloads/)
- [uv v0.4.30](https://github.com/astral-sh/uv)
- [GNU Make 3.81](https://www.gnu.org/software/make/)

## Cloud Dependencies

| Cloud dependency | Tool type | Description | Costs | Env Vars |
|-----------------|-----------|-------------|--------|-----------|
| [Hopsworks](https://rebrand.ly/serverless-github) | AI Lakehouse | Serverless AI Lakehouse used for its feature store, model registry and model serving | Free tier available: 0 costs to run the course | `HOPSWORKS_API_KEY` |
| [OpenAI API](https://openai.com/index/openai-api/) | LLM API | API access to OpenAI's language models used to build the LLM recommender | Pay-per-use | `OPENAI_API_KEY`, `OPENAI_MODEL_ID` |

# Install

To set up the project environment:

```bash
make install
```

This will:
- Create a virtual environment using `uv`
- Activate the virtual environment
- Install all dependencies from `pyproject.toml`

# Usage

## Set environment variables

The first step before running anything is to set up the environment variables required to access Hopsworks and OpenAI's API.

Go to the root of the repository and run:
```bash
cp .env.example .env
```

Open your `.env` file and fill it as explain in the comments.

## Pipeline components

The project consists of several pipeline components that can be run individually or all at once.

### Running all the pipelines at once

To run all the pipeline at once in a sequence, run:
```bash
make all
```

This will execute all the ML pipelines in the following order:
1. Feature engineering
2. Training the retrieval model 
3. Training the ranking model
4. Creating the candidate embeddings
5. Deploying the inference pipeline
6. Scheduling the materialization jobs

### Individual Pipeline Components

You can also run each component separately:

### Individual Pipeline Components

1. **Feature Engineering**
   Execute the feature engineering Notebook (`notebooks/1_fp_computing_features.ipynb`):
   ```bash
   make feature-engineering
   ```

2. **Train Retrieval Model**
   Execute the retrieval model training Notebook (`notebooks/2_tp_training_retrieval_model.ipynb`):
   ```bash
   make train-retrieval
   ```

3. **Train Ranking Model**
   Execute the ranking model training Notebook (`notebooks/3_tp_training_ranking_model.ipynb`):
   ```bash
   make train-ranking
   ```

4. **Create Embeddings**
   Execute the embeddings computation Notebook (`notebooks/4_ip_computing_item_embeddings.ipynb`):
   ```bash
   make create-embeddings
   ```

5. **Create Deployments**
   Execute the deployments creation Notebook (`notebooks/5_ip_creating_deployments.ipynb`):
   ```bash
   make create-deployments
   ```

6. **Schedule Materialization Jobs**
   Execute the materialization jobs scheduling Notebook (`notebooks/6_scheduling_materialization_jobs.ipynb`):
   ```bash
   make schedule-materialization-jobs
   ```

### Notes
- All notebooks are executed using IPython through the UV virtual environment
- Make sure you have UV installed and properly configured before running the pipelines
- The pipelines should be run in the specified order when executing individually

## Run Streamlit app

To launch the Streamlit frontend application that uses the feature store and fine-tuned models, run:

```bash
make start-ui
```

## Clean Hopsworks resources

To clean all 

```bash
make clean-hopsworks-resources
```