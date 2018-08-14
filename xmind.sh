#!/bin/sh
XMIND_CONFIG="${XDG_CONFIG_HOME:-$HOME/.config}/xmind"
VERSION_FILE="${XDG_CONFIG_HOME:-$HOME/.config}/xmind/.version_file"
if [ ! -d "$XMIND_CONFIG" ]; then
    install -d "$XMIND_CONFIG"
fi
# make sure to update the config in case Xmind was updated or this is first install
if [ ! -f "$VERSION_FILE" ] || [ "$(cat "$VERSION_FILE")" != "$(rpm -q xmind)" ]; then
    cp -r -a /usr/share/xmind/configuration/* "$XMIND_CONFIG"
    rpm -q xmind > "$VERSION_FILE"
fi
exec /usr/share/xmind/XMind -configuration $XMIND_CONFIG -data $XMIND_CONFIG "$@"
