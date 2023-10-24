#  index = key % arraySize


def hashFunc1 ( key, arraySize ):
  hashVal = 0
  pow26 = 1

  for j in range (len(key) - 1, -1, -1):
    letter = ord (key[j]) - 96
    hashVal += pow26 * letter
    pow26 *= 26

  return hashVal % arraySize


def hashFunc2 ( key, arraySize ):
  hashVal = 0
  for j in range (len(key)):
    letter = ord (key[j]) - 96
    hashVal = (hashVal * 26 + letter ) % arraySize
  return hashVal


def main():
  print('Your value for your UT EID is', hashFunc2('dxl85', 5))

if __name__ == '__main__':
  main()