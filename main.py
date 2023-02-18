from pprint import pprint
import csv
import re

PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)\3-\4-\5 \6\7'

def normalize_phonebook():
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    for contact in contacts_list:
      names = contact[0].split(' ')
      if(len(names) > 1):
        contact[0] = names[0]
        contact[1] = names[1]
        if (len(names) > 2):
          contact[2] = names[2]
      else:
        names = contact[1].split(' ')
        if (len(names) > 1):
          contact[1] = names[0]
          contact[2] = names[1]
  return contacts_list


def remove_dublicates(contacts):
  i = 1
  clear_list = contacts[:]
  for current in contacts[1:]:
    i += 1
    if i <= len(contacts):
      for next in contacts[i:]:
        if current[0] == next[0]:
          for j in range(len(current)):
            if current[j] == '': current[j] = next[j]
          clear_list.remove(next)
  return clear_list

def normilaze_phones(contacts):
  for contact in contacts:
    contact[5] = re.sub(PHONE_PATTERN, PHONE_SUB, contact[5]).strip()
  return contacts

if __name__ == '__main__':
    contacts = normalize_phonebook()
    contacts = remove_dublicates(contacts)
    contacts = normilaze_phones(contacts)
    #pprint(contacts)
    with open("phonebook.csv", "w", newline='') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts)