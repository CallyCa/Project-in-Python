from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = input('Digitar grupo: ')
msg = input('Digitar mensagem: ')
count = int(input('Enter the count : '))

input('Scanear QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('compose-btn-send').click()
