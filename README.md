# lab2_mothmanu

ALU Transcript Generator, Lab 2 for *Introduction to Python Programming and Databases* (BSE Year 1, Trimester 2), African Leadership University.

The project has two parts:

- **`grade-evaluator.py`** reads a student's course grades from a CSV file, validates them, calculates the final GPA, decides whether the student PASSED or FAILED, and lists any formative assignments available for resubmission.
- **`organizer.sh`** archives the grades file with a timestamp, creates a fresh empty `grades.csv`, and records what it did in a log.

## Files

| File | Purpose |
|---|---|
| `grade-evaluator.py` | Python program that validates the grades and prints the transcript |
| `organizer.sh` | Bash script that archives `grades.csv` and logs the action |
| `grades.csv` | Sample course grades used as input |
| `README.md` | This file |

## Requirements

- Python 3, using only the standard library (`csv`, `sys`, `os`)
- Bash
- Tested on Ubuntu under WSL

## How to run

### Grade evaluator

```bash
python3 grade-evaluator.py
```

The program asks for a filename:

```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

### Organizer

```bash
bash organizer.sh
```

Run it with `bash` as shown, because the file is not marked as executable in the repository.

## CSV format

The file must have a header row with these four columns:

| Column | Meaning |
|---|---|
| `assignment` | Name of the assignment |
| `group` | `Formative` or `Summative` |
| `score` | The student's score, from 0 to 100 |
| `weight` | The assignment's weight in the course |

The weights must add up to **100** in total: **60** for Formative and **40** for Summative.

Example:

```
assignment,group,score,weight
Quiz,Formative,85,20
Midterm Project - Simple Calculator,Summative,70,20
```

## How the result is calculated

- **Weighted score** of each assignment: `score × weight / 100`
- **Category totals:** the weighted scores added up separately for Formative (out of 60) and Summative (out of 40)
- **GPA:** `(total weighted score / 100) × 5.0`
- **Status:** `PASSED` only if the student scores at least 50% of the weight in **both** categories, that is at least 30/60 Formative **and** at least 20/40 Summative. Falling below in either category gives `FAILED`.
- **Resubmission:** a formative assignment with a score below 50 counts as failed. Of the failed formatives, the one with the highest weight is available for resubmission. If several are tied for the highest weight, all of them are listed. If there are none, the program prints `None`.

## Example output

Using the `grades.csv` in this repository:

```
--- Processing Grades ---
Formatives (60): 34.00
Summatives (40): 26.00
GPA: 3.0000
Status: PASSED
Available for resubmission: Group Exercise, Functions and Debugging Lab
```

Group Exercise (40) and Functions and Debugging Lab (45) are both failed formatives with the same weight (20), so both are listed.

## Error handling

The program never shows a Python traceback. Invalid input produces a clear message and the program stops (exit code 1). It reports every problem it finds in a check before stopping.

| Problem | Example message |
|---|---|
| File not found | `Error: The file 'grades.csv' was not found.` |
| Empty file, or header only | `The grades file is empty.` |
| Missing or misspelt column | `The file is missing the 'assignment' column.` |
| Non-numeric or empty score or weight | `Line 2 (Quiz): score 'abc' or weight '20' is not a number.` |
| Score outside 0 to 100 | `The Quiz assignment has an invalid score of 150.0. Scores must be between 0 and 100.` |
| Unknown group | `The Bonus assignment has an unknown group Other. Groups must be Formative or Summative.` |
| Category weights wrong | `Formative weights do not add up to 60. They add up to 70.0.` |
| Total weight wrong | `Assignment weights must add up to 100. They add up to 110.0.` |

Fully blank lines in the CSV are skipped.

## What `organizer.sh` does

1. Stops with `There is no grades.csv file.` if `grades.csv` does not exist.
2. Creates an `archive` folder if one does not already exist.
3. Moves `grades.csv` into `archive/`, renamed with a timestamp in the format `grades_YYYYMMDD-HHMMSS.csv`.
4. Creates a new, empty `grades.csv`.
5. Appends a line to `organizer.log`. Entries build up across runs and are never overwritten. Example:

```
20261117-184836 grades.csv archived in archive/grades_20261117-184836.csv
```

**Note:** after running `organizer.sh`, `grades.csv` is empty, so running the evaluator prints `The grades file is empty.` To restore the data, copy the archived file back:

```bash
cp archive/grades_YYYYMMDD-HHMMSS.csv grades.csv
```

## Author

Obichukwu Nwosu 

GitHub: [mothmanu](https://github.com/mothmanu)
