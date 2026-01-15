#!/bin/bash

sudo systemctl enable graphical.target --force
sudo systemctl set-default graphical.target
sudo reboot -h now

