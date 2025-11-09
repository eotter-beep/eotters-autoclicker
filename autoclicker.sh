#!/bin/bash

# Simple autoclicker using xdotool
# Press Ctrl+C to stop

echo "Starting autoclicker... (Ctrl+C to stop)"

while true; do
  xdotool click 1   # left-click
  sleep 0.1
done
