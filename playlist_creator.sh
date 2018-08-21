#!/bin/sh
# m3u playlist generator shell script
# Generates playlists for use with media players such as mpv
# Use with dirs containing video, audio or image files only

BASEDIR=$1
if [ -z "$BASEDIR" ]; then
      echo You must specify a base directory
      exit 1
fi

cd "$BASEDIR" || exit 1
BASEDIR=$(pwd)

# Remove existing playlists
find . -name '*.m3u'|sed -e "s/^/\"/"|sed -e "s/$/\"/"|xargs rm -f

find . -type d |sort| while read -r DIR; do
      cd "$BASEDIR/$DIR" || exit 1
      find . -type f | grep -v m3u | sort> '00-Playlist.m3u'
done

