#!/usr/bin/env bash

curl -su $USER -X POST -F "file=@$1" https://share-cli.andrejt.com
