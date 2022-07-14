import requests
import json
import os


# REGISTER_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"


# register_data = {
#      "phone": "0778989260",
#      "full_name": "Arif Elbis",
#      "password": "123",
#      "password2": "123",
# }

# register_headers = {
#      "Content-Type": "application/json",
#      # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IjA3Nzg5ODkyNTkiLCJleHAiOjE1OTMxMTk1OTMsInBob25lIjoiMDc3ODk4OTI1OSIsIm9yaWdfaWF0IjoxNTkzMTE5MjkzfQ.d6KxDHrzpvW8bbbsBqRag09PiwIp69FbRH9mCOhuo7c'
# }


# r = requests.post(REGISTER_ENDPOINT, data=json.dumps(register_data), headers=register_headers)
# print(r.text)
# print(r.json()['full_name'])

# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

image_path = os.path.join(os.getcwd(), 'icon.png')

credential_header = {
     "Content-Type": "application/json",
}


credential = {
     # "phone": "0778989270",
     # "password": "123",
     "phone": "0778989111",
     "password": "111",
}

# validate = {
#      "phone": "0778989259",
#      "password": "351",
#      "repeat_password": "351",
#      "access_code": "9001",
# }

r = requests.post(AUTH_ENDPOINT, data=json.dumps(credential), headers=credential_header)
# token = r.json()
# token = r.json()['token']
token_json = r.json()
# print("value of token_json")
# print(token_json)
token = ""

print(r.status_code)
if r.status_code == 200:
     # token = token_json['response']['token']
     token = token_json['token']
     print("value of token")
     print(token)
# elif r.status_code == 200 and r.json()['token'] != "User is not activated":
#      token = token_json['token']
#      print(token)
# else:
#      token_error = token_json['detail']
#      print(token_error)
# print(r.status_code)
# print(r.content)
#
BASE_ENDPOINT = "http://127.0.0.1:8000/api/session/"
ENDPOINT      = BASE_ENDPOINT + "36/"
GET_SINGLE_ENDPOINT      = BASE_ENDPOINT + "?q=2"



# order_data = {
#         "id": 66,
#         "order_subtotal": 1190.0,
#         "order_purchase_price_total": 340.0,
#         "order_discount": 0.0,
#         "cash_collected": 1200.0,
#         "change_due": 10.0,
#         "order_item_no": 4,
#         "timestamp": "2020-07-26 19:05:38.226411",
#         "qr_code_string": "FSH202007261POS",
#         "payment_completion_status": 0,
#         "cart_id": 1,
#         "session_id": 1
#     }

session_data_temp = {
     "id": 70,
     "opening_balance": 2000.0,
     "closing_balance": 0.0,
     "order_no": 0,
     "opening_time": "2020-07-27 12:24:52.416149",
     "closing_time": "Unknown time",
     "close_status": 0,
     "session_purchase_price_total": 0.0,
     "net_revenue": 0.0,
     "session_discount": 0.0
}

# shopping_cart_pk            = models.IntegerField()
#     subtotal                    = models.FloatField()
#     cart_purchase_price_total   = models.FloatField()
#     total_discount              = models.FloatField()
#     cart_item_quantity          = models.IntegerField()
#     timestamp                   = models.CharField(max_length=255, null=True, blank=True)
#     checked_out                 = models.BooleanField(default=False)
#     on_hold                     = models.BooleanField(default=False)

# category_data = {
#      # "id": 98,
#      "category_pk": 24,
#      "name": "Apple8",
#      "include_in_drawer": 1,
#      "pos_backup": 2,
# }

# shoppin_cart_data = {
#      'shopping_cart_pk': 88,
#      'subtotal': 8999,
#      'cart_purchase_price_total': 18999,
#      'total_discount': 200,
#      'cart_item_quantity': 10,
#      'timestamp': "today bro",
#      # 'checked_out': 1,
#      # 'on_hold': 0,
#      'pos_backup': 19,
# }

# pos_data = {
#      "id": 36
#      # "version_name": "version4",
# }


headers = {
     # "Content-Type": "application/json",
     "Authorization": "JWT " + token
}

with open(image_path, 'rb') as image:
     file_data = {
          'picture': image
     }
     # r = requests.get(BASE_ENDPOINT, headers=headers)
     # r = requests.get(GET_SINGLE_ENDPOINT, headers=headers)
     # r = requests.get(ENDPOINT, headers=headers)
     # r = requests.put(ENDPOINT, data=data2, headers=headers)
     # r = requests.delete(ENDPOINT, headers=headers)
     # print(r.text)
     # r = requests.post(BASE_ENDPOINT, data=data2, headers=headers, files=file_data)
     r = requests.post(BASE_ENDPOINT, data=session_data_temp, headers=headers)
     print("response of .....")
     print(r.text)
     print(r.status_code)
     # print(r.text['id'])
     # print(r.json())
     
     
#############################################################

# with open(image_path, 'rb') as image:
#      file_data = {
#           'icon': image
#      }
#      # r = requests.get(ENDPOINT, headers=headers2)
#      # print(r.text)
#      # r = requests.put(ENDPOINT, data=data2, headers=headers2, files=file_data)
#      # r = requests.put(ENDPOINT, data=data2, headers=headers2)
#      # r = requests.delete(ENDPOINT, data=data2, headers=headers2)
#      # print(r.text)
#      # r = requests.post(BASE_ENDPOINT, data=data2, headers=headers2, files=file_data)
#      # print(r.text)
#      # r = requests.post(BASE_ENDPOINT, data=data2, headers=headers2)
#      # r1 = requests.post(BASE_ENDPOINT, data=data3, headers=headers2)
#      print(r.text)
#      # print(r1.text)



# headers = {
#      "Content-Type": "application/json",
#      "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMiwidXNlcm5hbWUiOiIwNzc4OTg5MjcwIiwiZXhwIjoxNTkyOTIwMjcwLCJwaG9uZSI6IjA3Nzg5ODkyNzAiLCJvcmlnX2lhdCI6MTU5MjkxOTk3MH0.gOKMlkjdLlxOR72jEuMHx3gMyr4vTTf8UZ5eXqKyVL4', 'expires': '2020-06-30T13:42:50.075238Z'
# }

# data = {
#      "phone": "0778989270",
#      "full_name": "Elbis7",
#      "password": "123",
#      "password2": "123",
# }

# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()
# print(token)

# headers1 = {
#      "Content-Type": "application/json",
#      "Authorization": "JWT " + token
# }
# headers_with_file = {
#      # "Content-Type": "application/json",
#      "Authorization": "JWT " + token
# }

# # post_data=json.dumps({"category_pk": "21", "name": "this post is with jwt"})
# # posted_response = requests.post(ENDPOINT, data=post_data, headers=headers1)

# with open(image_path, 'rb') as image:
#      file_data = {
#           'icon': image
#      }
#      post_data = {
#           "category_pk": "21", 
#           "name": "this post is with jwt"
#      }

#      posted_response = requests.post(ENDPOINT, data=post_data, headers=headers_with_file, files=file_data)
#      print(posted_response.text)

# print(r.json())
# print(r.json()['token'])

# refresh_data = {
#      "token": token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()

# print(new_token)

# def do_img(method = "get", data={}, is_json = True, img_path=None):
#      headers = {}
#      if is_json:
#           headers['content-type'] = "application/json"
#           data = json.dumps(data)
#      if img_path is not None:
          # with open(image_path, 'rb') as image:
          #      file_data = {
          #           'icon': image
          #      }
#                r = requests.request(method, ENDPOINT, files=file_data, data=data, headers=headers)
#      else:
#           r = requests.request(method, ENDPOINT, data=data, headers=headers)
#      print(r.text)
#      print(r.status_code)
#      return r

# do_img(method="post", data={"category_pk": "21", "name": "this post2 with image", "user": 1}, is_json=False, img_path=image_path)

# def do(method = "get", data={}, id=3, is_json = True):
#      headers = {}
#      if is_json:
#           headers['content-type'] = "application/json"
#           data = json.dumps(data)
#      r = requests.request(method, ENDPOINT, data=data, headers=headers)
#      print(r.text)
#      print(r.status_code)
#      return r

# do()
# do(data={"id": 77})

# do(method="put", data={"id": 5, "category_pk": "333", "name": "this is from endpont", "user": 1})
# do(method="put", data={"category_pk": "23", "name": "this post is from endpoint", "user": 1})
# do(method="delete", data={"id": 6})




