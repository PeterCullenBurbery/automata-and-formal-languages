# Peter Cullen Burbery
# HW2b CS 360 Fall 2023
import re

def extract_phone_number(line):
  """Extracts the phone number from a line of text.

  Args:
    line: The line of text containing the name and phone number.

  Returns:
    The phone number in the format "(304) 123-4567".
  """

  phone_number_regex = r"(\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})"
  match = re.search(phone_number_regex, line)
  if match:
    return match.group(1)
  else:
    return None

def main():
  """Reads a list of names and phone numbers from the standard input and outputs the phone numbers."""

  phone_numbers = []
  while True:
    line = input()
    phone_number = extract_phone_number(line)
    if phone_number:
      phone_numbers.append(phone_number)
    else:
      break

  for phone_number in phone_numbers:
    print(phone_number)

def get_lines():
  lines = []
  while True:
    line = input()
    if line == '':
      break
    lines.append(line)
  return lines

lines = get_lines()

for line in lines:
  print(line)


if __name__ == "__main__":
  main()
