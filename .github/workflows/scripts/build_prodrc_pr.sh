#! /usr/bin/env bash

export MY_ORG=$(echo "${GITHUB_REPOSITORY}" | awk -F / '{print $1}')
export MY_APP=$(echo "${GITHUB_REPOSITORY}" | awk -F / '{print tolower($2)}')
export DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
export BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
export COMMIT=$(echo "$SHA" | cut -c -7)

docker login -u "$DOCKER_ACTOR" -p "$DOCKER_TOKEN" ghcr.io
docker build --build-arg BUILD_DATE="$DATE" \
             --build-arg COMMIT="$COMMIT" \
             --build-arg BRANCH="$GITHUB_HEAD_REF" \
             --build-arg PULL_REQUEST="$PR" \
             --label us.kbase.vcs-pull-req="$PR" \
             -t ghcr.io/"$MY_ORG"/"$MY_APP":"pr-""$PR" .
docker push ghcr.io/"$MY_ORG"/"$MY_APP":"pr-""$PR"
