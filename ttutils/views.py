from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')

def modify(request):
    giventext = request.POST.get('text','default')
    upper = request.POST.get('upper','off')
    lower = request.POST.get('lower','off')
    removepunc = request.POST.get('removepunc','off')
    removespace = request.POST.get('removespace','off')
    removenew = request.POST.get('removenew','off')
    
    
    print(giventext)
    if(giventext==""): 
        return HttpResponse("<h1>Please Write something in the box!!!<h1>")

    if(removepunc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        newtext=""
        for char in giventext:
            if char not in punctuations:
                newtext += char
        context = {'changes':'Removed Punctuation','newtext':newtext}
        giventext = newtext
    
    if(lower=="on"):
        newtext=""
        for char in giventext:
            newtext += char.lower()
        context = {'changes':'LowerCase','newtext':newtext}
        giventext = newtext
    
    if(upper=="on"):
        newtext=""
        for char in giventext:
            newtext += char.upper()
        context = {'changes':'UpperCase','newtext':newtext}
        giventext = newtext
    
    if(removespace=="on"):
        newtext = ""
        for index, char in enumerate(giventext):
            if char == giventext[-1]:
                    if not(giventext[index] == " "):
                        newtext += char

            elif not(giventext[index] == " " and giventext[index+1]==" "):                        
                newtext += char

        context = {'changes':'Removed spaces','newtext':newtext}
        giventext = newtext
    
    if(removenew=="on"):
        newtext=""
        for char in giventext:
            if char != "\n" and char!="\r":
                newtext += char
            else:
                newtext += ' '
        context = {'changes':'Removed New Lines','newtext':newtext}
        giventext = newtext


    if(removepunc != "on" and lower!="on" and upper!="on" and removespace!="on" and removenew!="on"):
        return HttpResponse("<h1>please select any operation and try again</h1>")
   
    return render(request,'modify.html',context)