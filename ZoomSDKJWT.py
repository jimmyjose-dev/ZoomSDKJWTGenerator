import jwt
from datetime import timedelta, datetime
from time import mktime, time


class ZoomSDKJWT:
   

    def __init__(self, sdk_key, sdk_secret):
 
        self.sdk_key = sdk_key
        self.sdk_secret = sdk_secret
       

    def generate_token(self):
 
        iat = int(mktime(datetime.now().timetuple()))
        exp = int(mktime((datetime.today() + timedelta(days=1)).timetuple()))
        tokenExp = int(
            mktime((datetime.today() + timedelta(hours=1)).timetuple()))
        encode = jwt.encode(
            {"appKey": self.sdk_key, "iat": iat, "exp": exp, "tokenExp": tokenExp},
            self.sdk_secret,
            algorithm="HS256",
            headers={"typ": "JWT"},
        )
        return encode.decode("utf-8")


zoom_sdk = ZoomSDKJWT("","")
print(zoom_sdk.generate_token())
