#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="sereg_posmotri_komp", password="zxckondratzxc123!?",
               like_per_day=1500,  # Лайков каждый день
               comments_per_day=90,   # Коментов каждый лень
               tag_list=['awesome', 'amazing','бомба','boombs', 'Закат','супер'], # По тегам
               max_like_for_one_tag=250, # Лайков на один тег
               follow_per_day=0, # Подписок каждый лень
               follow_time=5*60*60, # Сколько времени между фоллов-анфолло (сек)
               unfollow_per_day=150, #  Отписка в день
               unfollow_break_min=15, # пЕРЕРЫВЫ
               unfollow_break_max=30, # пРЕЕРЫВЫ
               log_mod=0) #Писание лога.  (С)smweb

bot.new_auto_mod()
