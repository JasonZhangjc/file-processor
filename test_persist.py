import unittest
from processor import persist
import psycopg2
import json


class PersistDataTest(unittest.TestCase):
    def test_first_test(self):
        self.assertEqual(3,3)
    
    def test_first_test(self):
        self.assertTrue("PYTHON".isupper())

    def test_read_from_pg(self):
        dbObject = persist.PersistData("postgres")
        courses = dbObject.read_from_pg("futurexschema.futurex_course_catalog")
        # print(courses[0][1])
        self.assertEqual(courses[0][1], 'Hadoop Spark')
        self.assertEqual(len(courses[0]), 5)
        with self.assertRaises(psycopg2.errors.UndefinedTable):
            dbObject.read_from_pg("futurexschema.table_invalid")



if __name__ == '__main__':
    unittest.main()