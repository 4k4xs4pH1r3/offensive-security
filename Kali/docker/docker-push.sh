#!/bin/sh

set -e

DISTRO=$1

# Retrieve variables from former docker-build.sh
. ./$DISTRO.conf

# $CI_REGISTRY_IMAGE/$IMAGE:$VERSION has been built by docker-build.sh

# Overwrite the "latest" version too
if [ -n "$CI_JOB_TOKEN" ]; then
    docker pull $CI_REGISTRY_IMAGE/$IMAGE:$VERSION
fi
docker tag $CI_REGISTRY_IMAGE/$IMAGE:$VERSION $CI_REGISTRY_IMAGE/$IMAGE:latest

# Try to push tags
if [ -n "$CI_JOB_TOKEN" ]; then
    # In GitLab, push must work !
    docker push $CI_REGISTRY_IMAGE/$IMAGE:$VERSION
    docker push $CI_REGISTRY_IMAGE/$IMAGE:latest
else
    echo "Trying to push to $CI_REGISTRY_IMAGE ... might fail if not logged in"
    docker push $CI_REGISTRY_IMAGE/$IMAGE:$VERSION || true
    docker push $CI_REGISTRY_IMAGE/$IMAGE:latest || true
fi
