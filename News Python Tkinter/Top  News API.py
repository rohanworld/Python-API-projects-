print("News App using API")
import requests
import tkinter as tk

def getNews():
    api = "f036c6bed24e482ab045a476154910d1"
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api
    news = requests.get(url).json()
    articles = news["articles"]
    myArticles=[]
    myNews=""

    for i in articles:
        myArticles.append(i["source"]["name"]+": \t"+i["title"])
    for j in range(10):
        myNews = myNews+str(j+1)+". "+myArticles[j]+"\n \n"

    # print(myNews)
    label.config(text=myNews)

root=tk.Tk()
root.geometry("1320x600")
root.title("News App by Python using API")

button = tk.Button(root,font=24, text="Top News of the Day", command = getNews)
button.pack(pady=20)

label = tk.Label(root,font=18, justify="left")
label.pack(pady=20)

getNews()

root.mainloop()