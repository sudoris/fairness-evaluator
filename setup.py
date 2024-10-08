import pathlib

from setuptools import find_packages, setup

setup(
  name="fairness-evaluator",
  version="0.0.1",
  description="A fairness evaluation plugin for MLflow",
  packages=find_packages(),
  # Require MLflow as a dependency of the plugin, so that plugin users can simply install
  # the plugin & then immediately use it with MLflow
  install_requires=["mlflow"],
  python_requires=">=3.9, <3.12",
  entry_points={
    # Define a MLflow model evaluator with name "fairness_evaluator"
    "mlflow.model_evaluator": (
        "fairness_evaluator=fairness_evaluator.src.fairness_evaluator:FairnessEvaluator"
    )     
  }
)