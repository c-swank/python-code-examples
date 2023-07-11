from io import StringIO
from flask import Flask, jsonify, request
import pandas

# This is a simple function to convert a pandas object from csv to html
# The input csv should be a pandas dataframe
def generateHtml(csv):
    print(csv)
    y = csv.to_html()
    print(y)
    return y

"""
Example 1

Calling our generateHtml function statically. We have to run the entire
file in order to execute this code, and give it a specific file path
from our computer.

"""
x = pandas.read_csv("somefile.csv")
generateHtml(x)



# --------------------------------------------- #
"""
Example 2

Calling our generateHtml function as part of an API, or a server
"""
# This defines a server. When the application is running, that would be on
# 127.0.0.1:5000 or http://localhost:5000 (5000 is just the default "port")
server = Flask(__name__)

# This defines a route on the server, like "home" in www.website.com/home.
# Our server will provide an API like http://localhost:5000/csv_to_html
@app.route('/csv_to_html', methods=['POST'])
def csv_to_html():
    # Our API needs some data whenever we call it.
    data = request.get_data()

    # We need to convert our csv into a pandas dataframe before we
    # call our generateHtml function. First, lets create an IO stream
    # from our data string, because pandas requires a stream
    csvIo = StringIO(data)

    # Now we can create our dataframe
    df = pandas.read_csv(csvIo)

    # Initialize an empty "response" object. Our API needs to send back
    # data, so we'll fill this res with data to send back.
    res = {}

    # We call our generateHtml function, and pass in our dataframe. We save
    # the output to the res object which we will return in our API response.
    res['html'] = generateHtml(df)
    
    # We generally want to represent API responses as JSON.
    res = jsonify(res)
    return res

"""
There’s a concept called the “call stack”, which represents the depth of code execution. If you think of a script that doesn’t call any functions, like the following

x = 1 + 2
s = f"some text with the variable x set to a value of {x}"
print(s)

It has a stack depth of 0. You can just read the code top to bottom and debug it that way.
"""