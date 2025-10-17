from flask import Flask    

# Creates the Flask app
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')    # defines the home route   
def hello(): 
    return 'HELLO'
  
if __name__=='__main__': 
   app.run(debug=True)


"""
Explanation:

    Flask(__name__): Creates the Flask app.
    @app.route('/'): Defines the home route (/).
    def hello(): creates a function that is bound with '/' route and returns "HELLO" 
                when the root page is accessed.
    app.run(debug=True): runs the app in debug mode. 
                        It ensure that app is not need to restart manually if any 
                        changes are made in code.

"""