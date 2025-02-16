# import requests
# import random
# import hashlib
#
#
# class BaiDuFanYi:
#     def __init__(self, appKey, appSecret):
#         self.url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
#         self.appid = appKey
#         self.secretKey = appSecret
#         self.fromLang = 'auto'
#         self.toLang = 'zh'
#         self.salt = random.randint(32768, 65536)
#         self.header= dict({"Content-Type":"application/x-www-form-urlencoded"})
#
#     def BdTrans(self, text, rep):
#         sign = self.appid + text + str(self.salt) + self.secretKey
#         md = hashlib.md5()
#         md.update(sign.encode(encoding='utf-8'))
#         sign = md.hexdigest()
#         data = {
#             'appid': self.appid,
#             'q': text,
#             'from': self.fromLang,
#             'to': self.toLang,
#             'salt': self.salt,
#             'sign': sign
#         }
#         response = req.post(self, params=data, headers=self.header)
#
#         text = requests.json()
#         results = text['trans_result'][0]['dst']
#         return results
#
#
# if __name__ == '__main__':
#     appKey = '20250216002275064'
#     appSecret = 'K6bzR1FcFnbSzoTTxwuI'
#     BaiDuFanYi_test = BaiDuFanYi(appKey, appSecret)
#     word = input('Enter you word:\n')
#     Results = BaiDuFanYi_test.BdTrans(word,requests)
#     print('Means:\n', Results)

import requests
import random
import hashlib


class BaiDuFanYi:
    def __init__(self, appKey, appSecret):
        """
        初始化百度翻译类

        :param appKey: 百度翻译API的应用ID
        :param appSecret: 百度翻译API的应用密钥
        """
        self.url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
        self.appid = appKey
        self.secretKey = appSecret
        self.fromLang = 'auto'
        self.toLang = 'zh'
        self.salt = random.randint(32768, 65536)
        self.header= dict({"Content-Type":"application/x-www-form-urlencoded"})

    def generate_sign(self, text):
        """
        生成百度翻译API的签名

        :param text: 需要翻译的文本
        :return: 生成的签名
        """
        sign = self.appid + text + str(self.salt) + self.secretKey
        md = hashlib.md5()
        md.update(sign.encode(encoding='utf-8'))
        return md.hexdigest()

    def BdTrans(self, text, req):
        """
        调用百度翻译API进行文本翻译

        :param text: 需要翻译的文本
        :param req: requests库的实例
        :return: 翻译后的文本
        """
        sign = self.generate_sign(text)
        data = {
            'appid': self.appid,
            'q': text,
            'from': self.fromLang,
            'to': self.toLang,
            'salt': self.salt,
            'sign': sign
        }
        response = req.post(self.url, params=data, headers=self.header)

        if response.status_code == 200:
            text = response.json()
            results = text['trans_result'][0]['dst']
            return results
        else:
            raise Exception(f"请求失败，状态码: {response.status_code}")


if __name__ == '__main__':
    appKey = ''
    appSecret = ''
    BaiDuFanYi_test = BaiDuFanYi(appKey, appSecret)
    word = input('Enter you word:\n')
    Results = BaiDuFanYi_test.BdTrans(word, requests)
    print('Means:\n', Results)
