import json, csv, os

from utils import *
from dotenv import load_dotenv
load_dotenv()

def main():
    row_stack = ["Bug ID", "ExceptionType", "Repair Pattern", "Buggy Lines", "Fixed Lines", "Combined Lines"]

    # Opening JSON file and loading the data
    # into the variable data
    with open(os.getenv('IMPORT')) as json_file:
        data = json.load(json_file)
    
    # now we will open a file for writing
    data_file = open(os.getenv('EXPORT'), 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0 
    
    for data in data:
        if count == 0:
            # Writing headers of CSV file
            csv_writer.writerow(row_stack)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(get_all(data))
    
    data_file.close()

if __name__ == "__main__":
    main()