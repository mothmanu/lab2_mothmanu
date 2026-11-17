#!/bin/bash
# A check that grades.csv exists
if [ ! -f "grades.csv" ]; then
    echo "There is no grades.csv file."
    exit 1
fi

# The timestamp stored in a variable
now=$(date +%Y%m%d-%H%M%S)

# The archived filename built from the timestamp
file_name="grades_${now}.csv"

# Create the archive folder if it doesn't exist
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Archiving the grades.csv file
mv grades.csv archive/"${file_name}"

# Creating a new empty file
touch grades.csv

# Create a log entry
echo "${now} grades.csv archived in archive/${file_name}" >> organizer.log
