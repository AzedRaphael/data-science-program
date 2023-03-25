def schoolEval(name, age):
    '''
    School eval accepts names and age and returns the category of school of the person depending on the age
    '''
    kindergartenMinAge = 2
    elementaryMinAge = 4
    highSchoolMinAge = 10
    collegeMinAge = age

    candidateAge = age
    if candidateAge >= 75:
        return [name, 'Cannot go to school']
    elif candidateAge >= 16:
        return [name, 'College']
    elif candidateAge >= 10:
        return [name, 'Highschool']
    elif candidateAge >= 4:
        return [name, 'Elementary']
    elif candidateAge >= 2:
        return [name, 'Kindergarten']
    else:
        return [name, 'Daycare']

studName, school = schoolEval('Raphael', 20)
