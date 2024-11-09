# Dependencies

- [Python v3.11](https://www.python.org/downloads/)
- [uv v0.4.30](https://github.com/astral-sh/uv)
- [GNU Make 3.81](https://www.gnu.org/software/make/)

## Cloud Dependencies

- [Hopsworks](https://www.hopsworks.ai/): Create an account an generate an API key. We will stick to their freemium plan.

# Install

To set up the project environment:

```bash
make install
```

This will:
- Create a virtual environment using `uv`
- Activate the virtual environment
- Install all dependencies including extras from `pyproject.toml`

# Usage

## Pipeline Components

The project consists of several pipeline components that can be run individually or all at once.

### Running the Complete Pipeline

To run all pipeline components in sequence:
```bash
make all
```

This will execute the following steps in order:
1. Feature Engineering
2. Retrieval Model Training
3. Embeddings Creation
4. Ranking Model Training
5. Deployment Creation

### Individual Pipeline Components

You can also run each component separately:

1. **Feature Engineering**
   ```bash
   make feature-engineering
   ```
   Executes the feature engineering notebook (`notebooks/1_feature_engineering.ipynb`)

2. **Train Retrieval Model**
   ```bash
   make train-retrieval
   ```
   Trains the retrieval model using `notebooks/2_train_retrieval_model.ipynb`

3. **Create Embeddings**
   ```bash
   make create-embeddings
   ```
   Generates embeddings using `notebooks/3_embeddings_creation.ipynb`

4. **Train Ranking Model**
   ```bash
   make train-ranking
   ```
   Trains the ranking model using `notebooks/4_train_ranking_model.ipynb`

5. **Create Deployments**
   ```bash
   make create-deployments
   ```
   Sets up model deployments using `notebooks/5_create_deployments.ipynb`

### Notes
- All notebooks are executed using IPython through the UV virtual environment
- Make sure you have UV installed and properly configured before running the pipelines
- The pipelines should be run in the specified order when executing individually

## Run Streamlit app

To launch the Streamlit application that uses the feature store and fine-tuned models, run:

```bash
make run-app
```

## Clean Hopsworks resources

```bash
make clean-hopsworks-resources
```