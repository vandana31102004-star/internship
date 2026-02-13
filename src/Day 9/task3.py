# Step 1: Import Pandas
import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Step 3: Clean the usernames
cleaned_usernames = usernames.str.strip()   
cleaned_useranames = cleaned_usernames.str.lower()
contains_a = cleaned_usernames.str.contains('a')
print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nUsernames containing 'a':")
print(contains_a)


s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

scores=pd.Series([45,67,89,34,90])
passed=scores[scores>90]
print(passed)

data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(1))

names=pd.Series(['Alice','bob','CHARLIE'])
print(names.str.lower())
print(names.str.contains('A'))

