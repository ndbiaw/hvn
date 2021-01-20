import os
import requests
import string 
import sys
os.system('cls' if os.name == 'nt' else 'clear')
print("Công cụ hỗ trợ đăng kí tài khoản HentaiVN bởi NDBIAW")
email = input("Nhập gmail của bạn:")
emails = email.replace('@gmail.com', '', 42)
gmail = emails.replace('.', '', 42)
password = input("Nhập mật khẩu của bạn:")
days = input("Nhập ngày sinh của bạn bằng số:")
months = input("Nhập tháng sinh của bạn bằng số:")
years = input("Nhập năm sinh của bạn bằng số:")
names = input("Nhập tên thành viên:")
url = 'https://hentaivn.net/register.php'
gmails = gmail + '@gmail.com'
name = '​' + names
r = requests.post(url, allow_redirects=False, data={
	'email_xacnhan': gmails,
	'username': name,
	'password1': password,
	'password2': password,
	'ngay': days,
	'thang': months,
	'nam': years,
})
