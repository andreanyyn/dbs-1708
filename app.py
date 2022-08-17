#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request, render_template


# In[2]:


import joblib


# In[3]:


app = Flask(__name__) #__name__ is a reserve word used by python to tell cloud this is my program? created from scratch


# In[4]:


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method=="POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2= joblib.load("tree")
        r2 = model2.predict([[rates]])
        print(rates)
        return(render_template("index.html", result1= r1, result2=r2))
    else:
        return(render_template("index.html", result1="waiting", result2="waiting"))

    


# In[ ]:


if __name__ == "__main__":
    app.run()

