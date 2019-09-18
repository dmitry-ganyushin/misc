def smallest_subarray_with_given_sum(s, arr):
    for k  in range (1, len(arr)): # win size
        for index in range(0, len(arr) -k +1): # starting index of a window
          sum = 0
          for i in range(index, index + k):
              sum += arr[i]
          if sum >= s :
            return k


  # TODO: Write your code here
    return -1


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
