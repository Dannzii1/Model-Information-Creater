import random
from mimesis import *
import pandas as pd
from werkzeug.security import generate_password_hash
from datetime import datetime


Company = Business('en')
person = Person('en')
address = Address('en')
date = Datetime('en')
text = Text('en')

user_Columns = ['company_name', 'email', 'password', 'profile_picture', 'comp_desc', 'tel_num', 'role']
user_Column = ['company_id', 'street', 'parish', 'city']

password = 'p@$$word'
domains = ['com.jm', 'net.jm', 'org.jm', 'edu.jm', 'gov.jm', 'mil.jm']
picture = ['default.png']
parish = ['Kingston', 'St.Andrew', 'Portland', 'St. Thomas', 'St. Catherine',
          'Manchester', 'St Mary', 'St. Ann', 'Clarendon', 'Trelawny', 'St. James', 'Hanover', 'Westmoreland',
          'St. Elizabeth']
role = ['company']

company_data = []
company_address = []


def generateData(records):
    for _ in range(records):
        print("creating record " + str(_))
        company_name = Company.company()

        company_data.append([company_name, company_name.replace(" ", "_") + '.' + '@' + random.choice(domains),
                             generate_password_hash(password, method='pbkdf2:sha512', salt_length=10),
                             random.choice(picture), 'At' + ' ' + company_name + Company.company_type() + text.text(quantity=7),
                             '876' + '-' + person.telephone(mask='###-####'), random.choice(role)])

    pd.DataFrame(company_data).drop_duplicates(subset=[0]).to_csv(
        'Company_list.csv', sep=',', index=False, header=user_Columns)


def generateAddress(records):
    for _ in range(records):
        company_address.append([random.randint(335, 1473), address.street_number() + ' ' + address.street_name() + ' ' + address.street_suffix(),
                                random.choice(parish), address.city()])

    pd.DataFrame(company_address).to_csv(
        'Company_address_list.csv', sep=',', index=False, header=user_Column)


if __name__ == '__main__':
    start = datetime.now()
    print("in progress.........")
    #generateData(6000)
    generateAddress(6000)
    print((datetime.now()-start).total_seconds())
