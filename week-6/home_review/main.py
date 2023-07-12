import numpy as np

arr = np.array(
    [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36],
    ]
)

for i in range(6):
    # print(arr[i, :])
    print(f"Sum row {i+1}  : {np.sum(arr[i, :])}")

print("=================================================================")

for i in range(6):
    # print(arr[:, i])
    print(f"Sum row {i+1}  : {np.sum(arr[:, i])}")

#        row   column
# print(arr[3:, 3:])

print("blue:", np.sum(arr[:3, :3]))
print("yellow:", np.sum(arr[3:, :3]))
print("red:", np.sum(arr[:3, 3:]))
print("green:", np.sum(arr[3:, 3:]))
