import csv
from json import loads


import requests

payload = {}
headers = {
    "apikey": "3AS2FMnrrBCR7zYOniLszRevTHr9UU1q"
}

skill = ['Python', 'R', 'Ruby', 'css', 'javascript', 'html', 'php', 'angular', 'react', 'django', 'rails',
         'UNIX', 'TCP/IP', 'C#', 'inference', 'ML', 'SQL', '.Net', 'Mean', 'vue', 'backbone', 'LAN', 'WAN',
         'hypothesis testing', 'git', 'vue', 'Kotlin']
store_skill = []

for i in skill:
    url = "https://api.promptapi.com/skills?q={}".format(i)
    skills = requests.request("GET", url, headers=headers, data=payload)
    status_code = skills.status_code
    skill_result = skills.text
    store_skill += loads(skill_result.replace('\n', ''))


with open('company_skills1.csv', 'w') as f:
    the_writer = csv.writer(f)
    the_writer.writerow(['Skills'])
    for skill in store_skill:
        the_writer.writerow({skill.replace(',', ' ')})



