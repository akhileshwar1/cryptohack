from matrix_e1b463dddbee6d17959618cf370ff1a5 import matrix2bytes

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    result = []
    for i in range(0, len(s)):
        list = []
        for j in range(0, len(s[i])):
            list.append(s[i][j] ^ k[i][j])
        
        result.append(list)

    return matrix2bytes(result)



print(add_round_key(state, round_key))
