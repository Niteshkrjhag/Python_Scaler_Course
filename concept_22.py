#Strings are immutable so when every a fun like s.lower() is performed it returns a new string 

'''
.lower(): Converts all characters in the string to lowercase. This method is widely used in case-insensitive 
          comparisons.

.upper(): Transforms all characters to uppercase. It's commonly used for emphasizing certain texts or for 
          uniform data entry.

.capitalize(): Capitalizes the first character of the string while turning the rest into lowercase. 
               Useful for formatting titles or names.

.title(): Converts the first character of every word to uppercase and the other characters to lowercase. 
          Ideal for formatting headings or titles.

.swapcase(): Reverses the case of all characters in the string, turning lowercase letters to uppercase and 
             vice versa.

.casefold(): Similar to .lower(), but more aggressive. It's designed to remove all case distinctions in a string 
             and is often used for more effective case-insensitive comparisons.

'''

s = ' PyThOn Is AwEsOmE '
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.casefold())
print("..")
print(s.strip())

#find does not raise and error but index does.

'''

Method	                                                    Description
capitalize()	                        Capitalizes the first character and lowercase the rest.
casefold()	                            Converts the string to lowercase for caseless matching.
center()	                            Centers the string within a specified width.
count()	                                Counts occurrences of a substring in the string.
encode()	                            Converts the string to a specified encoding format.
endswith()	                            Verifies whether the string concludes with the given suffix.
expandtabs()	                        Replaces tab characters with spaces.
find()	                                Provides the smallest index where the specified substring is located, if present.
format()	                            Formats the string into a nicer output.
format_map()	                        Similar to format(), but accepts a dictionary.
index()	                                Returns the lowest index of the substring and raises an error if not found.
isalnum()	                            Checks if all characters are alphanumeric.
isalpha()	                            Checks if all characters are alphabetic.
isdecimal()	                            Checks if all characters are decimals.
isdigit()	                            Checks if all characters are digits.
isidentifier()	                        Checks if the string is a valid identifier.
islower()	                            Checks if all characters are lowercase.
isnumeric()	                            Checks if all characters are numeric.
isprintable()	                        Checks if all characters are printable.
isspace()	                            Checks if all characters are whitespace.
istitle()	                            Checks if the string is titled (capitalized words).
isupper()	                            Checks if all characters are uppercase.
join()	                                Joins iterable elements with the string as a separator.
ljust()	                                Left-justifies in a specified width field.
lower()	                                Converts all characters to lowercase.
lstrip()	                            Trims leading whitespace.
maketrans()	                            Creates a translation table for translate() method.
partition()	                            Divides the string at the initial instance of the separator.
replace()	                            Substitutes instances of one substring with a different one.
rfind()	                                Returns the highest index of the substring.
rindex()	                            Returns the highest index of the substring, raises an error if not found.
rjust()	                                Right-justifies in a specified width field.
rpartition()	                        Splits the string at the last occurrence of the separator.
rsplit()	                            Splits the string at the separator from the right.
rstrip()	                            Trims trailing whitespace.
split()	                                Splits the string at the separator.
splitlines()	                        Splits the string at line breaks.
startswith()	                        Checks if the string starts with the specified prefix.
strip()	                                Trims leading and trailing whitespace.
swapcase()	                            Swaps the case of all characters.
title()	                                Converts the first character of each word to uppercase.
translate()	                            Transforms the string using a translation table.
upper()	                                Converts all characters to uppercase.
zfill()	                                Pads the string with zeros on the left to fill a width.

'''

print('..')
print("nitesh".join(' x '))