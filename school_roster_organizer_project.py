
import itertools

student_roster = [
  {
    "name": "Karina M",
    "age": 8,
    "height": 48,
    "favorite_subject": "Math",
    "favorite_animal": "Dog"
  },
  {
    "name": "Yori K",
    "age": 7,
    "height": 50,
    "favorite_subject": "Art",
    "favorite_animal": "Cat"
  },
  {
    "name": "Alex C",
    "age": 7,
    "height": 47,
    "favorite_subject": "Science",
    "favorite_animal": "Cow"
  },
  {
    "name": "Esmeralda R",
    "age": 8,
    "height": 52,
    "favorite_subject": "History",
    "favorite_animal": "Rabbit"
  },
  {
    "name": "Sandy P",
    "age": 7,
    "height": 49,
    "favorite_subject": "Recess",
    "favorite_animal": "Guinea Pig"
  },
  {
    "name": "Matthew Q",
    "age": 7,
    "height": 46,
    "favorite_subject": "Music",
    "favorite_animal": "Walrus"
  },
  {
    "name": "Trudy B",
    "age": 8,
    "height": 45,
    "favorite_subject": "Science",
    "favorite_animal": "Ladybug"
  },
  {
    "name": "Benny D",
    "age": 7,
    "height": 51,
    "favorite_subject": "Math",
    "favorite_animal": "Ant"
  },
  {
    "name": "Helena L",
    "age": 7,
    "height": 53,
    "favorite_subject": "Art",
    "favorite_animal": "Butterfly"
  },
  {
    "name": "Marisol R",
    "age": 8,
    "height": 50,
    "favorite_subject": "Math",
    "favorite_animal": "Lion"
  }
]

# define ClassroomOrganizer class which organizes students in tables in general
# cases or for those specifically interested in math/science
 
class ClassroomOrganizer:
  def __init__(self):
    self.stored_names = []
    self.math_science_names = []

  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    if self.count < len(student_roster):
      (self.stored_names).append(student_roster[self.count]['name'])
      (self.stored_names).sort()
      self.count += 1
      return self.count
      return self.stored_names
    else:
      raise StopIteration 
  #4
  def table_combos(self):
    return list(itertools.combinations(self.stored_names, 2))
#5
  def math_sci_tables(self):
    for i in range(len(student_roster)):
      if student_roster[i]['favorite_subject'] == 'Math' or student_roster[i]['favorite_subject'] == 'Science':
        (self.math_science_names).append(student_roster[i]['name'])
    return list(itertools.combinations(self.math_science_names, 4))





Roster = ClassroomOrganizer()

for i in Roster:
  Roster.stored_names
#calls next dunder per iteration which adding a name 
#to our list and sorting if alphabetically. Final iteration returns 
#finalized list full of names sorted alphabetically.

#print(Roster.stored_names)
#prints list of all names sorted alphabetically (A-Z)

student_names = Roster.stored_names
#print(student_names)

tables = Roster.table_combos()
#print(tables)
#prints list of every possible table combination (of two people) each represented as a tuple

#5
tables_for_math_sci_students = Roster.math_sci_tables()
print(tables_for_math_sci_students)
#prints a list of all table combos (seating 4 each) for those interested in science or math 
