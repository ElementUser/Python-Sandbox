# ========================================================================================================================================================================================
# Summary:
# This Python script measures the run time for the creation of an object vs. the creation of a dictionary, given similar data members
# Relevant context: this script is used to automatically use the Google Calendar API & create a Google Calendar Event (hence why dateutil.parse is needed with a datetime event)
# ========================================================================================================================================================================================

# References: 
# - https://pythontips.com/2013/07/28/generating-a-random-string/
# - https://www.geeksforgeeks.org/timeit-python-examples/

# Importing the required modules
import timeit
from dateutil.parser import parse
import string
import random

# Random string generator function
def random_string(size):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(size))

# Object creation function
def createTimestampObj(start, end, roomName, firstName, lastName):
    # For some reason, replacing "+" directly with anything will still yield a whitespace character after the parse function, and the parse function requires that + to not be there
    formattedStartTime = str(parse(start.replace("%3A", ":").replace("+", " "))).replace(" ", "T")
    formattedEndTime = str(parse(end.replace("%3A", ":").replace("+", " "))).replace(" ", "T")
    summaryText = roomName + " (" + firstName + " " + lastName + ")"
    description = "Test Run"

    return Timestamp(summaryText, description, formattedStartTime, formattedEndTime)

class Timestamp:
    # Parametrized constructor
    def __init__(self, summary, description, start, end):
        self.summary = summary
        self.description = description
        self.start = start
        self.end = end
        self.timeZone = 'America/Toronto'

# Dictionary creation function
def createTimestampDict(start, end, roomName, firstName, lastName):
    # For some reason, replacing "+" directly with anything will still yield a whitespace character after the parse function, and the parse function requires that + to not be there
    formattedStartTime = str(parse(start.replace("%3A", ":").replace("+", " "))).replace(" ", "T")
    formattedEndTime = str(parse(end.replace("%3A", ":").replace("+", " "))).replace(" ", "T")
    summaryText = roomName + " (" + firstName + " " + lastName + ")"
    description = "Test run"

    return {
        'summary': summaryText,
        'description': description,
        'start': formattedStartTime,
        'end': formattedEndTime,
        'timeZone': 'America/Toronto',
    }

# Compute object creation time
def objectCreation_time():
	SETUP_CODE = ''' 
from __main__ import createTimestampObj, random_string
from dateutil.parser import parse
import string
import random

calendarList = []'''

	TEST_CODE = ''' 
calendarList.append(createTimestampObj('2019-10-19+12%3A00', '2019-10-19+14%3A00', random_string(4), random_string(10), random_string(10)))'''

	times = timeit.repeat(setup = SETUP_CODE, 
						stmt = TEST_CODE, 
						repeat = 3, 
						number = 1)

	print('Object creation & appending to a list time: {}'.format(min(times)))		 


# Compute dictionary creation time
def dictCreation_time(): 
	SETUP_CODE = ''' 
from __main__ import createTimestampDict, random_string
from dateutil.parser import parse
import string
import random

calendarList = []'''

	TEST_CODE = ''' 
calendarList.append(createTimestampDict('2019-10-19+12%3A00', '2019-10-19+14%3A00', random_string(4), random_string(10), random_string(10)))'''

	times = timeit.repeat(setup = SETUP_CODE, 
						stmt = TEST_CODE, 
						repeat = 3, 
						number = 1)

	print('Dictionary creation & appending to a list time: {}'.format(min(times)))

if __name__ == "__main__":
	objectCreation_time()
	dictCreation_time()
