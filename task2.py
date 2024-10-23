import random
import string
from collections import defaultdict


# Step 1: Create a list of random number of dictionaries (from 2 to 10)
def generate_random_dicts():
    # Generate a random number of dictionaries between 2 and 10
    num_dicts = random.randint(2, 10)
    list_of_dicts = []

    for i in range(num_dicts):
        # Generate a random number of keys for each dictionary (letters from 'a' to 'z')
        num_keys = random.randint(1, 5)  # Random number of keys between 1 and 5
        keys = random.sample(string.ascii_lowercase, num_keys)

        # Generate random values for each key (0-100)
        random_dict = {key: random.randint(0, 100) for key in keys}

        # Append the generated dictionary to the list
        list_of_dicts.append(random_dict)

    return list_of_dicts


# Step 2: Merge the list of dictionaries
def merge_dicts(list_of_dicts):
    merged_dict = {}
    key_max_dict = defaultdict(list)

    # Iterate over each dictionary and find the max value for each key across dictionaries
    for i, d in enumerate(list_of_dicts):
        for key, value in d.items():
            key_max_dict[key].append((value, i + 1))  # Track the value and dict index (i+1)

    # Now, build the final merged dictionary
    for key, value_list in key_max_dict.items():
        if len(value_list) == 1:
            # If key exists in only one dictionary, take it as is
            merged_dict[key] = value_list[0][0]
        else:
            # If the key exists in multiple dictionaries, take the max value
            max_value, dict_index = max(value_list)
            # Rename the key to include the dict number with the max value
            merged_dict[f"{key}_{dict_index}"] = max_value

    return merged_dict


# Main script
if __name__ == "__main__":
    # Generate random dictionaries
    random_dicts = generate_random_dicts()

    # Print generated list of dicts
    print("Generated list of dicts:")
    for d in random_dicts:
        print(d)

    # Merge dictionaries
    merged = merge_dicts(random_dicts)

    # Print merged dictionary
    print("Merged dictionary:")
    print(merged)
