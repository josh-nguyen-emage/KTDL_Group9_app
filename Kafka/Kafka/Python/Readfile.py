import os
import time

def add2files(new_file_path, file1_path, file2_path):
    # Read contents of file 1
    with open(file1_path, 'r') as file1:
        file1_content = file1.read()
    
    # Read contents of file 2
    with open(file2_path, 'r') as file2:
        file2_content = file2.read()
    
    # Combine contents of both files
    combined_content = file1_content + "\n" + file2_content
    with open(new_file_path, 'w'):
        pass  # Doing nothing effectively clears the file
    # Write combined content to new file
    with open(new_file_path, 'w') as new_file:
        new_file.write(combined_content)

# def operate_file(new_file_path):
#     # with open(new_file_path, 'w'):
#     #     pass  # Doing nothing effectively clears the file
#     with open(new_file_path, 'w') as new_file:
#         print(123)
#         # new_file.write(combined_content)
def get_number_from_line(line):
    try:
        return int(line.split("/")[1].split("-")[0])
    except IndexError:
        # If the line doesn't have the expected format, return a large number
        # so it appears at the end when sorted
        return float('inf')

def read_sort_and_rewrite(new_file_path, new_file_path_1):
    # Read lines from the file and store them in a list
    lines = []
    with open(new_file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    # Sort the lines based on the extracted numbers
    # lines.sort(key=lambda line: int(line.split("/")[1].split("-")[0]))
    lines.sort(key=get_number_from_line)


    # Rewrite the sorted lines back to the file
    with open(new_file_path_1, 'w') as file:
        for line in lines:
            file.write(line + "\n")

def remove_duplicate_pairs(file_path):
    pairs_seen = set()  # Set to store pairs of numbers that have been encountered
    
    # Read lines from the file and store unique pairs
    pairs_set = set()  # Set to store unique pairs of numbers
    updated_lines  = []
    with open(file_path, 'r') as file:
        for line in file:
            try:# Split the line into parts
                pair = line.split("#")[0].split("/")[1], line.split("#")[1].split("/")[1]
                # print(pair)
            except IndexError:
                # If the line doesn't have the expected format, skip it
                continue

            # Check if the pair is already in the set
            if pair in pairs_set:
                # Skip the line if the pair is already in the set
                continue

            # print(pair)
            pairs_set.add(pair)
            updated_lines.append(line)

    
    # Rewrite the unique lines back to the file
    with open(file_path, 'w') as file:
        for line in updated_lines:
            file.write(line)

def remove_duplicates_except_last_three(file_path):
    lines_dict = {}  # Dictionary to store lines with the same first number
    updated_lines = []  # List to store lines to keep

    # Read lines from the file
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the first number from the line
            first_number = line.split("/")[1].split("-")[0]

            # Add the line to the dictionary with the first number as key
            lines_dict.setdefault(first_number, []).append(line)

    # Keep only the last 3 occurrences of each first number
    for first_number, lines in lines_dict.items():
        updated_lines.extend(lines[-3:])

    # Rewrite the updated lines back to the file
    with open(file_path, 'w') as file:
        for line in updated_lines:
            file.write(line)



def Readfile_running():
    file1_path = "../Python/other_txt/shopping_bag.txt"
    file2_path = "../Python/other_txt/click.txt"
    new_file_path = "../Python/other_txt/recommendation.txt"
    new_file_path_1 = "../listener-output-log/recommendation_sort.txt"

    while True:
        # Read files and update new file
        add2files(new_file_path, file1_path, file2_path)
        print("Files updated.")
        read_sort_and_rewrite(new_file_path, new_file_path_1)
        remove_duplicate_pairs(new_file_path_1)
        remove_duplicates_except_last_three(new_file_path_1)
        
        # Wait for 1 minute
        time.sleep(60)


# if __name__ == "__main__":
#     main()