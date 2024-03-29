# -*- coding: utf-8 -*-
from django import forms
from .models import Post, Comment

__author__ = "suvorovao"


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
