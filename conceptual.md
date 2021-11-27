### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
> Answer:
> 
> 1. JavaScript uses curl braces to denote code blocks and can indent just to beautify the code.  Python on the other hand uses indentation to denote it's code block along with allowing it to be easier to read.
> 
> 2. Python is strongly typed where JavaScript is weakly typed.
> 
> 3. JavaScript has a global variable and it's variables must be declared with a keyword.  Python does not have a global variable and variables are not declared with a keyword

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
> Answer:
> 
>	1.   use get().  get(key, def_val), if the key is present, then the value associated with the key is returned else the def_value aregument that was passed in is returned.
>
>	2. use setdefault().  setdefault(key, def_val) is similar to the get() method except if the key is not present, then the key is created and the def_value is associated with the newly created key.

- What is a unit test?
> Answer:
> 
>  Unit tests are automated tests to see if individual units of code operate as expected.

- What is an integration test?
> Answer:
> 
> Integration tests are automated tests that check if multiple modules of code are interacting together as expected.

- What is the role of web application framework, like Flask?
> Answer:
> 
> A web application framework is a set of libraries and tools to provide a standard way to build and deploy a web application.  They may provide database access, templating, session management, and often promote code reuse. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
> Answer:
> 
> Typically you would use a URL parameter when the information you want to pass in is similar to the subject of the page and you would use a query parameter when the information is more like additional info.

- How do you collect data from a URL placeholder parameter using Flask?
> Answer:
> 
> In the decorator route you pass it in between angled brackets and in the following view function you would pass it in as a parameter to the function.

```python
@app.route('/shop/<toy>')
def toy_detail(toy):
  pass
```

- How do you collect data from the query string using Flask?
> Answer:
> 
> A query string is a string of key/value pairs sent by the client to the server in the URL.  Use `request.args()` to parse and serialize the query string into an <span style="color:red">***ImmutableMultiDict***</span>.

- How do you collect data from the body of the request using Flask?
> Answer:
> 
> * `request.form()` - key/value pairs are in the body, from a HTML form, or when JavaScript is not <span style="color:blue">JSON encoded</span>.
> 
> * `request.json()` - parsed JSON data but request must have *applicaiton/json* content type or use `request.get_json(force=True)` to ignore the content type. 

- What is a cookie and what kinds of things are they commonly used for?
> Answer:
> 
> Cookies are a name/string-value pair that store small bits of information on client side (browser).  Side note: everything turned into a string to include numbers and the data can be altered within them.

- What is the session object in Flask?
> Answer:
> 
> The session object:
> 
> * contain info for the current browser
> 
> * preserve type (list stay as lists, etc.)
> 
> * are "signed" so users can not modify data contained in them

- What does Flask's `jsonify()` do?
> Answer:
> 
> `josnify()` serialilzes data to JSON and wraps it in a **Response** applying *applicaiton/json* mimetype.
