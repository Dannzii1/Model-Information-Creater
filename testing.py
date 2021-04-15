import csv
from faker import Faker
import os

fake = Faker()

with open('students.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    os.path.join('/Documents/Year3/Capstone/model ting', 'students.csv')
    thewriter.writerow(['UserId', 'Username', 'Password', 'First Name', 'Last Name', 'Email', 'DOB', 'Phone Number'])
    for i in range(1, 100):
        fname = fake.first_name()
        lname = fake.first_name()

        thewriter.writerow(
            [fake.random_int(min=1, max=100), fname + fake.bothify(text='###'), fake.bothify(text='???###?#'), fname,
             lname, fname + '.' + lname + '@' + fake.free_email_domain(),
             fake.date_between(start_date='-30y', end_date='-18y'), '876' + '-' + fake.bothify(text='###-####')])

with open('student_address.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    os.path.join('/Documents/Year3/Capstone/model ting', 'student_address.csv')
    thewriter.writerow(['Street', 'parish'])
    parish = ['Kingston', 'St.Andrew', 'Portland', 'St. Thomas', 'St. Catherine',
              'Manchester', 'St Mary', 'St. Ann', 'Clarendon', 'Trelawny', 'St. James', 'Hanover', 'Westmoreland',
              'St. Elizabeth']
    for i in range(1, 100):
        thewriter.writerow([fake.street_address(), fake.random.choice(parish)])

# populating table User_email
# with open('mycsv3.csv','w',newline='') as f:
#    thewriter = csv.writer(f)
#     thewriter.writerow(['UserId','Email'])
#    for i in range (1,10):
#         thewriter.writerow([fake.random_int(min=1, max=10),fake.first_name() + fake.last_name() +'@'+fake.free_email_domain()])
