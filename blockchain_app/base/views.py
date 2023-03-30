from django.shortcuts import render
from .models import Member
import json

all_members = Member.objects.all().values()
account_list = []
for x in all_members:
    #x.pop('id')
    account_list.append(x)

account_list_json = json.dumps(account_list)
print("json",account_list)


#account_data = {  'name':'Paramvir', 'accountNo' :"0xec95cad38df7b49b3432d83f0b80997e82a47a68"  }
def mainPage(request):
    return render(request, 'base/pages/mainPage.html',{'account_list_json': account_list_json})

def signup(request):
    return render(request, 'base/pages/signup.html')

def home(request):
    return render(request, 'base/pages/home.html',{'account_list_json': account_list_json})
