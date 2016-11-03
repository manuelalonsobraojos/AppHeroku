from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

	
    return """
	<html>
    <head>
        <title>Home Page</title>
    </head>
    <body> 
        <h1>Pagina principal</h1>
    </body> 
</html> """ 
 

@app.route('/user/<nombre>', methods=['GET'])
def usuario(nombre):
	
    return "<h1>bienvenido %s</h1>" %(nombre)


	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
