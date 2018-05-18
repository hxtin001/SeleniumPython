# -*- coding: utf-8 -*-
web_address = 'https://console.cloud.google.com/projectselector/home/dashboard?cloudshell=true&supportedpurview=project&project&folder&organizationId'
path_chrome = r'/usr/bin/google-chrome'
path_chromedriver = '/home/hxtin001/Documents/Project/software/chromedriver'
path_application_log = '/home/hxtin001/Documents/Project/Selenium/logs/application.log'
xpath_oneway = "//*[@id='oneway']"
xpath_round = "//*[@id='round']"
xpath_datepicker = '//div[@id="ui-datepicker-div"]//td[@data-year="YEAR"][@data-month="MONTH"]/a[@class="ui-state-default"][text()="DAY"]'
commandline_crontab = '/home/hxtin001/Documents/VirtualProject/SeleniumPythonTest/bin/python /home/hxtin001/Documents/Project/Selenium/SeleniumPython.py'
xpath_calendar = "//*[@id='searchform']/div/div[3]/ul/li[1]/p/img"
xpath_outward_time_zone = "//*[@id='searchform']/div/div[3]/ul/li[1]/select"
xpath_submit_button = '//*[@id="searchform"]/div/p[1]/a'
xpath_flight = '//*[@id="flight_ANA985HNDITM"]/span'
xpath_sample_ANA985HNDITM = '//*[@id="sample_ANA985HNDITM"]/td/table/tbody/tr/td/table/tbody/tr[1]/td[4]/a/span'
xpath_submit_button2 = '//*[@id="input_form"]/p[2]/a'
id_adult_num = "occu01"
id_child_num = "occu02"
id_infant_num = "occu03"
id_domestic_air_seat00 = "domestic_air_seat00"
id_domestic_air_seat01 = "domestic_air_seat01"
id_domestic_air_seat02 = "domestic_air_seat02"
id_list_port_depart = 'header_col_dept_value'
id_list_port_arrive = 'header_col_arrive_value'
id_date_booking = "header_outward_date_value"
id_registry_button = "registry_button"
id_city_depart = 1
id_city_arrive = 5
id_input_no_email = "no_member_mail"
id_family_name =  'family_name_kana1'
id_first_name = 'first_name_kana1'
id_year_of_birth = 'year_of_birth1'
id_month_of_birth = 'month_of_birth1'
id_day_of_birth = 'day_of_birth1'
id_card_number = 'card_number_new'
id_card_holder_name = 'card_holder_name'
id_card_holder_name_new = 'card_holder_name_new'
id_male = 'male1'
id_tel_num1 = 'tel_num11'
id_tel_num2 = 'tel_num21'
id_tel_num3 = 'tel_num31'
id_security_code_new = 'security_code_new'
id_security_code = 'security_code'
id_family_name_kanji = 'member_family_name_kanji'
id_first_name_kanji = 'member_first_name_kanji'
id_family_name_kana = 'member_family_name_kana'
id_first_name_kana = 'member_first_name_kana'
id_member_email_re_enter  = 'member_email_re_enter'
id_password = 'password'
id_password_re_enter  = 'password_re_enter'
id_member_male = 'member_male'
id_member_year_of_birth = 'member_year_of_birth'
id_member_month_of_birth = 'member_month_of_birth'
id_member_day_of_birth = 'member_day_of_birth'
id_app_re_enter = 'applicant_email_re_enter'
# id_member_kiyaku = 'MemberKiyaku'
id_pay_kiyaku = 'PayKiyaku'
id_joken = 'Joken'
id_cancel = 'cancel'
id_submit = 'submit'
id_member_mail = 'member_mail'
id_member_password = 'mem_pass'
id_login_btn = 'login_button'
list_city = {1: "TYO", 2: "HND", 3: "NRT", 4: "OSA", 5: "ITM", 6: "KIX", 7: "CTS", 8: "NGO", 9: "FUK", 11: "OKA"}
list_name = {1: "ミア".decode('utf-8'), 2: "ミヤ".decode('utf-8'), 3: "ナナミ".decode('utf-8'), 4: "アシタ".decode('utf-8'), 5: "ベタ".decode('utf-8'), 6: "アンア".decode('utf-8'), 7: "キミ".decode('utf-8'), 8: "ララ".decode('utf-8'), 9: "チナ".decode('utf-8'), 10: "ヤマ".decode('utf-8')}
list_alphabet_name = {1: "KALI", 2: "MIZI", 3: "HANA", 4: 'MARI', 5: "SUSHI", 6: "LILI", 7: "BABI", 8: 'NAMI', 9: "HELI"}
marionette = 'marionette'
day_default = "10"
month_default = "1" #month from 0 to 11
year_default = "2017"
outward_time_zone_default = "1" #outward time zone from 0 to 3
adult_num_default = "1" #adult number from 1 to 6
child_num_default = "0" #child number from 0 to 4
infant_num_default = "0" #infant number from 0 to 2
screen_width_default = 1024 #Running error if size unsuitable
screen_height_default = 768
email = "hxtin002@evo.vn"
password_default = '123456'
first_name_default = 'ミミ'.decode('utf-8')  #Website not eccept romaji
family_name_default =  'ミミ'.decode('utf-8')
card_number_default = '4200000000000000'
card_holder_name_default = 'MIMI MIMI'
tel_num11_default = '090'
tel_num21_default = '4831'
tel_num31_default = '4723'
year_of_birth_default = '1990'
month_of_birth_default = '10'
day_of_birth_default = '20'
security_code_defualt = '123'
# 藤田　泉岐             mizuki fujita
family_name_kanji_default = '藤田'.decode('utf-8')     # Just accept japanese
# family_name_kana_default = 'ミミ'.decode('utf-8')   #Mizuki
first_name_kanji_default =  '泉岐'.decode('utf-8')
# first_name_kana_default = 'ミミ'.decode('utf-8')    #fujta