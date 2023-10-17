#!/bin/bash

# Name of the output file
output_file="info.txt"

# List of Python scripts to execute
python_scripts=("avi.py" "h264.py" "hevc.py" "vp9.py")

# Clear the contents of the output file or create a new one
> "$output_file"

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
    echo "Execution Time for $script: $execution_time seconds"

    # Find and print the size of the Python script
    file_size=$(du -h "$script" | cut -f1)
    echo "File Size of $script: $file_size"

    # Append the information to the output file
    echo "Execution Time for $script: $execution_time seconds" >> "$output_file"
    echo "File Size of $script: $file_size" >> "$output_file"
done
