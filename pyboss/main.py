#PyBoss

#import pertinent modules
import os
import csv
import datetime
import us 

#csv paths
data_csv = "employee_data2"

working_csv = os.path.join(data_csv + ".csv")

employee_id =[]
first_name = []
last_name = []
dob = []
ssn = []
state = []

with open(working_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header row
    next (csvreader)

    for row in csvreader:

        #compile employee ID
        employee_id.append(row[0])

        #split name into first and last names
        split_name = (row[1].split())

        #compile first names
        first_name.append(split_name[0])

        #compile last names
        last_name.append(split_name[1])

        # compile & format DOB
        dob.append(datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%-m/%d/%y"))

        #split ssn
        ssn_full = (row[3].split("-"))

        #compile ssn
        ssn.append("***-**-" + ssn_full[2])

        # compile state and format with abbrevation
        state.append(us.states.lookup(row[4]).abbr)

clean_header = [("Emp ID", "First Name", "Last Name", "DOB", "SSN", "State")]
clean_data = zip(employee_id, first_name, last_name, dob, ssn, state)

output_file = data_csv + "results.csv"
data_output = os.path.join(output_file)

with open(data_output, mode = "w", newline = "") as output:
    writer = csv.writer(output)

    writer.writerows(clean_header)
    writer.writerows(clean_data)