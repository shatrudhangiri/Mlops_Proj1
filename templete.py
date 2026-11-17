
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

project_name = "src"


list_of_files =[

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/feature_engineering.py",
    f"{project_name}/compoentns/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongodb_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_database.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/finance_data.py",
    f"{project_name}/constants/__init__.py",
    f'{project_name}/entity/__init__.py'
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/enity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:

    filepath = BASE_DIR / filepath

    filepath.parent.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        filepath.touch()
        print(f"Created: {filepath}")
    else:
        print(f"Already exists: {filepath}")

print("\nProject structure created successfully!")



