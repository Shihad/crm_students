
from datetime import datetime

datetime_string = "11/17/20"
datetime_obj = datetime.strptime(datetime_string, '%m/%d/%y')
print(datetime_obj)
