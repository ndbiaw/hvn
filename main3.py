import os
import requests
import string 
import sys
def registration():
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
def inputname():
	names = input("Nhập tên thành viên:")
	if len(names) > 24:
		print("Tên thành viên không được dài quá 24 kí tự!")
	if len(names) < 25:
		registration()
def inputyear():
	years = input("Nhập năm sinh của bạn bằng số:")
	if years.isdigit():
		inputname()
	if years.isalpha:
		print("Vui lòng nhập chính xác năm sinh của bạn bằng số")
		sys.exit()
def inputmonth(months, minimum=1, maximum=12):
	months = input("Nhập tháng sinh của bạn bằng số:")
	if months.isdigit():
		inputyear()
	if months.isalpha:
		print("Vui lòng nhập chính xác tháng sinh của bạn bằng số")
def inputday(days, minimum=1, maximum=31):
	days = input("Nhập ngày sinh của bạn bằng số:")
	if days.isdigit():
		inputmonth()
	if months.isalpha: 
		print("Vui lòng nhập chính xác ngày sinh của bạn bằng số")
		sys.exit()
def inputpassword():
	password = input("Nhập mật khẩu của bạn:")
	if len(password) < 8:
		print("Mật khẩu phải có từ 8 kí tự trở lên!")
	sys.exit()
	if len(password) > 7:
		inputday()
def inputemail():
	email = input("Nhập gmail của bạn:")
	if len(email) > 42:
		print ("Xin hãy nhập định dạng gmail hợp lệ!")
	if len(email) < 43:
		emails = email.replace('@gmail.com', '', 42)
		gmail = emails.replace('.', '', 42)
		inputpassword()
def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Công cụ hỗ trợ đăng kí tài khoản HentaiVN bởi NDBIAW")
	inputemail()
