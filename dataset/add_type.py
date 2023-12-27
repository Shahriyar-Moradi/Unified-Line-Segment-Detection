import json
import os
import glob

# Path to the directory containing JSON files
json_directory = '/home/mora_sh/Unified-Line-Segment-Detection/dataset/dop_raw'  # Replace with your JSON directory path

# Gather list of JSON files
json_files = glob.glob(os.path.join(json_directory, '*.json'))

# Process each JSON file
for json_file in json_files:
    # Read the existing data from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Check if the data is a list
    if isinstance(data, list):
        # Iterate over each item in the list (assuming each item is a dictionary)
        for item in data:
            item['type'] = 'pinhole'
    else:
        # If the data is a dictionary, add the key-value pair directly
        data['type'] = 'pinhole'

    # Write the modified data back to the JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

print(f"'type': 'pinhole' has been added to all JSON files in {json_directory}.")