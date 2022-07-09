import pickle

courses_rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1224,
                 'CM241':1411}
courses_instructors = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich',
                      'NT110':'Burke','CM241':'Lee'}
courses_times = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.',
                'NT110':'11:00 a.m.','CM241':'1:00 p.m.'}


file = open('classpickle.pickle','wb')
pickle.dump(courses_rooms, file)
pickle.dump(courses_instructors, file)
pickle.dump(courses_times, file)
file.close()

course = True

while course == True:
    course = input('\nEnter a course number or press "q" to quit: ')
    print(course)
    
    if course in courses_rooms.keys():
        print()
        print('Room: ',courses_rooms[course])
        print('Instructor: ',courses_instructors[course])
        print('Time: ',courses_times[course])
        
    elif course == 'q' or 'Q':
        break
    
    else:
        print("That is not appropriate characters")