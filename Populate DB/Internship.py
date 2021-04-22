import random
from mimesis import *
from random import randint
import pandas as pd
from datetime import datetime

Company = Business('en')
person = Person('en')
address = Address('en')
date = Datetime('en')
text = Text('en')

user_Columns = ['company_id', 'position', 'profile_picture', 'description', 'tel_num', 'qualifications', 'gpa',
                'start_date', 'end_date', 'is_active']
user_Column = ['internship_id', 'street', 'parish', 'city']
user_skill_Column = ['internship_id', 'name']

activity_status = ['True', 'False']
picture = ['default.png']
positions = ['Full Stack Developer', 'Back End Developer', 'Front End Developer', 'Software Engineer', 'Data Analysts',
             'Network Administrator', 'Network Analyst']
parish = ['Kingston', 'St.Andrew', 'Portland', 'St. Thomas', 'St. Catherine',
          'Manchester', 'St Mary', 'St. Ann', 'Clarendon', 'Trelawny', 'St. James', 'Hanover', 'Westmoreland',
          'St. Elizabeth']
description = ['We are looking for a hardworking individual, who is a quick learner and open to learn and grow with '
               'our company.', 'Expected to participate in the implementation of information systems policies, '
                               'procedures, standards and guidelines across all divisions and subsidiaries. ',
               'Responsible for the development of detailed implementation plans for solutions to be deployed to the '
               'live environment. ', 'We are seeking to recruit a suitably qualified experienced professional to fill '
                                     'the position stated above. We are looking forward to working with you in our '
                                     'company. ']

job_position_skills = {
    'BackEndDeveloper': ['php', 'git', 'django', 'rails'],
    'FrontEndDeveloper': ['git', 'vue', 'backbone', 'css', 'javascript', 'html', 'angular', 'react'],
    'FullStackDeveloper': ['css', 'javascript', 'html', 'php', 'git', 'vue', 'backbone', 'django', 'rails', 'angular',
                           'react', 'SQL'],
    'Software Engineer': ['Java', 'Python', 'C#', '.Net', 'Mean', 'Ruby'],
    'Data Analysts': ['SQL', 'R', 'Python', 'Ruby'],
    'Network Administrator': ['LAN', 'WAN', 'UNIX', 'TCP/IP', 'C++', 'Python'],
    'Network Analyst': ['hypothesis testing', 'statistical' 'inference', 'regressions', 'ML systems', 'Python', 'R',
                        'SQL']
}
courses = ['Computer Science', 'Information Technology', 'Systems & Network Administration', 'Information Science',
           'Computer Engineering', 'Cybersecurity', 'Information Systems']
skills = ['php', 'git', 'django', 'rails', 'git', 'vue', 'backbone', 'css', 'javascript', 'html', 'angular', 'react',
          'css', 'javascript', 'html', 'php', 'git', 'vue', 'backbone', 'django', 'rails', 'angular',
          'react', 'SQL', 'Java', 'Python', 'C#', '.Net', 'Mean', 'Ruby', 'LAN', 'WAN', 'UNIX', 'TCP/IP', 'C++',
          'hypothesis testing', 'statistical' 'inference', 'regressions', 'ML systems', 'R']

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
start_year = [2021]
end_year = [2021, 2022]

internship_data = []
internship_address = []
internship_skill = []


def get_skills(pos_skills_list):
    skill_copy = [x for x in pos_skills_list]
    new_skills = []
    for _ in range(0, 5):
        skill_index = randint(0, len(skill_copy) - 1)
        new_skills.append(skill_copy.pop(skill_index))

    return new_skills


def generateData(records):
    for _ in range(records):
        year1 = str(random.choice(start_year))
        year2 = str(random.choice(end_year))
        mounth = str(random.choice(month))
        days = str(random.choice(day))
        start_date = year1 + '/' + mounth + '/' + days
        end_date = year2 + '/' + mounth + '/' + days
        internship_data.append(
            [random.randint(335, 1473), random.choice(positions), random.choice(picture), random.choice(description),
             '876' + '-' + person.telephone(mask='###-####'), random.choice(courses),
             round(random.uniform(2, 4), 2), start_date, end_date, random.choice(activity_status)])

    pd.DataFrame(internship_data).drop_duplicates(subset=[0]).to_csv(
        'Internship_list.csv', sep=',', index=False, header=user_Columns)


def generateAddress(records):
    for _ in range(records):
        internship_address.append([random.randint(454, 1586),
                                   address.street_number() + ' ' + address.street_name() + ' ' + address.street_suffix(),
                                   random.choice(parish), address.city()])

    pd.DataFrame(internship_address).to_csv(
        'Internship_address_list.csv', sep=',', index=False, header=user_Column)


def generateSkill(records):
    for _ in range(records):
        internship_skill.append([random.randint(454, 1586), random.choice(skills)])

    pd.DataFrame(internship_skill).to_csv(
        'Internship_skill_list.csv', sep=',', index=False, header=user_skill_Column)


if __name__ == '__main__':
    start = datetime.now()
    print("in progress.........")
    generateData(6000)
    # generateAddress(6000)
    #generateSkill(6000)
    print((datetime.now() - start).total_seconds())
