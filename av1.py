import subprocess

input_file = "inputvid.mp4"   
output_file = "output_av1.mkv"  # Using MKV container

# FFmpeg command to compress using AV1 codec and MKV container
ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_file,
    "-c:v", "libaom-av1",  # Use the AV1 codec
    "-strict", "experimental",  # Enable experimental codecs
    "-b:v", "500k",  # Set the video bitrate (adjust as needed)
    output_file
]

# Run FFmpeg command
try:
    subprocess.run(ffmpeg_cmd, check=True)
    print("Compression completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

