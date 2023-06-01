from processor import ingest, persist
import logging
import logging.config

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
    print("Entering the main method")

    print_hi('vscode')
    driver = DriverProgram("json")
    driver.my_function()


