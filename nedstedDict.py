ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}
#1
print("Ramit\'s email: " + ramit['email'])
#2
print("Ramit\'s first interest: " + ramit['interests'][0])
#3
print("Jasmine\'s email: " + ramit['friends'][0]['email'])
#4
print("Jan\'s second interest is: " + ramit['friends'][1]['interests'][1])