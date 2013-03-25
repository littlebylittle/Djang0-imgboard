#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#  * Date: 3/23/13
#  * Time: 10:21 PM
#  =============================
from __future__ import print_function

if __name__ == '__main__':
    pass

from django.conf.urls import url, patterns

urlpatterns = patterns('boards.views',
                       url(r'^$', 'show_index'),
                       url(r'^frame/$', 'show_frame'),
                       url(r'^news/$', 'show_news'),
                       url(r'^([-\d\w_]+)/res/(\d+)', 'show_thread'),
                       url(r'^([-\d\w_]+)/(\d+)', 'show_board_index'),
                       url(r'^(?P<board_name>[-\d\w_]+)/(index)?$', 'show_board_index',
                           {'page_number': '0'}),

                       )
