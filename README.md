# beneath-stream

## Installing the SDK and Setup

First, create a secret in the Console. Then:
- `xcode-select --install`: on MacOS, to avoid the error documented in `beneath_sdk_error.txt`
- `pip3 install -r requirements.txt`
- `beneath auth [YOUR_SECRET]`. NOTE: This is needed for the CLI, but a secret can be passed in with the Python SDK.

Further setup:
- Create a `.env` file copying `secrets_example.env`, updating to your Beneath secret.

## Suggestions

- Schema for stream to be an object of some sort instead of string; a string might be more prone to types or syntax errors.

## Issues

- On MacOS, need to run `xcode-select --install` to avoid the error documented in `beneath_sdk_error.txt`
- When creating a project from the commandline, ran into error documented in `cli_create_project_error.txt`. Got around this by creating a project directly in the Console.
