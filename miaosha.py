import selenium
from selenium import webdriver
import datetime
import time

# 启动火狐浏览器的驱动器
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()

# 传入用户名密码，登录淘宝
def login():
    # 打开淘宝
    driver.get("https://www.taobao.com")

    # 查找文本，登录
    if driver.find_element('link text', "亲，请登录"):
        driver.find_element('link text', "亲，请登录").click()

    print("请在30秒内完成扫码登录")
    time.sleep(30)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    # 点击购物车里全选按钮
    if driver.find_element("id","J_SelectAll1"):
        driver.find_element("id","J_SelectAll1").click()
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    count = 0
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        count += 1
        if now >= buytime:
            try:
                # 点击结算按钮J_Go
                if driver.find_element("id","J_Go"):
                    driver.find_element("id","J_Go").click()
                    submit()
            except:
                pass
        if count == 50:
            print(now)
            count = 0

        time.sleep(0.01)


def submit():
    while True:
        try:
            if driver.find_element('link text', "提交订单"):
                driver.find_element('link text', "提交订单").click()
                now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                print("抢购成功时间：%s" % now1)
                break
        except:
            print("再次尝试提交订单")
            time.sleep(0.01)


if __name__ == "__main__":
    print("请先将秒杀物品加入购物车并保证购物车内仅有秒杀物品, 再打开手机淘宝扫一扫，最后键盘回车进行下一步")
    a = input()
    print("请按以下格式输入秒杀时间 xxxx-xx-xx xx:xx:xx 比如 2022-08-11 21:00:00  并回车")
    x = str(input())
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if now >= x:
        print("时间格式错误或早于当前时间")
        time.sleep(60)
        raise KeyboardInterrupt()
    login()
    # 设置抢购时间
    while 1:
        buy(x)