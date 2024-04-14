'''
A program in python to find the shortest path to go to other buildings from Computer Science building.
CS 3364: Project 3
'''

a = [
    'College Square', 'Prince Center', 'Police Dept', 'Student Health Center',
    'Lewis Science Center', 'Computer Science', 'Torreyson Library',
    'Old Main', 'Fine Art', 'Student Center', 'Burdick', 'McAlister Hall',
    'Wingo', 'New Business Building', 'Brewer-Hegema', 'Bear Village Apt',
    'Speech Language Hearing', 'Maintenance College', 'Oak Tree Apt']  # a list of all vertices
list1 = []  # used to hold data in the data extraction function.
new = {
}  # dictionary to hold the vertices(keys) and connected edges in the form of objects.
v = []
dist = {}  # dictionary for distance between edges. Initial val = inf
prev = {}  # dictionary for previous values. Initial val = NIL
sTree = {}  # dictionary for spanning Tree. Key: [values]


class DataExtraction:

  def __init__(self, Name, Distance) -> None:
    self.Name = Name
    self.Distance = Distance


class object1:

  def __init__(self, index, value):
    self.index = index
    self.value = value


class PriorityQueue(object):

  def __init__(self):
    self.queue = []

  def __str__(self):
    return ' '.join([str(i) for i in self.queue])

  def isEmpty(self):
    return len(self.queue) == 0

  def insert(self, index, data):
    if index is not None:
      for i in self.queue:
        if i.index == index:
          self.queue[self.queue.index(i)] = data
    else:
      self.queue.append(data)

  def delete(self):
    try:
      max_val = 0
      for i in range(len(self.queue)):
        if self.queue[i].value < self.queue[max_val].value:
          max_val = i
      item = self.queue[max_val]
      del self.queue[max_val]
      return item
    except IndexError:
      print()
      exit()


# Provided data
data_lines = [
    'College Square - Prince Center 300 - Lewis Science Center 200',
    'Prince Center - College Square 300 - Police Dept 100 - Torreyson Library 30 - Computer Science 80',
    'Police Dept - Prince Center 100 - Student Health Center 100 - Old Main 200 - Fine Art 50',
    'Student Health Center - Police Dept 100 - Student Center 50 - Brewer-Hegema 200',
    'Lewis Science Center - College Square 200 - Computer Science 150 - Speech Language Hearing 250',
    'Computer Science - Lewis Science Center 150 - Prince Center 80 - Torreyson Library 40 - Burdick 30',
    'Torreyson Library - Computer Science 40 - Prince Center 30 - Old Main 30 - Burdick 80',
    'Old Main - Torreyson Library 30 - Police Dept 200 - Fine Art 90 - McAlister Hall 100',
    'Fine Art - Old Main 90 - Police Dept 50 - Student Center 80 - McAlister Hall 100',
    'Student Center - Fine Art 80 - Student Health Center 50 - New Business Building 110 - Wingo 100 - McAlister Hall 100',
    'Burdick - Speech Language Hearing 100 - Computer Science 30 - Torreyson Library 80 - McAlister Hall 200 - Maintenance College 300',
    'McAlister Hall - Burdick 200 - Old Main 100 - Fine Art 180 - Student Center 100 - Wingo 50 - Maintenance College 150',
    'Wingo - McAlister Hall 50 - Student Center 100 - New Business Building 50 - Maintenance College 100',
    'New Business Building - Wingo 50 - Student Center 110 - Brewer-Hegema 20 - Maintenance College 30',
    'Brewer-Hegema - New Business Building 20 - Student Health Center 200 - Bear Village Apt 350 - Oak Tree Apt 40',
    'Bear Village Apt - Brewer-Hegema 350',
    'Speech Language Hearing - Lewis Science Center 250 - Burdick 100 - Maintenance College 120',
    'Maintenance College - Speech Language Hearing 120 - Burdick 300 - McAlister Hall 150 - Wingo 100 - New Business Building 150 - Oak Tree Apt 160',
    'Oak Tree Apt - Maintenance College 160 - Brewer-Hegema 40'
]