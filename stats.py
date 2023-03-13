import json, csv, datetime

#load INTERNAL data
internal_jobs_list=[]
with open('input/job_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if (row[2]):
            internal_jobs_list.append(row[2])
print('Internal jobs for processing:', len(internal_jobs_list))
# END INTERNAL DATA

# Load the OPENDATA data
now_jobs = []
with open('input/clean/now.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        now_jobs.append(row)
print("Loaded {} NOW jobs.".format(len(now_jobs)))

bis_jobs = []
with open('input/clean/bis.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        bis_jobs.append(row)
print("Loaded {} BIS jobs.".format(len(bis_jobs)))
# END OPENDATA

# count processed jobs
processed_jobs = 0
processed_data = [['Dataset', 'Job', 'Cost', 'SQFT', 'Applicant', 'BIN']]
# count the index errors
index_error_count = 0
index_error_rows = []

for job in internal_jobs_list:
    try:
        if job[0].isalpha():
            #this is a now job
            for row in now_jobs:
                fixed_job_number =  job + "-I1"
                if fixed_job_number.lower() == row[0].lower():
                    dob = 'now'
                    cost = row[31]
                    sqft = row[32]
                    applicant = row[12]
                    bin = row[7]
                    processed_data.append([dob, fixed_job_number, cost, sqft, applicant, bin])
        else:
            pass
            for row in bis_jobs:
                if job.lower() == row[0]:
                    dob = 'bis'
                    cost = row[46]
                    sqft = row[83]
                    applicant = row[38]
                    bin = row[7]
                    processed_data.append([dob, job, cost, sqft, applicant, bin])

        processed_jobs += 1
        if (processed_jobs % 1000 == 0):
            print('...processed 1000 jobs. Continuing on the rest..')

    except IndexError:
        index_error_count += 1
        index_error_rows.append(job)

print('Index errors encountered:', index_error_count)
print('Internal jobs processed:', processed_jobs)

now = datetime.datetime.now()
output_filename = 'output/'
output_filename += now.strftime('%Y-%m-%d_%H-%M-%S.csv')
with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in processed_data:
        writer.writerow(row)

print('{} file written successfully'.format(output_filename))
