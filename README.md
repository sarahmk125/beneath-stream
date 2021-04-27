# Beneath SDK

This repo starts to build streaming pipelines with the [Beneath Python SDK](https://about.beneath.dev/docs/quick-starts/install-sdk/), a hosted streaming solution for data engineers and data scientists. For setup, I signed up at beneath.dev and created a secret token.

## Installing the SDK and Setup

First, create a secret in the Console. Then:
- `pip3 install -r requirements.txt`
- `beneath auth [YOUR_SECRET]`. NOTE: This is needed for the CLI, but a secret can be passed in with the Python SDK.

To run in Docker (preferred):
- `make build` then `make run`
- This puts you in bash. `cd beneath-stream` and `python main.py` runs the script.

Further setup:
- Create a `.env` file copying `secrets_example.env`, updating to your Beneath secret. NOTE: This seems to be quirky, explained below (in reference to `secrets.txt`)

## Suggestions

- Schema for stream to be an object of some sort instead of string; a string might be more prone to types or syntax errors.

## Issues

MacOS related:
- On MacOS, need to run `xcode-select --install` to avoid the error documented in `beneath_sdk_error.txt`
- When creating a project from the commandline on a Mac, ran into error documented in `cli_create_project_error.txt`. This also occurs when trying to authenticate via Python SDK. No solution found.

Running in Docker (on `ubuntu` 18.04 image):
- Running on Docker, I get the issue in `beneath_sdk_get_secret_docker.txt`. However, this is resolved by copying the `secret.txt` file to `/root/.beneath/secret.txt` in the container.
- When running the script I get `ModuleNotFoundError: No module named 'importlib_metadata'`. This is solved by installing `importlib-metadata`. This is documented in `beneath_dependency.txt`
- It's not immediately clear when I need to start the client; I run `await stream.write()` and get the Client not started error documented in `client_error.txt` - this is in the API Docs on the stream, but not in the general docs.
