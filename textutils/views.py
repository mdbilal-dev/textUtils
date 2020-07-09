# I HAVE CREATED THIDS FILE !
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
 
def analyze(request):
    djtext=request.POST.get('text')
    
    check=request.POST.get('removepunc')


    puncts='''  !@#$%^&*(){[]}.,<>?/\-~_ '''

    #REMOVING PUNCTUATIONS
    if check=='on':
        puretext=""
        for i in djtext:
            if i not in puncts:
                puretext+=i
    
        params={'purpose':'Punctuations Removed :','puretext':puretext}
        djtext=puretext


    #UPPERCASING ALL LETTERS
    if request.POST.get('uppercase')=='on':
        puretext=""
        for i in djtext:
            puretext+=i.upper()
        params={'purpose':'Uppercased :','puretext':puretext}
        djtext=puretext



    #REMOVING NEW LINES
    if request.POST.get('newlineremover')=='on':    
        puretext=""
        for i in djtext:
            if i !="\n" and i!="\r":
                puretext+=i
        params={'purpose':'NewLines Removed: ','puretext':puretext}
        djtext=puretext

    # REMOVING SPACES
    if request.POST.get('spaceremover')=='on': 
        puretext=""   
        for i in djtext:
            if i !=" ":
                puretext+=i
        params={'purpose':'Spaces Removed: ','puretext':puretext}
        djtext=puretext

    #FINDING LENGTH
    if request.POST.get('findLength')=='on': 
        puretext=""
        count=0   
        space=0
        for i in djtext:
            if i==" ":
                space+=1
            count+=1
        puretext=count-space
        params={'purpose':'Length in Words: ','puretext':str(puretext)}

    if request.POST.get('spaceremover')!='on' and request.POST.get('findLength')!='on' and request.POST.get('newlineremover')!='on' and  request.POST.get('uppercase')!='on' and request.POST.get('uppercase')!='on' and check!='on' or djtext==" " :
        return HttpResponse('<center><h1 style="color:red">PLEASE SELECT AN OPERATION OR WRITE SOMETHING !!</h1></center>')
        
    return render(request,'analyze.html',params)

#about us Page
def about(request):
    return render(request,'aboutUs.html')



    
   
    
