import pytest
from processor import persist
import psycopg2


def test_my_test():
    assert True

def test_read_from_pg():
    dbObject = persist.PersistData("postgres")
    courses = dbObject.read_from_pg("futurexschema.futurex_course_catalog")
    assert 5 == len(courses[0])

def test_read_from_pg2():
    dbObject = persist.PersistData("postgres")
    with pytest.raises(psycopg2.errors.UndefinedTable):
        dbObject.read_from_pg("futurexschema.table_invalid")
    