import random
from mimesis import *
import pandas as pd
from werkzeug.security import generate_password_hash
from datetime import datetime

person = Person('en')
date = Datetime('en')
text = Text('en')
user_Columns = ['firstname', 'lastname', 'email', 'username', 'password', 'profile_picture', 'dob',
                'number', 'role', 'bio', 'major', 'minor', 'school']
user_Column = ['student_id', 'parish']
user_skill_Column = ['student_id', 'name']

domains = ['gmail.com', 'yahoo.com', 'outlook.com']
picture = ['default.png']
school = ['University of the West Indies', 'University of Technology', 'University of the Commonwealth Caribbean',
          'Mico University College', 'Northern Caribbean University', 'Shortwood Teachers College',
          'St.Joseph Teachers College']
courses = ['Computer Science', 'Information Technology', 'Systems & Network Administration', 'Information Science',
           'Computer Engineering', 'Cybersecurity', 'Information Systems']
parish = ['Kingston', 'St.Andrew', 'Portland', 'St. Thomas', 'St. Catherine',
          'Manchester', 'St Mary', 'St. Ann', 'Clarendon', 'Trelawny', 'St. James', 'Hanover', 'Westmoreland',
          'St. Elizabeth']
skills = ['php', 'git', 'django', 'rails', 'git', 'vue', 'backbone', 'css', 'javascript', 'html', 'angular', 'react',
          'css', 'javascript', 'html', 'php', 'git', 'vue', 'backbone', 'django', 'rails', 'angular',
          'react', 'SQL', 'Java', 'Python', 'C#', '.Net', 'Mean', 'Ruby', 'LAN', 'WAN', 'UNIX', 'TCP/IP', 'C++',
          'hypothesis testing', 'statistical' 'inference', 'regressions', 'ML systems', 'R']

role =['student']

student_data = []
student_address = []
student_skill = []
password = 'p@$$word'


def generateData(records):

    for _ in range(records):
        print("creating record "+str(_))
        first_name = person.first_name()
        last_name = person.last_name()
        student_data.append([first_name, last_name, first_name + '.' + last_name + '@' + random.choice(domains),
                             first_name + '.' + last_name,
                             generate_password_hash(password, method='pbkdf2:sha512', salt_length=10),
                             random.choice(picture), date.formatted_date(start=1994, end=2004),
                             '876' + '-' + person.telephone(mask='###-####'), random.choice(role),
                             text.text(quantity=4), random.choice(courses), random.choice(courses),
                             random.choice(school)])

    pd.DataFrame(student_data).drop_duplicates(subset=[3]).to_csv(
        'Students_list.csv', sep=',', index=False, header=user_Columns)


def generateAddress(records):
    for _ in range(records):
        student_address.append([random.randint(4591, 10581), random.choice(parish)])

    pd.DataFrame(student_address).to_csv(
        'Students_address_list.csv', sep=',', index=False, header=user_Column)


def generateSkill(records):
    for _ in range(records):
        student_skill.append([random.randint(4591, 10581), random.choice(skills)])

    pd.DataFrame(student_skill).to_csv(
        'Student_skill_list.csv', sep=',', index=False, header=user_skill_Column)


if __name__ == '__main__':
    start = datetime.now()
    print("in progress.........")
    #generateData(6000)
    #generateAddress(6000)
    generateSkill(15000)
    print((datetime.now()-start).total_seconds())
