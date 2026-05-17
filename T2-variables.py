# Variables in python
first_namee = 'Saniya Ali Jabeen'
last_name = 'Mohammad'
country = 'India'
city = 'Telangana'
age = 22
is_married = False
skills = ['HTML','CS','JS','REACT','PYTHON']
person_info = {
    'firstname' : 'sophie',
    'lastname' : 'kitty',
    'country' : 'korea',
    'city' : 'seoul'
}

# printing the values stored in the variables

print('First name:', first_namee)
print('First name length: ', len(first_namee))
print('Lst name: ', last_name)
print('Last name length: ',len(last_name))
print('Country: ', country)
print('City: ',city)
print('Age: ', age)
print('Married: ', is_married)
print( 'Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Saniya Ali Jabeen', 'Mohammad', 'India', 20, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('country: ', country)
print('age: ', age)
print('Married: ', is_married)