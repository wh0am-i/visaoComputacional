#!/bin/bash

sudo docker run -it \
  -p 8080:8080 \
  --ipc=host \
  --runtime=nvidia \
  --device /dev/video0:/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /usr/src/app:/usr/src/app \
  container_teste_yolo


