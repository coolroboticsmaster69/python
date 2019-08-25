import urllib.request

def read_text():

    quotes=open("/Users/vidit/Desktop/code/python/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
def check_profanity(text_to_check):
    conection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=conection.read()
    #print(output)
    conection.close()
    if "true" in output:
        print("profanity alert!!!!!!!!")
    elif "false" in output:
        print("no curse words")
    else:
        print("could not load properly")



read_text()
