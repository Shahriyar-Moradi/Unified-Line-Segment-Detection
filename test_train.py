import json
import random

# Assuming `all_wireframe_annotations` is your list of annotations
# Load your annotations from a file if they aren't already in memory
with open('/home/mora_sh/Unified-Line-Segment-Detection/dataset/dop_raw/image/ostpark.json', 'r') as f:
    all_wireframe_annotations = json.load(f)

# Define the split ratio for train and test sets
train_ratio = 0.7

# Shuffle the annotations randomly
random.shuffle(all_wireframe_annotations)

# Calculate the split index
split_index = int(train_ratio * len(all_wireframe_annotations))

# Split the annotations into train and test sets
train_annotations = all_wireframe_annotations[:split_index]
test_annotations = all_wireframe_annotations[split_index:]

# Save the train annotations to a JSON file
with open('train_annotations.json', 'w') as f:
    json.dump(train_annotations, f, indent=4)
    
# Save the test annotations to a JSON file
with open('test_annotations.json', 'w') as f:
    json.dump(test_annotations, f, indent=4)

print(f"Annotations split into {len(train_annotations)} for training and {len(test_annotations)} for testing.")