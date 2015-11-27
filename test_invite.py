import unittest
from pprint import pprint
from invite import Invite
from parser import PeopleParser

class TestInvite(unittest.TestCase):
    def setUp(self):
        self.invite = Invite()
        parser = PeopleParser()
        self.people = parser.parse('people.txt')

    def test_absolute_delta_returns_same_delta(self):
        lat1 = 53.3381985
        lat2 = 52.986375

        delta1 = self.invite.get_delta(lat1, lat2)
        delta2 = self.invite.get_delta(lat2, lat1)

        self.assertEqual(delta1, delta2)

    def test_get_central_angle_on_same_point(self):
        someone = self.people[0]
        someone['latitude'] = self.invite.intercom_lat
        someone['longitude'] = self.invite.intercom_lon
        someone['latitude_rad'] = self.invite.intercom_lat_rad
        someone['longitude_rad'] = self.invite.intercom_lon_rad

        central_angle = self.invite.get_central_angle(someone)

        self.assertAlmostEqual(central_angle, 0.00, places=2)

    def test_get_central_angle_on_different_points(self):
        someone = self.people[0]
        central_angle = self.invite.get_central_angle(someone)
        self.assertGreater(central_angle, 0.0)

    def test_get_distance_same_point(self):
        someone = self.people[0]
        someone['latitude'] = self.invite.intercom_lat
        someone['longitude'] = self.invite.intercom_lon
        someone['latitude_rad'] = self.invite.intercom_lat_rad
        someone['longitude_rad'] = self.invite.intercom_lon_rad

        distance = self.invite.get_distance(someone)

        self.assertAlmostEqual(distance, 0.00, places=2)

    def test_get_distance_different_points(self):
        someone = self.people[0]
        distance = self.invite.get_distance(someone)
        self.assertGreater(distance, 0.0)

    def test_filter_cool_people(self):
        cool_people = self.invite.filter_cool_people(self.people, 100)
        for cool_guy in cool_people:
            self.assertLessEqual(cool_guy['distance'], 100)

    def test_sort_people(self):
        people = self.invite.sort_people_by_id(self.people)
        current_id = 0
        for cool_guy in people:
            self.assertGreaterEqual(cool_guy['user_id'], current_id)
            current_id = cool_guy['user_id']

    def test_invite_test_people(self):
        cool_people = self.invite.these_within('people.txt', 100)
        pprint(cool_people)

if __name__ == '__main__':
    unittest.main()
