#학생1
import time
import selenium
from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Malgun Gothic')
a=int(input('시즌  1819 ,1920 ,2021 중 하나:'))
print('==========================')

URL = 'https://sports.news.naver.com/basketball/record/index.nhn?category=kbl'

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

if a==2021:

    basket = driver.find_elements_by_tag_name('tr')
    rerecord = []
    print('---------------------------------20-21팀순위---')
    for i in range(11):
        rerecord1 = []
        basket_team = basket[i].find_elements_by_tag_name('span')
        basket_team = basket_team[0].text
        print(basket_team)
        record = basket[i].find_elements_by_tag_name('td')
        for re in record:
            rerecord1.append(re.text)
        rerecord.append(rerecord1)
    del rerecord[0]

    print('-------------------------------20-21기록------')

    # 기록
    win = []
    lose = []
    score = []
    assist = []
    team = []

    print('기록: 팀   경기수   승률   승   패   승차   득점   AS   리바운드   스틸   블록   3점슛   자유투   자유투성공')

    for info in rerecord:
        print(info)
        win.append(info[3])
        lose.append(info[4])
        score.append(info[6])
        assist.append(info[7])
        team.append(info[0])

    print('\n', '승:', win, '\n', '패:', lose, '\n', '득점:', score, '\n', '도움:', assist, '\n')
    time.sleep(3)
    driver.close()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.yticks(x, team)
    plt.barh(x, assist, label='도움', color='y')
    plt.legend()
    plt.show()

#힉생2
if a==1920:
    driver.find_element_by_class_name('btn_move_date.prev').click()

    basket = driver.find_elements_by_tag_name('tr')
    rerecord = []
    print('----------------------------------19-20팀순위---')
    for i in range(11):
        rerecord1 = []
        basket_team = basket[i].find_elements_by_tag_name('span')
        basket_team = basket_team[0].text
        print(basket_team)
        record = basket[i].find_elements_by_tag_name('td')
        for re in record:
            rerecord1.append(re.text)
        rerecord.append(rerecord1)
    del rerecord[0]

    print('---------------------------19-20기록------')

    # 기록
    win = []
    lose = []
    score = []
    assist = []
    team = []

    print('기록: 팀   경기수   승률   승   패   승차   득점   AS   리바운드   스틸   블록   3점슛   자유투   자유투성공')

    for info in rerecord:
        print(info)
        win.append(float(info[3]))
        lose.append(float(info[4]))
        score.append(float(info[6]))
        assist.append(float(info[7]))
        team.append(info[0])

    print('\n','팀:',team,'\n', '승:', win, '\n', '패:', lose, '\n', '득점:', score, '\n', '도움:', assist, '\n')
    time.sleep(3)
    driver.close()

    #학생2 그래프
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.title('1920년 팀별 승')
    plt.yticks(x, team)
    plt.barh(x, win, color='r')
    plt.xlabel('승', fontsize=15)
    plt.show()

#학생3
if a==1819:
    for i in range(2):
        driver.find_element_by_class_name('btn_move_date.prev').click()

    basket = driver.find_elements_by_tag_name('tr')
    rerecord = []
    print('-------------------------------------18-19팀순위---')
    for i in range(11):
        rerecord1 = []
        basket_team = basket[i].find_elements_by_tag_name('span')
        basket_team = basket_team[0].text
        print(basket_team)
        record = basket[i].find_elements_by_tag_name('td')
        for re in record:
            rerecord1.append(re.text)
        rerecord.append(rerecord1)
    del rerecord[0]

    print('--------------------------18-19기록------')

    # 기록
    win = []
    lose = []
    score = []
    assist = []
    team = []

    print('기록: 팀   경기수   승률   승   패   승차   득점   AS   리바운드   스틸   블록   3점슛   자유투   자유투성공')

    for info in rerecord:
        print(info)
        win.append(float(info[3]))
        lose.append(float(info[4]))
        score.append(float(info[6]))
        assist.append(float(info[7]))
        team.append(info[0])

    print('\n','팀:',team,'\n', '승:', win, '\n', '패:', lose, '\n', '득점:', score, '\n', '도움:', assist, '\n')
    time.sleep(3)
    driver.close()

    #학생3 그래프
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.title('1819년 팀별 득점')
    plt.yticks(x, team)
    plt.barh(x, score, color='b')
    plt.xlabel('득점', fontsize=15)
    plt.show()