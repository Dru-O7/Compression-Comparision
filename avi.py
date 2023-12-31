import subprocess

input_file = "inputvid.mp4"   
output_file = "output_xvid.avi"  

# FFmpeg command to compress using Xvid codec
ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_file,
    "-c:v", "libxvid",
    "-q:v", "31",  # Adjust the video quality (1-31, lower is better quality)
    output_file
]

# Run FFmpeg command
try:
    subprocess.run(ffmpeg_cmd, check=True)
    print("Compression completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")