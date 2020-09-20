from smores_app import app
from flask import render_template, request, redirect
import requests

global q_dat =["Okay cool! Buckle up! North Pole here we come!\n \nWelcome to the North Pole! Before we go and \nmeet Santa, we first need to ride the train to\n Santa’s house from here! Over there is the train!\n \nHow many people are in the train waiting for me?"]
q_dat.append("Here, now we arrived in front of Santa’s house but\n oh no! What is that? \n \nCount how many presents I have for you all to \nenter my house!")
q_dat.append("Santa: “Before I send out the presents, I just have \nto do one more thing… I have this question that \nI haven’t been able to solve for so long… \nWill you help me solve this question?” \nI have 1 cookie, and you have 2 cookies! \nHow many cookies do we have total? ")
q_dat.append("Now I’m curious… Can you do this as well?\n What is 3 + 4? If you’re stuck, think about it with cookies! \nHow many total cookies do you have if I have 3 \ncookies and you have 4 cookies?")
q_dat.append("I have 7 cookies, and I give you 2 of \nthem! How many cookies do I have left? ")
global a_dat=[["3","4","5","6"],["10","12","16","17"],["1 cookie","2 cookies","3 cookies", "4 cookies"],["3","4","6","7"],["5 cookies","4 cookies","3 cookies","6 cookies"]]
global r_dat=[2,1,3,4,1]
global img_dat=["/static/s0.png","/static/s1.png","/static/s2.png","/static/s3.png","/static/s1.png","/static/q0.png","/static/q1.png","/static/q2.png","/static/q3.png","/static/q4.png"]
global story_array = [["Hi!\nIt’s so nice to meet you!\nMy name is Jen and I am here to lead you on an adventure. You lucked out, because not a lot of people really get the chance to meet Santa. But you know what? Since you seem to be so bright, I’m going to give you a special chance to meet Santa.\nNow, are you ready to travel to the North Pole?", "Count me in!"], 
["YAYYYY! HOORAYYY!\nYou’re so smart, how did you even do that?\nLet’s hop onto the train! All aboard!", "Choo choo!"],
["GOOD JOB! SO MANY PRESENTS RIGHT???!", "Yes!"],
["Oh wow!!! A smart wonder indeed!\nThis is called “addition”, where we count the total of something!\nWe use “+” between two numbers and count the total of the two numbers.\nIn the previous problem, it would be 1 + 2 is 3 total cookies, just like you did!", "Cool!"],
["WOW!!! You’re becoming a pro at this!!!\nNow that we have cookies… Do you want some of mine?", "Yes, of course!"]]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/qpage/<int:sum>")
def qpage(sum):
    next1=["/story/1","/story/2", "/story/3", "/story/4", "/end"]
    data=question_dict[sum]
    return render_template("qpage.html", ams = r_dat[sum], next=next1[sum], imglnk=img_dat[sum+5], quest=q_dat[sum].split('\n'), ams1=a_dat[num][0],ams2=a_dat[num][1],ams3=a_dat[num][2],ams4=a_dat[num][3])

@app.route("/story/<int:num>")
def story_page(num):
    this_button = story_array[num][1]
    text = story_array[num][0].split('\n')
    return render_template("story.html", text = text, imglnk = img_dat[num], button = this_button, next_question = num)

@app.route("/end")
def end_page():
    return render_template("end.html")
