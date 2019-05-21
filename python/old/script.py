#-*- coding: utf-8 -*-
from Wpdb import Wpdb
o = Wpdb('protivkorupcii.ru')
o.install_wp("http://protivkorupcii.ru",'Protivkorupcii.ru','Сайт против корупции в России','o.v.sergeyev@gmail.com','o.v.sergeyev','phen0men')
#o.create_post('11Эт есть новая статья', 'Теперь время такое что статьи создаются очень быстро')
#o.delete_post()
#print o.check_post_name('nw_hello-world')
#o.set_blogname("Зато Космос")
#o.set_description("Новый поход в освоении космоса")
#o.create_category("Прошу вас быть реще")
