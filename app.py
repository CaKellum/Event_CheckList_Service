''' This is the file you run '''
from dotenv import load_dotenv
load_dotenv()

from service_runner import app_container # pylint: disable=wrong-import-position

def main():
    '''main funtion of the app'''
    app_container.run()


if __name__ == "__main__":
    main()
