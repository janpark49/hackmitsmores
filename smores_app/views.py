from smores_app import app
from flask import render_template, request, redirect
import requests

global question_dict
global story_array
question_dict = [1]
story_array = [["Hi!\nIt’s so nice to meet you!\nMy name is Jen and I am here to lead you on an adventure. You lucked out, because not a lot of people really get the chance to meet Santa. But you know what? Since you seem to be so bright, I’m going to give you a special chance to meet Santa.\nNow, are you ready to travel to the North Pole?", "Count me in!"], 
["YAYYYY! HOORAYYY!\nYou’re so smart, how did you even do that?\nLet’s hop onto the train! All aboard!", "Choo choo!"],
["GOOD JOB! SO MANY PRESENTS RIGHT???!", "Yes!"],
["Oh wow!!! A smart wonder indeed!\nThis is called “addition”, where we count the total of something!\nWe use “+” between two numbers and count the total of the two numbers.\nIn the previous problem, it would be 1 + 2 is 3 total cookies, just like you did!", "Cool!"],
["WOW!!! You’re becoming a pro at this!!!\nNow that we have cookies… Do you want some of mine?", "Yes, of course!"]]
global story_num 
story_num = 0
global question_num 
question_num = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/story/<int:num>")
def story_page(num):
    global story_num
    global story_array
    global question_num
    story_num += 1
    next_question = question_num
    this_button = story_array[num][1]
    text = story_array[num][0].split('\n')
    return render_template("story.html", text = text, button = this_button, next_question = question_num)

@app.route("/end")
def end_page():
    return render_template("end.html")