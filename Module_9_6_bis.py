
import itertools


def get_list_partitions(string):
    partitions = []

    # list of binary sequences
    binary_sequences = ["".join(seq) for seq in itertools.product("01", repeat=len(string) - 1)]

    # go over every binary sequence (which represents a partition)
    for sequence in binary_sequences:
        partition = []

        # current substring, accumulates letters until it encounters "1" in the binary sequence
        curr_substring = string[0]
        for i, bit in enumerate(sequence):
            # if 0, don't partition. otherwise, add curr_substring to the current partition and set curr_substring to be the next letter
            if bit == '0':
                curr_substring = curr_substring + string[i + 1]
            else:
                partition.append(curr_substring)
                curr_substring = string[i + 1]

                # add the last substring to the partition
        partition.append(curr_substring)

        # add partition to the list of partitions
        partitions.append(partition)

    return partitions

print(get_list_partitions("abc"))