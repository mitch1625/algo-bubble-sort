sequence = [4, 3, 5, 0, 1]


def bubble_sort(sequence):
    swaps = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)-1):
            if sequence[j] > sequence[j+1]:
                current = sequence[j]
                sequence[j] = sequence[j+1]
                sequence[j+1] = current
            print(sequence)
            swaps+=1
    result = sequence
    print(f"Final result: {result}")
    print(f"Swaps: {swaps}")



bubble_sort(sequence)




# def bubble_sort(sequence):
#     swaps = 0
#     for i in range(len(sequence)):
#         for j in range(len(sequence)-1):
#             print(sequence)
#             print(f'Comparing {sequence[i]} to {sequence[j]}')
#             if sequence[i] < sequence[j]:
#                 temp = sequence[i]
#                 sequence[i] = sequence[j]
#                 sequence[j] = temp
#                 swaps+=1
#     result = sequence
#     print(f"Final result: {result}")
#     print(f"Swaps: {swaps}")


# bubble_sort(sequence)