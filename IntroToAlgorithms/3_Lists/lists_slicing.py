# Indexing a list
countries = ["Canada", "China", "Mexico",
             "Japan", "Brazil", "Iran",
             "Korea", "Philippines", "USA"]
print(countries[0])  # Canada
print(countries[-1])  # USA
print(countries[len(countries)-1])  # USA

# Modify(change) elements - lists are mutable(can be chage)
countries[0] = "England"
print(countries)

# Slicing lists (end index is not inclusive)
print(countries[0:3])
countries[4:6] = []  # removes 2 items 4 and 5
countries[0:3] = ["USA"]  # replaces 3 items at index 0, 1, 2 to "USA"
print(countries)

print(["USA"] * 3)

# str vs list
# strings are immutable. Strings contain characters.
# lists are mutable. lists can have any type of elements.

province = "AB"
# mutate(change) str province
# province[0] = "C"  # Error -> strings are immutable.
# re-assign a new value to province
province = "BC"
print(province)
