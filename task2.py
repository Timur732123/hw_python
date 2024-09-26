import random
import string


# Step 1: Create a list of random number of dicts (between 2 and 10).
def create_random_dicts():
    num_dicts = random.randint(2, 10)  # Randomly select the number of dictionaries (between 2 and 10)
    dicts_list = []  # Initialize an empty list to hold the dictionaries

    # Loop to create each dictionary
    for _ in range(num_dicts):
        num_keys = random.randint(1, 5)  # Randomly select the number of keys in each dictionary (1 to 5)
        random_dict = {}  # Initialize an empty dictionary

        # Generate a random key-value pair for each dictionary
        for _ in range(num_keys):
            key = random.choice(string.ascii_lowercase)  # Randomly select a lowercase letter as the key
            value = random.randint(0, 100)  # Randomly select a value between 0 and 100
            random_dict[key] = value  # Add the key-value pair to the dictionary

        dicts_list.append(random_dict)  # Add the dictionary to the list of dictionaries

    return dicts_list


# Step 2: Create a common dictionary from the list of dicts.
def merge_dicts(dicts_list):
    common_dict = {}  # Initialize an empty dictionary to store the merged result

    # Iterate over each dictionary in the list
    for i, current_dict in enumerate(dicts_list):
        dict_number = i + 1  # Dictionary number (1-indexed)

        # Iterate over each key-value pair in the current dictionary
        for key, value in current_dict.items():
            # If the key already exists in the common dictionary, compare values and take the maximum
            if key in common_dict:
                if value > common_dict[key][0]:  # Compare values
                    common_dict[key] = (value, dict_number)  # Update with the higher value and dict number
            else:
                common_dict[key] = (value, dict_number)  # Add the key-value pair with the dict number

    # Create a final dictionary with updated key names (add dict number if needed)
    final_dict = {}
    for key, (value, dict_number) in common_dict.items():
        # If the key appears in more than one dictionary, rename the key by appending the dictionary number
        new_key = f"{key}_{dict_number}" if dict_number > 1 else key
        final_dict[new_key] = value

    return final_dict


# Step 3: Main function to generate random dicts and merge them
if __name__ == "__main__":
    random_dicts = create_random_dicts()  # Generate the list of random dictionaries
    print("Generated List of Dicts:")
    print(random_dicts)  # Print the generated list of dictionaries

    merged_dict = merge_dicts(random_dicts)  # Merge the dictionaries
    print("Merged Dict with Renamed Keys:")
    print(merged_dict)  # Print the merged result
