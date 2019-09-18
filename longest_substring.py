# This is wrong
import collections
def longest_substring_with_k_distinct(str, k):
    for win_size in range(1, len(str)):
        for index in range(0, len(str) - win_size):
            substr=str[index : index + win_size]
            if len(collections.Counter(substr)) >=k:
                return str[index : index + win_size]  
 
    # TODO: Write your code here
    return -1

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()