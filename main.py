from flask import Flask,render_template,request
from pipeline import preprocessing,vectorizer,prediction
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    positive=0
    negative=0
    page_name = "Pipe line"
    comment = None
    if request.method == 'POST':
        comment = request.form['feed']
        preped_text=preprocessing(comment)
        vected=vectorizer(preped_text)
        result=prediction(vected)
        if result=='negative':
            negative+=1
            
        else:
            positive+=1
    return render_template('index.html', feed=comment, page=page_name,postive=positive,negative=negative)

        
