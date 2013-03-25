#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#  * Date: 3/23/13
#  * Time: 2:14 PM
#  =============================
from __future__ import print_function

if __name__ == '__main__':
    pass

from django.contrib import admin
from boards.models import BoardCategories
from boards.models import ImageBoard
from boards.models import PostInThread
from boards.models import Thread


class ImageBoardAdmin(admin.ModelAdmin):
    list_display = ['slug_name', 'caption', 'category',
                    'modification_date', 'board_enable_flag', 'number_of_messages']
    actions_on_bottom = True
    date_hierarchy = 'modification_date'
    readonly_fields = ('creation_date', 'modification_date', 'number_of_messages')
    save_as = True
    search_fields = ('caption', 'slug_name')


class BoardCategoriesAdmin(admin.ModelAdmin):
    #date_hierarchy = 'name'
    pass


class ThreadAdmin(admin.ModelAdmin):
    readonly_fields = ('message_number', 'creation_date', 'ip_creator')
    list_display = ('caption', 'message_number', 'board_owner')
    pass


class PostInThreadAdmin(admin.ModelAdmin):
    list_display = ('message_data', 'thread_owner')
    exclude = ('board_owner',)
    readonly_fields = ('message_number',)
    pass


admin.site.register(BoardCategories, BoardCategoriesAdmin)
admin.site.register(ImageBoard, ImageBoardAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(PostInThread, PostInThreadAdmin)
