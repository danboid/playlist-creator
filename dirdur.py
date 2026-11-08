#!/usr/bin/env python3
# dirdur.py - uses ffprobe to show the combined duration of video files within a directory

import os
import sys
import subprocess

# Supported video extensions
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.m4v', '.webm', '.ts', '.m2ts'}

def get_video_duration(file_path):
    """Extracts video duration in seconds using ffprobe rapidly without decoding."""
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(result.stdout.strip())
    except (subprocess.CalledProcessError, ValueError):
        # Returns 0.0 if file is corrupted or not a valid media stream
        return 0.0

def format_time(seconds):
    """Converts total seconds into hours, minutes, and seconds."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours}h {minutes}m {secs:.2f}s"

def scan_directories(root_dir):
    grand_total_seconds = 0.0
    
    # Recursively traverse the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dir_total_seconds = 0.0
        video_count = 0
        
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in VIDEO_EXTENSIONS:
                file_path = os.path.join(dirpath, filename)
                duration = get_video_duration(file_path)
                if duration > 0:
                    dir_total_seconds += duration
                    video_count += 1
        
        # Only print directories that contain valid video files (suppresses individual file names/lengths)
        if video_count > 0:
            grand_total_seconds += dir_total_seconds
            print(f"📁 Directory: {dirpath}")
            print(f"   Videos: {video_count} | Length: {format_time(dir_total_seconds)}\n")

    print("=" * 60)
    print(f"🎉 GRAND TOTAL (Parent + All Subdirectories): {format_time(grand_total_seconds)}")
    print("=" * 60)

if __name__ == "__main__":
    # Target directory defaults to current directory if not specified
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a valid directory path.")
        sys.exit(1)
        
    print(f"Scanning '{os.path.abspath(target_dir)}' using ffprobe...\n")
    scan_directories(target_dir)
