#!/bin/sh
XMIND_CONFIG="${XDG_CONFIG_HOME:-$HOME/.config}/xmind"
if [ ! -d "$XMIND_CONFIG" ]; then
    install -d "$XMIND_CONFIG"
    cp -r -a /usr/share/xmind/configuration/* "$XMIND_CONFIG"
fi
/usr/share/xmind/XMind -configuration $XMIND_CONFIG -data $XMIND_CONFIG "$@"
