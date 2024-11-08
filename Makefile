install:
	# uv venv
	# source .venv/bin/activate
	uv python install
	uv pip install --all-extras --requirement pyproject.toml

clean-hopsworks-resources:
	uv run python tools/clean_hopsworks_resources.py