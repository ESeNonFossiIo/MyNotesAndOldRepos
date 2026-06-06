#!/bin/bash


echo "OLD tag",$1
OLD=${1}
echo "NEW tag",$2
NEW=${2}
git tag ${NEW} ${OLD}
git tag -d ${OLD}
git push origin :refs/tags/${OLD}
git push --tags
