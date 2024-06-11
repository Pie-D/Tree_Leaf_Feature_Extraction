import numpy as np

# Đọc tệp .npy
file_path = './hog.npy'
data = np.load(file_path, allow_pickle=True)
# np.set_printoptions(threshold=np.inf)
print(data[0][1])
# for i in data[0][1]:
#     if (i > 0):
#         print(i, end="
