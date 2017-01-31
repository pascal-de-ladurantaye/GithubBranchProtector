# Github Branch Protector
A small webhook server that return a success status based on the branch the commit is on.

Make sure you copy `configs.py.template` to `configs.py` and adjust the settings to your liking.

Start by running `run_prod.sh` using screen or nohup if deploying on a remote server to prevent shutting down server when disconnecting from the shell. This will also setup a virtual environment and install dependencies.

If running locally, either launch with `run.sh` which uses Gunicorn or lauch through `main.py` for a simple blocking server.
## Contributing
Issues and feature requests are welcomed. Will also accept pull requests.
