import re

def findMatch(stringValue, stringValue2):
    regex = r"[0-9.?]"
    result = re.search(regex,stringValue)
    print(result)
    reg2 = r"Py.*n"
    result2 = re.search(reg2,stringValue2)
    print(result2)

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

findMatch("What do i do with this number 67996?", "Python Programming")


# Fill in the code to check if the text passed has at least 2 groups of 
# alphanumeric characters (including letters, numbers, and underscores) 
# separated by one or more whitespace characters.

def check_character_groups(text):
  
  result = re.search(r"[\w*][\s+][\w*]",text)
  #OR result = re.search(r"[a-zA-Z9_] [a-zA-z0-9_]", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


#Fill in the code to check if the text passed looks like a standard sentence, 
# meaning that it starts with an uppercase letter, 
# followed by at least some lowercase letters or a space, 
# and ends with a period, question mark, or exclamation point. 
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]+[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

def check_time(text):
  pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]\s*[APap][Mm]$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

def check_web_address(text):
  pattern = "^(https?://)?(www\.)?[a-zA-Z0-9_-]+\.[a-zA-Z]+\.*[a-z]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


#Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
def check_zip_code (text):
  result = re.search(r"[\s]\d{5}(-\d{4})?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


def contains_acronym(text):
  pattern = "\([\w*]+\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

#Fix the regular expression used in the rearrange_name function so that it can match middle names, 
# middle initials, as well as double surnames

def rearrange_name(name):
  result = re.search(r"^(\w*), (\w\.-*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

#The long_words function returns all words that are at least 7 characters. 
#Fill in the regular expression to complete this function.

def long_words(text):
  pattern = r"[\w*]{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  value = re.search(regex, log_line)
  if value is None:
    return ""
  return value[1]

print(extract_pid("This string has the error proccess id [14526].")) #returns 14526
print(extract_pid("This string has a numeric value 9908.")) #return empty string

def extract_pid2(log_line):
    regex = r"\[(\d+)\]:\s*([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid2("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid2("99 elephants in a [cage]")) # None
print(extract_pid2("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid2("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# We're working with a CSV file, which contains employee information.
# Each record has a name field, followed by a phone number field, and a role field. 
# The phone number field contains U.S. phone numbers, 
# and needs to be modified to the international format, 
# with "+1-" in front of the phone number. Fill in the regular expression, 
# using groups, to use the transform_record function to do that.

def transform_record(record):
  new_record = re.sub(r"(\d{3}-\d{3}-?\d{4})", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


#The multi_vowel_words function returns all words with 3 or 
#more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.

def multi_vowel_words(text):
  pattern = r"\b\w*[aeiouAEIOU]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

#The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX 
# (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), 
# and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
# Fill in the regular expression to complete this function.

def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b",r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


# The transform_comments function converts comments in a Python script into those usable by a C compiler. 
# This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), 
# which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility 
# of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. 
# We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, 
# to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 


def transform_comments(line_of_code):
  result = re.sub(r"#{1,3}", r"//",line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

#Regular Expressions Cheat-Sheet
# Check out the following links for more information:

# https://docs.python.org/3/howto/regex.html

# https://docs.python.org/3/library/re.html

# https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

# Shout out to 
# regex101.com
# , which will explain each stage of a regex. 

# Advanced Regular Expressions Cheat-Sheet
# Check out the following link for more information:

# https://regexcrossword.com/