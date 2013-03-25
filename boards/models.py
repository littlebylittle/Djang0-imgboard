# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.


class BoardCategories(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __unicode__(self):
        return self.name


class ImageBoard(models.Model):
    slug_name = models.CharField(max_length=20, unique=True)
    caption = models.CharField(max_length=80)
    max_threads_on_board = models.IntegerField(default=10, help_text='max. number of threads on board')
    max_post_in_thread = models.IntegerField(default=10)
    category = models.ForeignKey(BoardCategories)
    flash_on_flag = models.BooleanField(default=True, help_text='Requires `content_on_flag` ON')
    picture_on_flag = models.BooleanField(default=True, help_text='Requires `content_on_flag` ON')
    content_on_flag = models.BooleanField(default=True)
    default_username_on_board = models.CharField(max_length=80, default='Anonymous')
    board_enable_flag = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modification_date = models.DateTimeField(auto_now_add=True, auto_now=True, editable=False)
    number_of_messages = models.IntegerField(default=0, editable=False, help_text='Число всех сообщений в разделе')
    threads_on_page = models.IntegerField(default=10, editable=True, help_text='Количество постов на странице')

    class Meta:
        ordering = ('category',)

    def __unicode__(self):
        #return 'Раздел: %s' % (self.name,)
        return "Board: /%s/, max threads: [%3s]" % (self.slug_name, self.max_threads_on_board,)


class PublishedMessage(models.Model):
    board_owner = models.ForeignKey(ImageBoard,)
    message_number = models.IntegerField(editable=False, default=0)
    message_data = models.TextField(max_length=600,)
    author_name = models.CharField(max_length=20, default='Anonymous', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    captcha_data = models.CharField(max_length=20, default='captcha')
    user_agent = models.CharField(max_length=30, default='Chromium Browser (etc)', editable=False, blank=True)
    #TODO:add file-fields
    media_link = models.URLField(blank=True)
    password = models.CharField(max_length=64, default='password', blank=True)
    is_hide = models.BooleanField(default=False)
    ip_creator = models.IPAddressField(default='127.0.0.1', editable=False)

    class Meta:
        unique_together = (('message_number', 'board_owner'),)

    def __unicode__(self):
        return self.message_data[:30]

    def clean(self):
        self.board_owner.number_of_messages += 1
        self.board_owner.save()
        self.message_number = self.board_owner.number_of_messages


class Thread(PublishedMessage):
    caption = models.CharField(max_length=40, blank=True, default='New thread')
    is_attached = models.BooleanField(default=False)


class PostInThread(PublishedMessage):
    thread_owner = models.ForeignKey('Thread')

    def clean(self):
        self.board_owner = self.thread_owner.board_owner
        self.board_owner.number_of_messages += 1
        self.board_owner.save()
        self.message_number = self.board_owner.number_of_messages