A simple shell script to create .m3u playlists for use with mpv etc.

Running this script will create m3u playlists for the base directory
as well as all of its sub-directories so the user requires write
permission for every directory to be playlisted.

## USAGE

You should only use it with dirs of video, audio and image files.

I copy the script into my $PATH as **pc** like so:

```
 $ sudo cp playlist_creator.sh /usr/local/bin/pc
```

Then when I want to generate a playlist, I **cd** into the top level
directory that I want to recursively generate playlists for and run:

```
 $ pc .
```
