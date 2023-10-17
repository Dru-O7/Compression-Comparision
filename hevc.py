import subprocess

input_file = "inputvid.mp4"   # Replace with your input video file
output_file = "output_hevc.mp4"  # Replace with your desired output file

# FFmpeg command to compress using Xvid codec
ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_file,
    "-c:v", "libx265",
    "-q:v", "31",  # Adjust the video quality (1-31, lower is better quality)
    output_file
]

# Run FFmpeg command
try:
    subprocess.run(ffmpeg_cmd, check=True)
    print("Compression completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
