#!/bin/sh

set -e

DISTRO=$1
# Build the same version as for kali-rolling
VERSION=$(. ./kali-rolling.conf; echo $VERSION)
IMAGE=$DISTRO

docker build --pull -t $CI_REGISTRY_IMAGE/$IMAGE:$VERSION \
    --build-arg CI_REGISTRY_IMAGE=$CI_REGISTRY_IMAGE \
    --build-arg VERSION=$VERSION \
    -f extra/$IMAGE \
    .

if [ -n "$CI_JOB_TOKEN" ]; then
    # Push the image so that subsequent jobs can fetch it
    docker push $CI_REGISTRY_IMAGE/$IMAGE:$VERSION
fi

cat >$DISTRO.conf <<END
CI_REGISTRY_IMAGE="$CI_REGISTRY_IMAGE"
IMAGE="$IMAGE"
VERSION="$VERSION"
END
