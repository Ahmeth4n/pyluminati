import random
import os

class PyLuminati:

    def __init__(self,protocol=None):
        self.proxy_username = os.environ['PROXY_USERNAME']
        self.proxy_password = os.environ['PROXY_PASSWORD']
        self.country = os.environ['PROXY_COUNTRY']
        self.port = 22225
        self.luminati_session_id = abs(random.getrandbits(64))
        self.protocol = protocol

    def renew_session(self):
        self.luminati_session_id = abs(random.getrandbits(64))

    def luminati(self):
        if self.protocol is None:
            proxy_dict = {
                "http" : self.get_proxy("http"),
                "https" : self.get_proxy("https")
            }
        else:
            proxy_dict = {
                self.protocol: self.get_proxy(self.protocol)
            }

        return proxy_dict

    def get_proxy(self,protocol):
        luminati_url = "%s://%s%s-session-%s:%s@zproxy.lum-superproxy.io:%d" % (
            protocol,
            self.proxy_username,
            f"-country-{self.country}" if self.country else "US",
            self.luminati_session_id,
            self.proxy_password,
            self.port,
        )
        return luminati_url