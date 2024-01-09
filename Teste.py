from faker import Faker

fake = Faker()

num_entries = 5

name_list = []
age_list = []
sex_list = []

for _ in range(num_entries):

    name = fake.name()
    age = fake.random_int(min=12, max=85)
    sex = fake.random_element(elements=('Male', 'Female'))

    name_list.append(name)
    age_list.append(age)
    sex_list.append(sex)


for i in range(num_entries):
    print('Name: {}, Age: {}, Sex: {}'.format(name_list[i], age_list[i], sex_list[i]))





