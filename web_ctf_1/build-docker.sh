#!/bin/bash
docker rm -f web_gunhead
docker build -t web_gunhead .
docker run --name=web_gunhead --rm -p 80:80 -it web_gunhead