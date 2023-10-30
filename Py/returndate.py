import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  os.mkdir(filename)
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  properdate = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}-{}-{}".format(properdate.year,properdate.month, properdate.day))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd