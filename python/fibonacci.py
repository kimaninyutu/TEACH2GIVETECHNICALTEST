def fibonacci(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(100))
