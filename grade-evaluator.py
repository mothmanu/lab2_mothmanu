import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    score_error = False
    # Check if the grades file is empty
    if not data:
        print("The grades file is empty.")
        score_error = True

    # Check if all scores are percentage based (0-100)
    for assignment in data:
        if assignment['score'] < 0 or assignment['score'] > 100:
            print(f"The {assignment['assignment']} assignment has "
                  f"an invalid score of {assignment['score']}. "
                  "Scores must be between 0 and 100.")
            score_error = True

    if score_error:
        sys.exit(1)

    # Validate total weights (Total=100, Summative=40, Formative=60)
    weight_error = False
    formative_total = 0
    summative_total = 0
    weight_total = 0
    for assignment in data:
        weight_total += assignment['weight']
        if assignment['group'] == 'Formative':
            formative_total += assignment['weight']
        elif assignment['group'] == 'Summative':
            summative_total += assignment['weight']
        else:
            print(f"The {assignment['assignment']} assignment has an unknown "
                  f"group {assignment['group']}. Groups must be "
                  "Formative or Summative.")
            weight_error = True

    if formative_total != 60.0:
        print("Formative weights do not add up to 60. They "
              f"add up to {formative_total}.")
        weight_error = True

    if summative_total != 40.0:
        print("Summative weights do not add up to 40. They "
              f"add up to {summative_total}.")
        weight_error = True

    if weight_total != 100.0:
        print("Assignment weights must add up to 100. They "
              f"add up to {weight_total}.")
        weight_error = True

    if weight_error:
        sys.exit(1)

    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    pass


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
    