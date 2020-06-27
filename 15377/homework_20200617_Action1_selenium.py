from selenium import webdriver
import pandas as pd


def get_data(url=None,num = None):
    print(url)
    if url is None or num is None:
        raise Exception("Please check the arguments you putted into this function!")
    browser = webdriver.Safari()
    browser.maximize_window()
    result_list = []
    for i in range(1,num+1):
        browser.get(url_f+str(i)+url_b)
        raw_father_element = browser.find_elements_by_css_selector('div.tslb_b tr')
        _ = raw_father_element.pop(0)
        for ele in raw_father_element:
            car_status_list = []
            raw_tr_elements = ele.find_elements_by_css_selector('td')
            for tr_tle in raw_tr_elements:
                car_status_list.append(tr_tle.text)
            result_list.append(car_status_list)
    result_df = pd.DataFrame(data=result_list,
                             columns=['投诉编号','投诉品牌','投诉车系','投诉车型',
                                      '问题简述','典型问题','投诉时间','投诉状态'])
    browser.close()
    return result_df


if __name__ == '__main__':
    url_f = r'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
    url_b = r'.shtml'
    num = 5
    result = get_data([url_f, url_b],num)
    print(result)
