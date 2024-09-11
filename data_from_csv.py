import os
import csv
data =[]
def read_all_csv_in_row():
    directory = '/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/terror_transcript_analyze/input/csv_files'

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            print(f'Processing file: {filename}')

            with open(file_path, mode='r',  encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)


                for row in csv_reader:
                    data.append(row)
                return data
