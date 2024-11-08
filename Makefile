install:
	# uv venv
	# source .venv/bin/activate
	# uv python install
	uv pip install --all-extras --requirement pyproject.toml

run-app:
	uv run python -m streamlit run tools/6_inference_and_ui.py

clean-hopsworks-resources:
	uv run python tools/clean_hopsworks_resources.py