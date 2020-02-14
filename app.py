from flask import Flask, request
import test
app = Flask(__name__)
app.config["DEBUG"]=True

@app.route("/",methods=["GET","POST"])
def adder_page():
    if request.method=="POST":
        str1=request.form["string1"]
        str2=request.form["string2"]
        result=test.similarity(str1,str2)
        return '''
            <html>
                <body>
                
                <p>Similarity Index {result}</p>
                
                
                </body>
            </html>
        '''.format(result=result)
    
              
        
    return '''
        <html>
            <body>
                <p>Enter two strings:</p>
                <form method="post" action=".">
                    <p><input name="string1" /></p>
                    <p><input name="string2" /></p>
                    <p><input type="submit" value="Similarity Check" /></p>
                </form>
            </body>
        </html>
    '''
if __name__== '__main__':
    app.run()
