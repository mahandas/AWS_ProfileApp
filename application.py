from flask import Flask,render_template, request,jsonify,Response

application = Flask(__name__)
    
@application.route('/')
def sessions():
    return render_template('index.html')

@application.route('/mobileversion')
def mobileversion():
    return render_template('mobile.html')
# @application.route('/ChatApp/<UUID>')
# def testChatApp(UUID):
    # y = ""
    # for k,v in ClientLanguageMap.items():
      # y = y + k + "-" + v + ","
    # return render_template('ChatApp.html', name=UUID, valva=y[:-1])
    
    
    

if __name__ == '__main__':
    application.run(debug = True)
