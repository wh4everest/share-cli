# Share CLI

A simple way to share files from the terminal.

## Usage

```
> share ~/Downloads/my-file.txt
URL: https://share-cli.andrejt.com/b4ff4Sd-my-file.txt
```

## Install

Ubuntu

```
sudo apt-add-repository http://share-cli-ubuntu.andrejt.com/
sudo apt-get update
sudo apt-get install share
```

## Running the server

```
cd server/
pip install flask
export FLASK_APP=server.py
python -m flask run
```