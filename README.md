<div align="center">
  <h1>Hands-on H&M Real-Time Personalized Recommender</h1>
  <p class="tagline">Open source course by <a href="https://decodingml.substack.com">Decoding ML</a> in collaboration with <a href="https://rebrand.ly/homepage-github">Hopsworks</a></p>
</div>
</br>

<p align="center">
  <a href="https://decodingml.substack.com/p/33d3273e-b8e3-4d98-b160-c3d239343022">
    <img src="assets/architecture.png" alt="Architecture" width="600">
  </a>
</p>

## What will you learn?

The goal of this course is to teach you how to build and deploy a real-time personalized recommender for H&M fashion articles, going through:

- 4-stage recommender architecture
- Two-tower model training
- Scalable ML system design
- MLOps best practices
- Real-time deployment
- LLM-enhanced recommendations
- Interactive web interface

## Who is this for?

ML/AI engineers looking to understand how to design, build and deploy real-time personalized recommenders. Also, it is a good fit for DE/DS/SWE who want to understand the engineering behind a recommender.

This is NOT a course for data scientists or researchers showing how to train the most accurate models. This course will focus mostly on engineering and end-to-end system using MLOps best practices.

## Costs?

The lessons are completely free. Also, we will stick to the free version of all the tools used throughout the course.

The only thing that will cost you ~$1-2 is running the latest lesson on building recommenders with LLMs where we will use the OpenAI API. 

To conclude, Lesson 1,2,3, and 4 are free and Lesson 5 will cost you ~$1-2, which you can choose not to run.

## How will you learn?

This is a self-paced course where we provide 5 lessons, which will go over the theory, system design and implementation of building a real-time personalized recommender. Everything is backed by the open-source code found in this repository.

## Lessons

| Lesson | Title | Description | Local Notebooks | Colab Notebooks |
|--------|-------|-------------|----------------|-----------------|
| 1 | [Building a TikTok-like recommender](https://decodingml.substack.com/p/33d3273e-b8e3-4d98-b160-c3d239343022) | Learn how to architect a recommender system using the 4-stage architecture and two-tower model. | **No code** | **No code** |
| 2 | The feature pipeline | Learn how to build a scalable feature pipeline (WIP) | * [1_fp_computing_features.ipynb](notebooks/1_fp_computing_features.ipynb) | - |
| 3 | The training pipeline | Learn how to train and evaluate recommendation models (WIP) | * [2_tp_training_retrieval_model.ipynb](notebooks/2_tp_training_retrieval_model.ipynb) *  [3_tp_training_ranking_model.ipynb](notebooks/3_tp_training_ranking_model.ipynb) | - |
| 4 | The inference pipeline | Learn how to deploy models for real-time inference (WIP) | * [4_ip_computing_item_embeddings.ipynb](notebooks/4_ip_computing_item_embeddings.ipynb) * [5_ip_creating_deployments.ipynb](notebooks/5_ip_creating_deployments.ipynb) * [6_scheduling_materialization_jobs.ipynb](notebooks/6_scheduling_materialization_jobs.ipynb) | - |
| 5 | Building personalized real-time recommenders with LLMs | Learn how to enhance recommendations with LLMs (WIP) | - | - |


## Project structure

At Decoding ML we teach how to build production ML systems, thus the course follows the structure of a real-world Python project:

```bash
.
├── notebooks/          # Jupyter notebooks for each pipeline
├── recsys/             # Core recommender system package
│   ├── config.py       # Configuration and settings
│   ...
│   └── training/       # Training pipelines code
├── tools/              # Utility scripts
├── tests/              # Unit and integration tests
├── .env.example        # Example environment variables template
├── Makefile            # Build automation
├── pyproject.toml      # Project dependencies
```

## Install and usage

To understand how to install and run the code, go to the [INSTALL_AND_USAGE](https://github.com/decodingml/hands-on-personalized-recommender/blob/main/INSTALL_AND_USAGE.md) dedicated document.

> [!Note]
> Even though you can run everything solely using the INSTALL_AND_USAGE dedicated document, we recommend that you read the articles to understand how the personalized recommender works fully.

## Questions and troubleshooting

Please ask us any questions if anything gets confusing while studying the articles or running the code.

You can `ask any question` by `opening an issue` in this GitHub repository by clicking [here](https://github.com/decodingml/hands-on-personalized-recommender/issues).

## Sponsors

<table>
  <tr>
    <td align="center">
      <a href="https://rebrand.ly/homepage-github" target="_blank">Hopsworks</a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://rebrand.ly/homepage-github" target="_blank">
        <img src="assets/hopsworks.png" width="150" alt="Hopsworks">
      </a>
    </td>
  </tr>
</table>


## License

This course is an open-source project released under the Apache-2.0 license. Thus, as long you distribute our LICENSE and acknowledge your project is based on our work, you can safely clone or fork this project and use it as a source of inspiration for your educational projects (e.g., university, college degree, personal projects, etc.).
