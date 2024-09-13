place = ['Boston, Japan, Portugal']
print(place)


print("Original order:")
print(place)

print("\nAlphabetical:")
print(sorted(place))

print("\nOriginal order:")
print(place)

print("\nReverse alphabetical:")
print(sorted(place, reverse=True))

print("\nOriginal order:")
print(place)

print("\nReversed:")
place.reverse()
print(place)

print("\nOriginal order:")
place.reverse()
print(place)

print("\nAlphabetical")
place.sort()
print(place)

print("\nReverse alphabetical")
place.sort(reverse=True)
print(place)