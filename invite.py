from math import *
from parser import PeopleParser

class Invite(object):

    def __init__(self):
        self.intercom_lat = 53.3381985
        self.intercom_lat_rad = radians((90.0 - self.intercom_lat))
        self.intercom_lon = -6.2592576
        self.intercom_lon_rad = radians(self.intercom_lon)
        self.earth_radius = 6371
        self.parser = PeopleParser()

    def these_within(self, people_file, within):
        people = self.parser.parse(people_file)
        cool_people = self.filter_cool_people(people, within)
        sorted_cool_people = self.sort_people_by_id(cool_people)
        formatted_people = [(cool_guy['user_id'], cool_guy['name']) for cool_guy in sorted_cool_people]
        return formatted_people

    def filter_cool_people(self, people, within):
        cool_people = []
        for someone in people:
            someone['distance'] = self.get_distance(someone)
            if someone['distance'] <= within:
                cool_people.append(someone)
        return cool_people

    def sort_people_by_id(self, people):
        return sorted(people, key=lambda k: k['user_id'])

    def get_distance(self, someone):
        return self.earth_radius * self.get_central_angle(someone)

    def get_central_angle(self, someone):
        # Based on haversine
        delta_lat_rad = radians(self.get_delta(self.intercom_lat, someone['latitude']))
        delta_lon_rad = radians(self.get_delta(self.intercom_lon, someone['longitude']))
        x = pow(sin(delta_lat_rad / 2), 2) + \
            cos(self.intercom_lat_rad) * cos(someone['latitude_rad']) \
            * pow(sin(delta_lon_rad / 2), 2)
        return 2 * atan2(sqrt(x), sqrt(1 - x))

    def get_delta(self, elem1, elem2):
        return abs(elem1 - elem2)
