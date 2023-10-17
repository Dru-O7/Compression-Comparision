import subprocess

# Input and output file paths
input_file = "inputvid.mp4"
output_file = "output_vp9.mp4"

# FFmpeg command for H.264 compression
ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_file,
    "-c:v", "libvpx-vp9",  # Use libx264 codec for H.264 compression
    "-crf", "30",       # Adjust the Constant Rate Factor (CRF) for quality (0-51, lower is higher quality)
    output_file
]

# Run FFmpeg command
try:
    subprocess.run(ffmpeg_cmd, check=True)
    print("Compression completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")