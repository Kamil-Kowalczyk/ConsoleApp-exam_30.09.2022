import random

def main():
    array = gen_random_numbers()
    searched_number = int(input("Enter a number between 1-100 to find:\n"))
    print(f"Array elements:\n {array}")
    index_in_array = search_for(searched_number, array)
    if index_in_array >= 0:
        print(f"Your searched number index is: {index_in_array}")
        print(array[index_in_array])
    else:
        print("There is no number like you have typed")

def gen_random_numbers():
    array = []
    for i in range(0, 50):
        array.append(random.randint(1, 100))
    return array

def search_for(searched_number, array):
    array.append(searched_number)
    for i in range(0, len(array)):
        if array[i] == searched_number:
            index = i
            if index == len(array) - 1:
                return -1
            else:
                return index



if __name__ == "__main__":
    main()
