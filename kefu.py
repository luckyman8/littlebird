# 任务2：模拟淘宝客服自动回复

def find_answer(question):
    with open('reply.txt','r') as f :
        while True:
            line=f.readline()
            if  not line:   #也可以为if  line==''
                break
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
        return '对不起，没有你想要找的问题'

if __name__ =='__main__':
    question=input('请输入想要提问的内容：')
    while True:
        if question=='bye':
            break
        reply=find_answer(question)
        if not reply:
            question=input("小蜜不懂您在说什么，您可以问一些与订单、账户和支付相关的内容（退出请输入bye）：")
        else:
            print(reply)
            question=input("您可以问一些与订单、账户和支付相关的内容（退出请输入bye）：")
    print('谢谢，再见！')
