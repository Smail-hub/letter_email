import os
from dotenv import load_dotenv
import smtplib


load_dotenv()

login = os.getenv("LOGIN")
token = os.getenv("TOKEN")

sender_email = "Safin508@yandex.ru"
sender_name = "Эмиль"
recipient_email = "Safin508@yandex.ru"
recipient_name = "Родион"

email_from = sender_email
email_to = recipient_email
subject = "Приглашение!"

letter = """From: {From}
To: {To}
Subject: {Subject}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(
    From=sender_email, To=recipient_email, Subject="Приглашение!"
)

letter = letter.replace(
    "%website%", "https://dvmn.org/profession-ref-program/safin508/4CGyl/"
)
letter = letter.replace("%friend_name%", recipient_name)
letter = letter.replace("%my_name%", sender_name)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login(login, token)
server.sendmail(email_from, email_to, letter)
server.quit()
