from faker import Faker

fake = Faker(locale='en_CA')

# --------------------data session-------------------------
home_page_url = 'https://advantageonlineshopping.com/#/'
# home_page_title = ' Advantage Shopping'
home_page_title = '\xa0Advantage Shopping'
first_name = fake.first_name()
last_name = fake.last_name()
new_user_name = f'{first_name}{last_name}'.lower()[:15]
new_email = f'{new_user_name}@{fake.free_email_domain()}'
new_password = fake.password()
confirm_password = new_password
phone = fake.phone_number()
country = fake.current_country()
city = fake.city()
address = fake.street_address().replace('\n', ' ')
province = fake.province()[:5]
postal_code = fake.postcode()
subject = fake.sentence(nb_words=100)
account_first_name=first_name.capitalize()
account_last_name=last_name.capitalize()
account_full_name=f'{account_first_name} {account_last_name}'
sp_username='Spuser'
sp_password='Pass123'

list_opt = ['Username', 'Email', 'Password', 'Confirm password',
            'First Name', 'Last Name', 'Phone Number',
            'City', 'Address', 'Province', 'PostalCode']
list_names = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
              'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
              'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
              'postal_codeRegisterPage']
list_val = [new_user_name, new_email, new_password, new_password,
            first_name, last_name, phone,
            city, address, province, postal_code]

homepage_texts=['SPEAKER','TABLES','LAPTOPS','MICE','HEADPHONES']
homepage_textid=['speakersTxt','tabletsTxt','laptopsTxt','miceTxt','headphonesTxt']
homepage_menu=['SPECIAL OFFER','POPULAR ITEMS','CONTACT US']

fb_page_url='https://www.facebook.com/MicroFocus/'
tw_page_url='https://twitter.com/MicroFocus'
in_page_url='https://www.linkedin.com/company/unavailable/'

item1_name='HP Elite x2 1011 G1 Tablet'
item2_name='HP ELITEPAD 1000 G2 TABLET'
# print(list_val)
