# PyLuminati
A small class written for you to use luminati proxy service with python. A similar script is available in pip, but since I saw some deficiencies myself, I wrote a class for myself.

in order to use class, you need to define `PROXY_USERNAME`, `PROXY_PASSWORD`, `PROXY_COUNTRY` information in **environment variables**.

![proxy environment](https://github.com/ahmeth4n/pyluminati/blob/main/img/proxy_environment.png?raw=true)

# Example Usage

```
pyluminati_proxy = PyLuminati()
proxies = pyluminati_proxy.luminati()
r = requests.get("https://api.myip.com/",verify=False,proxies=proxies)
print(r.text)
```
