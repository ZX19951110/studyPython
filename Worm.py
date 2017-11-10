# -*- coding:utf-8 *-
import requests
res = requests.get('http://google.it')
print(res.encoding,res.status_code,res.cookies)

# def test(str):
#     length = len(str)
#     output = ''
#     if str[0] == '-':
#         output += '-'
#         while (length > 1):
#             output += (str[length-1])
#             length -= 1
#         print(output)
#     else:
#         while (length > 0):
#             output += (str[length - 1])
#             length -= 1
#         print(output)
#  test('123456789123')
# test('-210')