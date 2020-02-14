#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        # creating hashvalue by passing ht, and its current limit minus the current weight by index
        hashVal = hash_table_retrieve(ht, limit - weights[i])
        # check to see if the hash is 
        if hashVal is not None:
            a = (i, hashVal)
            print(a)
            return a
        else:
            hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
