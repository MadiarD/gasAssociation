from django.shortcuts import render
from .models import Members

def members():
    members = Members.objects.all()
    return members
