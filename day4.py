""""
student = {
    "name": "Amit",
    "age": 21,
    "course": "Engineering"
}
print(student["name"])

student["age"] = 22
student["city"] = "Delhi"
print(student)
"""
"""
marks = {"math": 80, "science": 75, "english": 85,}
print(marks.get("math"))
print(marks.get("history", 0))
for subject, score in marks.items():
    print(subject, score)
    """
""""
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

contacts["Diana"] = "555-3456"

contacts["Bob"] = "555-8765"
existing_contact = contacts.get("Alice", "Contact not found")
missing_contact = contacts.get("Evan", "Contact not found")


print("Safe Lookups:")
print("Alice:", existing_contact)
print("Evan:", missing_contact)
print()

print("Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
    """
""""
#unique set of IDs
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]


unique_users = set(raw_logs)

is_id05_present = "ID05" in unique_users
print("Is ID05 in unique_users?", is_id05_present)

print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))

print("Unique user IDs:", unique_users)
"""
# Create the interest sets
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b
print("Shared interests:", shared_interests)
print("All interests:", all_interests)
print("Interests unique to Friend A:", unique_to_a)



