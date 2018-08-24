import unittest
from WorkoutApi import ServerApi


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ENDPOINT:/np/workouts-partner/v1.0/workouts/{workoutId}
    # valid access token and workoutId
    def test_workoutById1(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', '219453846').status_code)

    # invalid access token
    def test_workoutById2(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('ghetaejkls12ap4dfo3erry425dmmtunv', '219453846').status_code)

    # missing access token
    def test_workoutById3(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('', '219453846').status_code)

    # missing access token and workoutId
    def test_workoutById4(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('', '').status_code)

    # invalid workoutId
    def test_workoutById5(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', '245').status_code)

    # invalid workouyId - negative
    def test_workoutById6(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', '-219453846').status_code)

    # invalid workouyId - non numeric values
    def test_workoutById7(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', 'fge').status_code)

    # invalid workouyId - service symbols
    def test_workoutById8(self):
         api = ServerApi()
         self.assertNotEqual(200, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', '#$@').status_code)







    # ENDPOINT:/np/workouts-partner/v1.0/exercisers/{exerciserUuid}/workouts
    # valid access token, exceciserUuid, limit, page
    def test_workoutByExceciserUuid1(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid access token
    def test_workoutByExceciserUuid2(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls1g6hj8kkjhyenbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

     # missing access token
    def test_workoutByExceciserUuid3(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid exceciserUuid
    def test_workoutByExceciserUuid4(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'ddddd32d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)
    # missing exceciserUuid
    def test_workoutByExceciserUuid5(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    '',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)






if __name__ == '__main__':
    unittest.main()