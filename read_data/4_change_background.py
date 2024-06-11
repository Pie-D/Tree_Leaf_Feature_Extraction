import os
import requests

# Thay 'Your-Remove-BG-API-Key' bằng API Key thực tế của bạn từ remove.bg
api_key = ''

# Đường dẫn đến thư mục chứa các ảnh cần xử lý
input_folder = 'datasetflower/cornus_mas/'

# Đường dẫn đến thư mục chứa ảnh sau khi xử lý
output_folder = 'cornus_mas_pre/'

# Tạo thư mục lưu trữ ảnh sau khi xử lý nếu nó không tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Biến đếm để đổi tên ảnh
count = 1

# Lặp qua tất cả các tệp trong thư mục đầu vào
for filename in os.listdir(input_folder):
    # Kiểm tra xem tệp có phải là tệp ảnh hay không
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, f"{count}.png")  # Đổi tên thành số

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(input_image_path, 'rb')},
            data={'size': 'auto', 'bg_color': 'black'},  # Thêm bg_color để đặt màu nền mới
            headers={'X-Api-Key': api_key},
        )

        if response.status_code == requests.codes.ok:
            with open(output_image_path, 'wb') as out:
                out.write(response.content)
            count += 1  # Tăng biến đếm
        else:
            print("Lỗi:", response.status_code, response.text)
