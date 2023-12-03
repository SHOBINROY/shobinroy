from typing import List

from django.db import models
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = ['name','desc','year','img']
