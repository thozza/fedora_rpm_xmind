#!/bin/sh

# check if the source is downloaded
SOURCE_LINK=$(rpmspec -P xmind.spec | grep Source0 | sed -E "s/Source0:[[:space:]]*(.*)/\1/g")
SOURCE_FILE=$(echo $SOURCE_LINK | sed -E "s/.*\/(.*)/\1/g")
if [ ! -f $SOURCE_FILE ]; then
    echo "'$SOURCE_FILE' not found -> downloading..."
    echo
    wget --user-agent="Mozilla/5.0" $SOURCE_LINK
fi

rpmbuild -bb xmind.spec --define "_sourcedir `pwd`" --define "_srcrpmdir `pwd`"
