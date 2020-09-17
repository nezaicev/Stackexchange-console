## Stackexchange-console
Скрипт обращаеться к API сервиса [[stackexchange.com]](https://stackexchange.com), позволяет искать ответы по определенному запросу.
Для запросов используется библиотека requests.

##  Как  запустить
В системе должен быть установлен Python3

```bash
pip install -r requirements.txt
``` 
#### Запуск
Получить ответы где встречается 'python'
``` bash
$ python main.py python
```
#### Вы получите список ответов
``` bash
loading...
+-------------------------------------------------------------------+--------------------+-------------------+------------------------------------------------------------+
| Title                                                             | Author             | Answered          | Link                                                       |
+-------------------------------------------------------------------+--------------------+-------------------+------------------------------------------------------------+
| How to make A - 1 = Z in Python?                                  | qwert zuiop        | azro              | https://stackoverflow.com/users/7212686/azro               |
| How do you select random rows from a pandas DataFrame with        | Jamiephilpott88    | bart cubrich      | https://stackoverflow.com/users/10443508/bart-cubrich      |
| constraints in Python                                             |                    |                   |                                                            |
| &#39;py&#39; works but not &#39;python&#39; in command prompt for | SuperAadi          | ShadowRanger      | https://stackoverflow.com/users/364696/shadowranger        |
| windows 10                                                        |                    |                   |                                                            |
| &#39;py&#39; works but not &#39;python&#39; in command prompt for | SuperAadi          | Dwarkesh Kaswala  | https://stackoverflow.com/users/11747818/dwarkesh-kaswala  |
| windows 10                                                        |                    |                   |                                                            |
| &#39;py&#39; works but not &#39;python&#39; in command prompt for | SuperAadi          | Alexandra Dudkina | https://stackoverflow.com/users/14168623/alexandra-dudkina |
| windows 10                                                        |                    |                   |                                                            |
| Command errored out with exit status 1: python setup.py egg_info  | Prem Patel         | phd               | https://stackoverflow.com/users/7976758/phd                |
| Check the logs for full command output - while installing pycopy- |                    |                   |                                                            |
| fcntl through pip                                                 |                    |                   |                                                            |
| I keep on receiving different error messages while scraping with  | Chase Gormley      | MendelG           | https://stackoverflow.com/users/12349734/mendelg           |
| python-bs4 with requests                                          |                    |                   |                                                            |
| How can I split strings while ignoring the portion in a           | kounteyo           | tzaman            | https://stackoverflow.com/users/257465/tzaman              |
| parentheses in python                                             |                    |                   |                                                            |
| How can I split strings while ignoring the portion in a           | kounteyo           | Grayrigel         | https://stackoverflow.com/users/5604562/grayrigel          |
| parentheses in python                                             |                    |                   |                                                            |
| How do order of operations go on Python?                          | Ashton             | Gabriel Staples   | https://stackoverflow.com/users/4561887/gabriel-staples    |
| How do order of operations go on Python?                          | Ashton             | Dillon            | https://stackoverflow.com/users/13672956/dillon            |
| How do order of operations go on Python?                          | Ashton             | Martijn Pieters   | https://stackoverflow.com/users/100297/martijn-pieters     |
| How do order of operations go on Python?                          | Ashton             | Rory Daulton      | https://stackoverflow.com/users/6246044/rory-daulton       |
| How do order of operations go on Python?                          | Ashton             | Johannes Overmann | https://stackoverflow.com/users/2205033/johannes-overmann  |
| ModuleNotFoundError - Python VSCode I can&#180;t import modules:  | Andree Alvarado    | Peter             | https://stackoverflow.com/users/7108589/peter              |
| How to parse data from gRPC response in python?                   | no746              | Joseph            | https://stackoverflow.com/users/4392376/joseph             |
| Parse a table with BeautifulSoup, Selenium in Python              | confusedcoder      | arundeep chohan   | https://stackoverflow.com/users/9901261/arundeep-chohan    |
| Save plots generated from fbprophet in Python                     | Alice_inwonderland | DrRaspberry       | https://stackoverflow.com/users/12177820/drraspberry       |
| Save plots generated from fbprophet in Python                     | Alice_inwonderland | patapon           | https://stackoverflow.com/users/2780934/patapon            |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | user3166559       | https://stackoverflow.com/users/3166559/user3166559        |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | Michael Alemu     | https://stackoverflow.com/users/11933599/michael-alemu     |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | Daniel F          | https://stackoverflow.com/users/4427777/daniel-f           |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | Make42            | https://stackoverflow.com/users/4533188/make42             |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | liwt31            | https://stackoverflow.com/users/7377553/liwt31             |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | donkopotamus      | https://stackoverflow.com/users/5249307/donkopotamus       |
| Check if a large matrix is diagonal matrix in python              | JoeJackJessieJames | ZdaR              | https://stackoverflow.com/users/3051961/zdar               |
| Python Save to file                                               | Stefan             | ALSHARGI NEWYORK  | https://stackoverflow.com/users/10664378/alshargi-newyork  |
| Python Save to file                                               | Stefan             | warvariuc         | https://stackoverflow.com/users/248296/warvariuc           |
| Python Save to file                                               | Stefan             | David Heffernan   | https://stackoverflow.com/users/505088/david-heffernan     |
| Python Save to file                                               | Stefan             | jaime             | https://stackoverflow.com/users/731624/jaime               |
| Scaling a normal distribution in Python                           | SKPS               | Quang Hoang       | https://stackoverflow.com/users/4238408/quang-hoang        |
| How to sort array in Python based on particular data set          | Ammad              | Vishesh Mangla    | https://stackoverflow.com/users/4213362/vishesh-mangla     |
| How to sort array in Python based on particular data set          | Ammad              | hgb123            | https://stackoverflow.com/users/6655160/hgb123             |
| How to sort array in Python based on particular data set          | Ammad              | Green Cloak Guy   | https://stackoverflow.com/users/2648811/green-cloak-guy    |
+-------------------------------------------------------------------+--------------------+-------------------+------------------------------------------------------------+

```

## Цель проекта 
Тестовое задание на вакансию Python-разработчик (Ижевский Радиозавод)
