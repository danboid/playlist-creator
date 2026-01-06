#!/bin/sh
# m3u playlist generator shell script
# Generates playlists for use with media players such as mpv

# Run it within dirs containing video, audio or image files only!
# Adding filetype filters notably slows the process down so all files are included.

# playlist-creator defaults to working from your present workibg directory.

BASEDIR="${1:-.}"
cd "$BASEDIR" || exit 1
BASEDIR=$(pwd)

# Remove existing playlists

find . -name '*.m3u'|sed -e "s/^/\"/"|sed -e "s/$/\"/"|xargs rm -f

find . -type d |sort| while read -r DIR; do
      cd "$BASEDIR/$DIR" || exit 1
      find . -type f | grep -v m3u | sort> '00-Playlist.m3u'
done

