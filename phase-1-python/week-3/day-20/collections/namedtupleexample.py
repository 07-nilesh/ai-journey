from collections import namedtuple
'''
# Define default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")
print(person)
print(person.name)  # Accessing the 'name' field
print(person.job)   # Accessing the 'job' field

# Create a dictionary from a named tuple
print(person._asdict())

# Replace the value of a field
person = person._replace(job="Web Developer")
print(person)'''

Milestone=namedtuple("Milestone", "name deadline is_urgent", defaults=["2024-12-31", True])
milestone1=Milestone("MVP Launch","May 30",True)
print(f"The {milestone1.name} milestone is due on {milestone1.deadline} and is urgent: {milestone1.is_urgent}")