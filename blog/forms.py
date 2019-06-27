# -*- coding: utf-8 -*-
from django import forms
from .models import Post

__author__ = "suvorovao"


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
