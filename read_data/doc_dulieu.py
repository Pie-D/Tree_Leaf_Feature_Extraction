import numpy as np

# Đọc tệp .npy
file_path = './concat_hsv_hog.npy'
data = np.load(file_path, allow_pickle=True)
# np.set_printoptions(threshold=np.inf)
# count = 0
# with open("output.txt", "w") as f:
#     for i in data[0][1]:
#         f.write(f"{i}   ")
#         if count > 500:
#             f.write(f"\n")
#             count = 0
#         count += 1
print(data)
