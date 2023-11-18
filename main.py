from website import create_app

app = create_app()

if __name__ == "__main__": # only if we run this file NOT import. 
    app.run(debug=True) # only want to run web server if we run this file directly. debug=True means everytime we make change to any of Python code it's going to auto rerun the web server