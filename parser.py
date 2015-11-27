import json

from math import *

#
# Parses a file of people
#
class PeopleParser(object):

    def parse(self, people_file):
        file = open(people_file)
        people = [json.loads(line.rstrip('\n')) for line in file]
        people = self.correct_types(people)
        file.close()
        return people

    def correct_types(self, people):
        correct_people = []
        for someone in people:
            someone['latitude'] = float(someone['latitude'])
            someone['longitude'] = float(someone['longitude'])
            someone['latitude_rad'] = radians(90.0 - float(someone['latitude']))
            someone['longitude_rad'] = radians(float(someone['longitude']))
            correct_people.append(someone)
        return correct_people
