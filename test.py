import datetime, os, netschoolapi, asyncio, time, requests, urllib, time
from netschoolapi.netschoolapi import NetSchoolAPI
# first_time = time.time()
#
#
import traceback
import loguru, sys
#loguru.logger.add('file_1.log', format="{time} {level} {message}", filter="my_module", level="ERROR", enqueue=True)
# loguru.logger.add("out.log")
# async def main():
#     # ns = NetSchoolAPI('https://giseo.rkomi.ru/')
#     # await ns.login("Скуб",
#     #             '342534',
#     #            'МОУ "СОШ №10"')
#     # report = await ns.diary()
#     # await ns.logout()
#     # print(time.time() - first_time)
#     a = int('asd')
#     print(a)
#
# if __name__ == '__main__':
#     asyncio.run(main())
#     first_time = time.time()

import math


# for x in range(-31, 31):
#     for y in range(-31, 30):
#         if x * y == 650:
#             print(f'x: {x}, y: {y}')
print(os.sep)
# try:
#     a = int('asd')
# except Exception as e:
#     a = traceback.format_exc()
#     with open('pipiska.txt', 'a') as file:
#         file.write(f"Date: {datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')}\n{a} \n\n")
#     with open('pipiska.txt', 'r') as file:
#         print(file.readlines())
# else:
#     print('True')

#
#
#
#
#
#
#
#
#
import datetime
import time
from datetime import timedelta

# import numpy as np
# import cv2
#
# days = {}
# first_pos = (260, 55)
# data_days = {}
#
#
# def updating_image(h_w, pos, im):
#     draw_text = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", 13)
#     if len(h_w) > 57:
#         num = h_w[:57].rfind(' ')
#         old_mess = h_w[:num]
#         new_mes = h_w[num + 1:]
#         new_pos = (pos[0], pos[1] + 16)
#         draw_text.text(pos, old_mess, fill=('#1c0606'), font=font)
#         updating_image(new_mes, new_pos, im)
#     else:
#         draw_text.text(pos, h_w, fill=('#1c0606'), font=font)
#
#
# def edit_msg(subject, h_w, mark, pos, im):
#     draw_text = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", 13)
#
#     # homework writing
#     if len(h_w) > 57:
#         num = h_w[:57].rfind(' ')
#         old_mess = h_w[:num]
#         new_mes = h_w[num + 1:]
#         new_pos = (pos[0], pos[1] + 16)
#         draw_text.text(pos, old_mess, fill=('#1c0606'), font=font)
#         updating_image(new_mes, new_pos, im)
#     else:
#         draw_text.text(pos, h_w, fill=('#1c0606'), font=font)
#
#     # subject writing
#     sub_pos = (pos[0] - 214, pos[1] + 2)
#     font = ImageFont.truetype("arialbd.ttf", 17)
#     draw_text.text(sub_pos, subject, fill=('#008ac9'), font=font)
#
#     # mark writing
#     sub_pos = (pos[0] + 462, pos[1] - 2)
#
#     color = '#0058c1'
#     print(mark)
#     if mark != '':
#         if int(mark) == 2:
#             color = '#ff0000'
#
#     font = ImageFont.truetype("BotData\\Tons\\ton.ttf", 40)
#     draw_text.text(sub_pos, mark, fill=color, font=font)
# def create_img(lessons, id):
#     first_pos = (260, 60)
#
#     im = Image.open('BotData\Pics\days.jpg')
#     date = lessons[0]
#     print(date.strip())
#     for lesson in lessons[1:]:
#         lesson = lesson.strip()
#         subject = lesson[:lesson.find(':')]
#         if len(subject) > 17:
#             subject = subject[:18] + '...'
#         if lesson[-8:] != 'Оценка: ':
#             print(lesson)
#             mark = lesson[lesson.rfind(':') + 1:]
#             print(mark)
#         else:
#             mark = ''
#         homework = lesson[lesson.find(':') + 2:lesson.find(' Оценка: ')]
#         edit_msg(subject, homework.replace('Оценка', '').replace('Не задано', ''), mark.strip(" "), first_pos, im)
#         first_pos = (first_pos[0], first_pos[1] + 57)
#
#     im.save(str(id) + '.jpg')
#     path = os.getcwd() + '\\' + str(id) + '.jpg'
#     return path

# for i in range(2, 6):
#     print(i)
#url = 'asdas/sdqwreq/asfa/qwqe'
# print(url.rstrip('/'))
# monday = datetime.date.today() - timedelta(days=datetime.date.today().weekday() + 14)
# for i in range(5):
#     print(monday + timedelta(days=7 * i))
# lessons_ken = 0
# asd = {'asd': '131231', 'dgfd': 'asd'}
# for i in asd.keys():
#     lessons_ken += len(asd[i])
#
# print(lessons_ken)

# now = datetime.datetime.today()
# new_year = datetime.datetime.strptime('01.01.2023', '%d.%m.%Y')
# print(f'До нового года:\n'
#       f'* {(new_year - now).days} дней\n'
#       f'* {(new_year - now).total_seconds() / 60.0} минут\n'
#       f'* {(new_year - now).total_seconds()} секунд')

# lis = ['asd', 'dsadqwe', 'asd(1)']
# print(len(lis) - 1 - lis[::-1].index('asd'))
# line = 'abc cba "alol sadqw asdqwe "'
# print(len('Эл.курс"Создание..редакторах"'))
# d = {'a': 1, 'b': 2, 'c': 4}
# print(list(d.keys()))
