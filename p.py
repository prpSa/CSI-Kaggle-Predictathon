#Converting to categorical value
categorical_d = {'yes': 1, 'no': 0}
x_newtest['schoolsup'] = x_newtest['schoolsup'].map(categorical_d)
x_newtest['famsup'] = x_newtest['famsup'].map(categorical_d)
x_newtest['paid'] = x_newtest['paid'].map(categorical_d)
x_newtest['activities'] = x_newtest['activities'].map(categorical_d)
x_newtest['nursery'] = x_newtest['nursery'].map(categorical_d)
x_newtest['higher'] = x_newtest['higher'].map(categorical_d)
x_newtest['internet'] = x_newtest['internet'].map(categorical_d)
x_newtest['romantic'] = x_newtest['romantic'].map(categorical_d)

categorical_d = {'F': 1, 'M': 0}
x_newtest['sex'] = x_newtest['sex'].map(categorical_d)

categorical_d = {'GP': 1, 'MS': 0}
x_newtest['school'] = x_newtest['school'].map(categorical_d)

# map the address data
categorical_d = {'U': 1, 'R': 0}
x_newtest['address'] = x_newtest['address'].map(categorical_d)

# map the famili size data
categorical_d = {'LE3': 1, 'GT3': 0}
x_newtest['famsize'] = x_newtest['famsize'].map(categorical_d)

# map the parent's status
categorical_d= {'T': 1, 'A': 0}
x_newtest['Pstatus'] = x_newtest['Pstatus'].map(categorical_d)

# map the parent's job
categorical_d = {'teacher': 0, 'health': 1, 'services': 2,'at_home': 3,'other': 4}
x_newtest['Mjob'] = x_newtest['Mjob'].map(categorical_d)
x_newtest['Fjob'] = x_newtest['Fjob'].map(categorical_d)

# map the reason data
categorical_d= {'home': 0, 'reputation': 1, 'course': 2,'other': 3}
x_newtest['reason'] = x_newtest['reason'].map(categorical_d)

# map the guardian data
categorical_d = {'mother': 0, 'father': 1, 'other': 2}
x_newtest['guardian'] = x_newtest['guardian'].map(categorical_d)