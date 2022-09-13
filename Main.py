from typing import List

def insertionSort(A) -> List[int]:
  # Write your code here
  for i in range(1,len(A)):
    v = A[i]
    j = i-1
    while j>=0 and A[j] > v :
      A[j+1] = A[j]
      j = j-1
    A[j+1] = v
  return A

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
