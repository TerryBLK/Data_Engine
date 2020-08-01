from selenium import webdriver
import requests
import pandas as pd


def download_data(res_df):
    # Lunch the webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--o-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)

    # get into http://car.bitauto.com/xuanchegongju/?l=8&mid=8
    browser.get("http://car.bitauto.com/xuanchegongju/?l=8&mid=8")

    # locate the location of those information we need
    ele_list = browser.find_elements_by_xpath("//div[@class='search-result-list']/div")
    for elem in ele_list:
        info_list = elem.find_element_by_css_selector("a").text.split("\n")
        if info_list[-1] == "暂无":
            info_list[-1] = "-"
            info_list.append("-")
        else:
            temp_list = info_list[-1].strip("万").split("-")
            info_list[-1] = temp_list[0]
            info_list.append(temp_list[1])
        info_list.append(elem.find_element_by_class_name("img").get_attribute("src"))
        res_df.loc[len(res_df)] = info_list
    browser.quit()
    return res_df


def download_pic(res_df):
    for i in range(len(res_df)):
        req = requests.get(res_df.loc[i][3])
        if req.status_code == 200:
            with open("./Img/" + res_df.loc[i][0] + ".jpg", "wb") as img:
                img.write(req.content)
        else:
            continue
    return res_df


def main():
    # Create a DataFrame to store data
    res_df = pd.DataFrame(columns=["Model", "bottom_price", "peak_price", "links"])
    # print(res_df)

    # Download data by using selenium
    res_df = download_data(res_df)

    # Download the Pic from links
    res_df = download_pic(res_df)

    # Save DataFrame to csv
    res_df.to_csv('SVW Brand Info.csv', encoding='GBK', index=False)


if __name__ == '__main__':
    main()
