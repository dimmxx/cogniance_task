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
       self.assertNotEqual(200, api.workoutByExceciserUuid('vrgabdejkls1g6hj8kkjhyedgs3dvlll',\
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



    # invalid page - negative
    def test_workoutByExceciserUuid6(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    -1).status_code)

    # invalid page - zero
    def test_workoutByExceciserUuid7(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    0).status_code)



    # invalid page - float values
    def test_workoutByExceciserUuid8(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    '1.5').status_code)



    # invalid page - non numeric values
    def test_workoutByExceciserUuid9(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    'g').status_code)



    # invalid limit - negative
    def test_workoutByExceciserUuid10(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    -1,\
                                                    1).status_code)

    # invalid limit - < 1000
    def test_workoutByExceciserUuid11(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1001,\
                                                    1).status_code)


    # invalid limit - zero
    def test_workoutByExceciserUuid12(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    0,\
                                                    1).status_code)

    # invalid limit - float
    def test_workoutByExceciserUuid13(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1.1,\
                                                    1).status_code)


    # invalid limit - non numeric values
    def test_workoutByExceciserUuid14(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    'e',\
                                                    1).status_code)


    # valid date
    def test_workoutByExceciserUuid15(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '%5B2018-01-01T00%3A00%3A00Z%2C%202018-12-31T23%3A59%3A59Z%5D',\
                                                    1000,\
                                                    1).status_code)



    # invalid date - no brackets
    def test_workoutByExceciserUuid16(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '2018-01-01T00%3A00%3A00Z%2C%202018-12-31T23%3A59%3A59Z',\
                                                    1000,\
                                                    1).status_code)


    # invalid date - one date, not a period
    def test_workoutByExceciserUuid17(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '%5B2018-01-01T00%3A00%3A00Z',\
                                                    1000,\
                                                    1).status_code)


    # invalid date - non numerics values
    def test_workoutByExceciserUuid18(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    'z@]',\
                                                    1000,\
                                                    1).status_code)

    # valid categoryId
    def test_workoutByExceciserUuid19(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    12,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid categoryId - negative
    def test_workoutByExceciserUuid20(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    -1,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid categoryId - zero
    def test_workoutByExceciserUuid21(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    0,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


    # invalid categoryId - float
    def test_workoutByExceciserUuid22(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    1.1,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


    # invalid categoryId - non numeric values
    def test_workoutByExceciserUuid23(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    'd',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


if __name__ == '__main__':
    unittest.main()