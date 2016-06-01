set -x
xhost +
docker build --build-arg USER_ID="$(id -u)" --tag=xmind .
docker rename xmind xmind-$(date +%d%m%Y-%H%m%S) || :
docker run \
    -ti \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=":0" \
    -e XAUTHORITY=/.Xauthority \
    -v ~/.Xauthority:/.Xauthority:ro \
    -v ~/:/home/xmind:rw \
    --name xmind \
    xmind
