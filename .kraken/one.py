def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "mlflow-stock-market",
            "timeout": 2600,
            "steps": [{
                "tool": "git",
                "checkout": "https://github.com/Kraken-CI/mlflow-example.git"
            }, {
                "tool": "shell",
                "cmd": "/opt/conda/bin/mlflow run .",
                "cwd": "mlflow-example",
                "timeout": 1200
            }, {
                "tool": "values_collect",
                "files": [{
                    "name": "metrics.json",
                    "namespace": "metrics"
                }, {
                    "name": "params.json",
                    "namespace": "params"
                }],
                "cwd": "mlflow-example"
            }],
            "environments": [{
                "system": "krakenci/mlflow",
                "executor": "docker",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
