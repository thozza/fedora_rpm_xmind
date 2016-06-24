set -eux
xhost +
docker build --build-arg USER_ID="$(id -u)" --tag=xmind .
docker rename xmind xmind-$(date +%d%m%Y-%H%m%S) || :
# machine-id is required for dbus
docker run \
    -ti \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=":0" \
    -e XAUTHORITY=/.Xauthority \
    -v ~/.Xauthority:/.Xauthority:ro \
    -v ~/:/home/xmind:rw \
    -v /etc/machine-id:/etc/machine-id \
    --name xmind \
    xmind
