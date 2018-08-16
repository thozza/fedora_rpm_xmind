#!/bin/sh

usage() {
    EXIT_VAL="${1:-0}"
    echo "Simple script to build SRPM and/or also RPM for XMind"
    echo "-o/--outdir <outdir>  Where to put resulting SRPM and RPMs (defaults to './results/')"
    echo "--no-rpm              Don't build RPMs, only SRPM"
    echo "-h/--help             Show this help"
    exit "$EXIT_VAL"
}


PARAMS="$(getopt -o o:h -l outdir:,help,no-rpm --name "$0" -- "$@")"

if [ $? -ne 0 ]
then
    usage 1
fi

eval set -- "$PARAMS"
unset PARAMS

RESULT_DIR="$(pwd)/results"
BUILD_RPM=1

while true
do
    case $1 in
        -o|--outdir)
            RESULT_DIR="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        --no-rpm)
            BUILD_RPM=0
            shift
            ;;
        --)
            shift
            break
            ;;
        *)
            usage
            ;;
    esac
done

if [ -d "$RESULT_DIR" ]; then
    rm -rf "$RESULT_DIR"
fi
mkdir "$RESULT_DIR"

# check if the source is downloaded
SOURCE_LINK=$(rpmspec -P xmind.spec | grep Source0 | sed -E "s/Source0:[[:space:]]*(.*)/\1/g")
SOURCE_FILE=$(echo "$SOURCE_LINK" | sed -E "s/.*\/(.*)/\1/g")
if [ ! -f "$SOURCE_FILE" ]; then
    echo "'$SOURCE_FILE' not found -> downloading..."
    echo
    wget --user-agent="Mozilla/5.0" "$SOURCE_LINK"
fi

echo "Building SRPM..."
SRPM=$(rpmbuild -bs xmind.spec --define "_sourcedir $(pwd)" --define "_srcrpmdir $RESULT_DIR" | sed -E "s/Wrote: (.*)/\1/g")
echo
echo "SRPM is written in $RESULT_DIR"

if [ "$BUILD_RPM" -eq 1 ]; then
    echo "Building RPMs using mock..."
    mock --rebuild "$SRPM" --resultdir="$RESULT_DIR"
    echo
    echo "SRPM is written in $RESULT_DIR"
fi
