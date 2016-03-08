docker run \
    -ti \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=":0" \
    -e XAUTHORITY=/.Xauthority \
    -v ~/.Xauthority:/.Xauthority:ro \
    --name xmind \
    -u root \
    xmind bash
