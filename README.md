# Airflow Setup

This repo serves as a template for a local installation of Airflow.  
It has a `.devcontainer/` and `.vscode/` folders to facilitate debugging in VSCode.

It is mainly taken from the official [documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html), with a few tweaks to be able to debug locally.

```bash
# Start Airflow on your local machine
docker compose up
```

Airflow should now be running on your local machine. Head over to [http://localhost:8080/](http://localhost:8080/) and login using the username `airflow` and password `airflow`.

```bash
# Stopping and cleaning up the images
docker compose down --rmi all -v --remove-orphans
```
