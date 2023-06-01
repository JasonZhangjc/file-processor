from processor import ingest, persist
import logging
import logging.config
from flask import Flask, request



app = Flask(__name__)

@app.route('/courses', methods=['GET'])
def get_courses():
    dbObject = persist.PersistData("postgres")
    courses = dbObject.read_from_pg("futurexschema.futurex_course_catalog")
    return "courses are - " + str(courses)

@app.route('/courses', methods=['POST'])
def insert_courses():
    input_json = request.get_json(force=True)
    print("input_json > " + str(input_json))
    dbObject = persist.PersistData("postgres")
    dbObject.write_from_json_to_pg("futurexschema.futurex_course_catalog", input_json)
    return "success"


class DriverProgram:
    logging.config.fileConfig("processor/resources/configs/logging.conf")

    def __init__(self,fileType):
        logging.debug("I am within the constructor")
        self.file_type = fileType

    def my_function(self):
        logging.debug("inside my function . Processing "+self.file_type + " file")
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")
        read_json = reader.read_file()
        print("read the json " + str(read_json))
        writer.store_data(read_json)

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    app.run(port=8005, debug=True)
    # print("Entering the main method")
    # print_hi('vscode')
    # driver = DriverProgram("json")
    # driver.my_function()



