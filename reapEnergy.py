#coding:utf-8
import time

import yaml
from appium import webdriver


def datas():
    with open("../data/zhifubaoReap.yaml", encoding='utf8') as f:
        caselist = yaml.safe_load(f)
    return caselist
# print(datas()[0]["cases"][0])

class zhifubao():
    def __init__(self):
        desirad_caps = {}
        desirad_caps["deviceName"] = 'b4f61229'
        desirad_caps["platformName"] = 'Android'
        desirad_caps["platformVersion"] = '10'
        desirad_caps["appPackage"] = 'com.eg.android.AlipayGphone'
        desirad_caps["appActivity"] = '.AlipayLogin'
        desirad_caps["noReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desirad_caps)
        time.sleep(1)

    # 获取屏幕分辨率
    def get_screen_size(self):
        x = self.driver.get_window_size()['width']  # 获取屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取屏幕高度
        return (x, y)

    # 单独通过绝对坐标点击
    def tap_alone(self, x, y, duration=1000):
        self.driver.tap([(x, y),(x, y)], duration)
        # print("点击坐标" + str(x) + "," + str(y))

    # 收取能量
    def getEnergy(self):
        """
        x除于1080等与x轴的实际比例
        y除于2310等于y轴的实际比例
        start_x、end_x、start_y、end_y设定指定范围
        """
        screen_x, screen_y = self.get_screen_size()
        start_x = int(float(130/1080)*screen_x)
        end_x = int(float(945/1080)*screen_x)
        start_y = int(float(564/2208)*screen_y)
        end_y = int(float(830/2208)*screen_y)
        for i in range(start_x, end_x, 100):
            for j in range(start_y, end_y, 100):
                # print("点击坐标"+str(i)+","+str(j))
                self.tap_alone(str(i), str(j))

    def getSize_y(self):
        """
        太恶心了这玩意儿，使用xpath或link_text都定位不到
        :return:
        """
        # self.driver.find_element_by_xpath("//*[@text='查看']")
        # hh = self.driver.find_element_by_xpath("//*[@text='最新动态']")
        x, y = self.get_screen_size()
        if int(y) <= 2208:
            return "1575"
        else:
            return "1575"


    # 判断是否有可偷的能量
    def isSteal(self):
        """
        没有能量可以偷取返时
        :return: False
        """
        text = self.driver.find_element_by_id("com.alipay.mobile.nebula:id/h5_tv_title").text
        if "蚂蚁森林" == text:
            print("没有能量可以偷取啦！，过会儿再来看看")
            return False
        else:
            name = text.split("的蚂蚁森林")[0]
            print("偷取" + name + "的能量")
            return True

    def run(self):
        #进入蚂蚁森林
        self.driver.find_element_by_xpath("//*[@text='蚂蚁森林']").click()
        time.sleep(3)
        # 收取自己能量
        self.getEnergy()
        print("收取自己的能量成功")
        # 获取屏幕大小，算出比例值
        x, y = self.get_screen_size()
        print("屏幕大小为:"+"宽"+str(x)+"长"+str(y))
        findEnergy_x = str(float(950/1080)*x)
        findEnergy_y = self.getSize_y()
        self.tap_alone(findEnergy_x, findEnergy_y)
        # 循环查找下一个有能量的小伙伴
        while self.isSteal():
            self.getEnergy()
            self.tap_alone(findEnergy_x, findEnergy_y)


if __name__ == "__main__":
    r = zhifubao()
    r.run()