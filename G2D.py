import csv
from faker import Faker
from random import randint

fake = Faker()

positions = ['FullStackDeveloper', 'BackEndDeveloper', 'FrontEndDeveloper', 'Software Engineer', 'Data Analysts',
             'Network Administrator', 'Network Analyst']

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

parish = ['Kingston', 'St.Andrew', 'Portland', 'St. Thomas', 'St. Catherine',
          'Manchester', 'St Mary', 'St. Ann', 'Clarendon', 'Trelawny', 'St. James', 'Hanover', 'Westmoreland',
          'St. Elizabeth']

GPA = ['2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5']
employment_type = ['Full Time', 'Part Time']


def get_skills(pos_skills_list):
    skill_copy = [x for x in pos_skills_list]
    new_skills = []
    for _ in range(0, 3):
        skill_index = randint(0, len(skill_copy) - 1)
        new_skills.append(skill_copy.pop(skill_index))

    return new_skills


# populating table
with open('company_internship.csv', 'w', newline='') as f:
    the_writer = csv.writer(f)
    the_writer.writerow(
        ['Position', 'GPA', 'Skills', 'Parish', 'Employment Type'])
    for i in range(1, 500):
        selected_position = fake.random.choice(positions)
        skills = get_skills(job_position_skills[selected_position])
        the_writer.writerow([selected_position, fake.random.choice(GPA), [skills[0], skills[1],
                             skills[2]], fake.random.choice(parish), fake.random.choice(employment_type)])


