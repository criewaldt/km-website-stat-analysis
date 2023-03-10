import json, csv
from opendata.opendata import GetDataByJOB

job_data = GetDataByJOB()

#load jobs data into list
csv_path = 'input/jobs.csv'
gathered_jobs_list = []
jobs_list=[]

now_jobs = []
bis_jobs = []

with open('input/now.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        now_jobs.append(row)
print("Loaded {} NOW jobs.".format(len(now_jobs)))

with open('input/bis.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        bis_jobs.append(row)



quit()
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        jobs_list.append(row[2])

print('Gathered {} job numbers.'.format(len(jobs_list)))
input()

for job in jobs_list:
    try:
        if job[0].isalpha():
            #this is a now job
            print('job number: ', job)
            data = job_data.get_data('now', job)
            
        else:
            #this is a bis job
            data = job_data.get_data('bis', job)
        
        if (data):
            gathered_jobs_list.append(data)
        
        if (len(gathered_jobs_list) % 1000 == 0):
            with open('output/output.csv', 'w', newline='') as csv_file:
                # Create a CSV writer object
                print('Writing file...')
                csv_writer = csv.writer(csv_file)
                for row in gathered_jobs_list:
                    csv_writer.writerow(row)

    except IndexError:
        pass



    
