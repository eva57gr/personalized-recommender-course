install:
	uv venv
	source .venv/bin/activate
	# uv python install
	uv pip install --all-extras --requirement pyproject.toml

run-app:
	uv run python -m streamlit run tools/inference_and_ui.py

clean-hopsworks-resources:
	uv run python tools/clean_hopsworks_resources.py

all: feature-engineering train-retrieval create-embeddings train-ranking create-deployments

feature-engineering:
	uv run ipython notebooks/1_feature_engineering.ipynb

train-retrieval:
	uv run ipython notebooks/2_train_retrieval_model.ipynb

create-embeddings:
	uv run ipython notebooks/3_embeddings_creation.ipynb

train-ranking:
	uv run ipython notebooks/4_train_ranking_model.ipynb

create-deployments:
	uv run ipython notebooks/5_create_deployments.ipynb