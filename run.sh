#!/bin/bash
# Name of the output file
output_file="info.txt"
# List of Python scripts to execute
python_scripts=("avi.py" "h264.py" "hevc.py" "vp9.py")

# Clear the contents of the output file or create a new one
> "$output_file"
echo "Size of inputvid.mp4 is" $(du -h inputvid.mp4 | cut -f1) >> "$output_file"
for script in "${python_scripts[@]}"; do
    echo "Running $script..."

    # Record the start time
    start_time=$(date +%s.%N)

    # Run the Python script
    python "$script"

    # Record the end time
    end_time=$(date +%s.%N)

    # Calculate the execution time
    execution_time=$(echo "$end_time - $start_time" | bc)
    # echo "Execution Time for $script: $execution_time seconds"

    echo "Execution Time for $script: $execution_time seconds" >> "$output_file"
done

output=("output_xvid.avi" "output_h264.mp4" "output_hevc.mp4" "output_vp9.mp4")

for video_file in "${output[@]}"; do
    echo "Calculating the size of $video_file..."

    # Get the size of the output video
    output_video_size=$(du -h "$video_file" | cut -f1)
    echo "Size of $video_file: $output_video_size" >> "$output_file"
done
