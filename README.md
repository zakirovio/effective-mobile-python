# effective-mobile-python
Effective Mobile | QA Automation Engineer position test task

* Два задания разбил на отдельные приложения в одном проекте
* github можно собрать через Docker или как обычно в системе машины

## Сборка проекта без Docker
* ```git clone git@github.com:zakirovio/effective-mobile-python.git```
* ```cd effective-mobile-python```
* ```python -m venv .venv``` или ```python3 -m venv .venv```
* ```source ./.venv/bin/activate``` или ```.venv\Scripts\activate```
* ```pip install -r requirements.txt```
* ```далее нужно создать .env файл, скопировав переменные окружения из .env.template```
* ```! нужно задать свои github credentials в .env файле !```

## Дополнительная информация
* ```настройки всего проекта хранятся config/settings.py```
* ```run.py утилита для запуска одного из приложений```
* ```сами приложения расположены в директории apps``` 

## Запуск github
* ```удостовертесь, что находитесь в папке src и активен .venv```
* ```выполните в терминале:```  
    * ```на Windows: python run.py github```
    * ```на Unix: python3 run.py github```
* ```за ходом работы можно следить по логам в консоли```

* ```Docker```
    * ```дополнительно собрал образ в Docker для этого теста Github```
        * ```docker-compose up``` 

## Запуск e2eui
* ```удостовертесь, что находитесь в папке src и активен .venv```
* * ```выполните в терминале:```  
    * ```на Windows: python run.py e2eui```
    * ```на Unix: python3 run.py e2eui```
* ```за ходом работы можно следить по логам в консоли и в окне браузера```
