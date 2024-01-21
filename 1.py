# Импорт библиотеки вебдрайвера
from selenium import webdriver
#импорт библиотеки времени, для ожидания прогрузки страницы
import time
#Импорт библиотеки By
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
# Обратимся к документации: https://selenium-python.readthedocs.io/
from selenium.webdriver.support.wait import WebDriverWait
# Исключительное ожидание
from selenium.webdriver.support import expected_conditions as EC

#-----------------инициализация библиотеки для firefox-------------
from selenium.webdriver.firefox.options import Options
#-----------------инициализация библиотеки для firefox-------------
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------

link = "https://webtucre.ru/testovaya-stranicza-6/"
# browser = webdriver.Firefox() #----отключили для запуска теста для jenkins вне графического интерфейса-----
#Добавим команду которая называется browser максимизировать окно браузера
browser.maximize_window()
browser.get(link)
# Строка поиска=serch_string
search_string = browser.find_element(By.CSS_SELECTOR, "input[class*=elementor-search-form__input]")
#Ввод поискового запроса в строку поиска
search_string.send_keys("QA228")
#Кнопка поиска
knopka = browser.find_element(By.CSS_SELECTOR, "button[class*=elementor-search-form__submit]")
#Клик по кнопке поиска
knopka.click()
#данную команду лучше не использовать так как она удленяет работу теста, поэтому
# мы будем использовать библиотеку и команду
#time.sleep(2)


#Проверка того что мы действительно нашли то что искали
proverka = WebDriverWait(browser, 5).until(
EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[class*=entry-title]"))).text
#Вывод сообщения о найденом элементе
print(proverka)
# Проверяем раздел на существующее название (Мы взяли переменную=proverka1 со словом "тестирование"
# и взяли обычную переменную=proverka, которая ищет наш запрос и берет оттуда просто текст=.text
# и мы говорим, давайте сравним в цикле if и else и выведем на экран соответствующие надписи)
proverka1 = "QA228"
# Удалим сравнение и добавим проверку
assert proverka == proverka1, f"Тест не пройден, вот что удалось найти вместо QA228 - {proverka}"
#Закрываем открытые окна браузера после теста
browser.quit()
