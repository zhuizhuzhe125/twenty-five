'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
'''
激活码， 总共十六位， 每四位为一组，
比如: 
'ZDUP-Pb5i-Lg7I-br4K', 'Sbnq-wSN8-eKIS-nrAF', 
'fVzj-l6xj-LiWw-Vpnf', 'qgWZ-6xAU-t945-Abq7', 
'e5qp-9ZbN-dJeu-UpIE', 'U6FW-A1bN-Q9oi-kpaM', 
'''
# 导入库
import string, random

#激活码中的字符和数字
field = string.ascii_letters + string.digits
'''
首先用变量保存 字母和数字的集合
ascii_letters: 生成所有字母，从a-z和A-Z,
digits: 是生成所有数字0-9.
'''

#获得四个字母和数字的随机组合
def getRandom():
    return "".join(random.sample(field,4))
'''
利用 sample 从 field中随机获得 4 个字符
sample(m, n): 从序列m中选择n个随机且独立的元素
join: 将序列中的元素以指定的字符连接生成一个新的字符串
'''

#生成的每个激活码中有几组
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])
'''
每循环一次，就调用一次 getRandom() 然后得到返回值。
再用jion方法将返回值拼接。
'''

#生成n组激活码
def generate(n):
    return [concatenate(4) for i in range(n)]
'''

'''

if __name__ == '__main__':
    print(generate(10))

