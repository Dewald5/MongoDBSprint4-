# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymongo

q = -1
myclient = pymongo.MongoClient("mongodb://localhost:27017/")   
mydb = myclient["DataTracker"]                       

mychips = mydb["Chips"]
mycooldrinks = mydb["Cooldrinks"]
mypies = mydb["Pies"]
myfruits = mydb["Fruits"]
mycupcakes = mydb["Cupcakes"]
myveggies = mydb["Veggies"]
mytop3 = mydb["Top3"]
def chipsdb():
    mylist = [
        { "Item": "Lays", "Price": "15", "Stocklvl": "31"},             
        { "Item": "Doritos", "Price": "15", "Stocklvl": "21"},
        { "Item": "Pringles", "Price": "20", "Stocklvl": "11"},
        { "Item": "Cheesesnaks", "Price": "14", "Stocklvl": "15"}
        ]  
    a = mychips.insert_many(mylist)

def cooldrinksdb():
    mylist2 = [
        { "Item": "Coke", "Price": "12", "Stocklvl": "26"},             
        { "Item": "Fanta", "Price": "12", "Stocklvl": "14"},
        { "Item": "Sprite", "Price": "12", "Stocklvl": "20"}
        ]  
    b = mycooldrinks.insert_many(mylist2)
    
def piesdb():
    mylist3 = [
        { "Item": "Chicken", "Price": "17", "Stocklvl": "30"},             
        { "Item": "Beef", "Price": "16", "Stocklvl": "19"},
        { "Item": "Steaknkidney", "Price": "20", "Stocklvl": "32"}
        ]  
    c = mypies.insert_many(mylist3)

def fruitsdb():
    mylist4 = [
        { "Item": "Orange", "Price": "6", "Stocklvl": "13"},             
        { "Item": "Banna", "Price": "5", "Stocklvl": "15"},
        { "Item": "Pear", "Price": "5", "Stocklvl": "17"}
        ]  
    d = myfruits.insert_many(mylist4)

def cupcakesdb():
    mylist5 = [
        { "Item": "Chocolate", "Price": "10", "Stocklvl": "14"},             
        { "Item": "Cappacino", "Price": "13", "Stocklvl": "30"},
        { "Item": "Vanilla", "Price": "11", "Stocklvl": "23"}
        ]  
    e = mycupcakes.insert_many(mylist5)    

def veggiesdb():
    mylist6 = [
        { "Item": "Carrots", "Price": "5", "Stocklvl": "22"},             
        { "Item": "Cabbage", "Price": "9", "Stocklvl": "27"},
        { "Item": "Potato", "Price": "4", "Stocklvl": "34"}
        ]  
    f = myveggies.insert_many(mylist6)
def top3():
    mylist7 = [
        { "_id": 3,"Item": "Lays", "Price": "15", "Stocklvl": "31"},             
        { "_id": 2,"Item": "Steaknkidney", "Price": "20", "Stocklvl": "32"},
        { "_id": 1,"Item": "Potato", "Price": "4", "Stocklvl": "34"}
        ]  
    g = myveggies.insert_many(mylist7)
    
def update():
    myquery = {"Item":"Carrots","Price":"5","Stocklvl":"22"}
    newval = { "$set": { "Item": "OrangeCarrots","Price":"12","Stocklvl":"22" } }
    myveggies.update_one(myquery, newval)


def delall():
     mychips.delete_many({})
     mycooldrinks.delete_many({})
     mypies.delete_many({})
     myfruits.delete_many({})
     mycupcakes.delete_many({})
     myveggies.delete_many({})
     mytop3.delete_many({})
def delete():
    myquery = {"Item":"Chicken"}
    mypies.delete_one(myquery)
    myquery2 = {"Item":"Beef"}
    mypies.delete_one(myquery2)

Deleteall = input("Do you want to delete the Database(Y/N)\n")
Createcol = input("Do you want to create the Database(Y/N)\n")
ascdsc = input("Do you want the Collections in Ascending or Descending order(ASC/DSC)\n")
Updater = input("Do you want to update Carrots to OrangeCarrots(Y/N)\n")
Delete2Q = input("Do you want to delete the 2nd and 3rd products(Y/N)\n")
Printout = input("Do you want a printout of all the collections(Y/N)\n")
  
if Createcol.lower() == "y":
    chipsdb()
    cooldrinksdb()
    piesdb()
    fruitsdb()
    cupcakesdb()
    veggiesdb()
    top3()
if Updater.lower() == "y":
    update()
    
if Deleteall.lower() == "y":
    delall()
    
if Delete2Q.lower() == "y":
    delete()
if ascdsc.lower() == "asc":
    q = 1
elif ascdsc.lower() == "dsc":
     q = -1    
if Printout.lower() == "y":
 
 mydoc = mychips.find().sort("Stocklvl", q)
 mydoc2 = mycooldrinks.find().sort("Stocklvl", q) 
 mydoc3 = mypies.find().sort("Stocklvl", q)
 mydoc4 = myfruits.find().sort("Stocklvl", q)
 mydoc5 = mycupcakes.find().sort("Stocklvl", q)
 mydoc6 = myveggies.find().sort("Stocklvl", q)
 mydoc7 = mytop3.find().sort("Stocklvl", q)
 
 for a in mydoc:
    print(a)
 for b in mydoc2:
    print(b) 
 for c in mydoc3:
    print(c)
 for d in mydoc4:
    print(d)    
 for e in mydoc5:
    print(e)
 for f in mydoc6:
    print(f)
 for g in mydoc7:
    print(g)   
 print("\nThanks for using MongoDB")