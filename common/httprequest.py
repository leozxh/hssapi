import  requests


#定义请求方法
class http_request:

    def http_get(url,params,headers=None):
        res = requests.get(url,params,headers=headers)
        return res

    def http_post(url,params,cookies = None):
        res = requests.post(url,params,cookies = cookies)
        return res
