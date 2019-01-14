from django import forms
from .models import Article
from django.shortcuts import render,HttpResponse,redirect

class ArticleForm(forms.ModelForm):
    class Meta:
     model = Article
     fields = ["author","title","content","article_image"]
   
     
     



     
       
