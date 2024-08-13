import mlflow

# experiment = mlflow.create_experiment("Logarithm amounts")
mlflow.get_experiment_by_name("Logarithm amounts")
mlflow.set_experiment(experiment_id=experiment.experiment_id)

with mlflow.start_run(run_name = "Initial try") as run:
    print(run.info)
    mlflow.log_param("Key", "Value")
    mlflow.log_param("Key2", "Value2")

    