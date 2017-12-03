from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
   title = "Presure Watch"
   paragraph = ["A basic website for watching barametric pressure", ]

   return render_template ("index.html", title =title, paragraph = paragraph)

@app.route('/about')
def aboutpage():
   title ="About this site"
   paragraph = ['Data is pulled from a free weather API', 'The site itself runs off of a Flask framework and the graph is from Matplotlib']
   pageType = 'about'

   return render_template ("index.html", title = title, paragraph=paragraph, pageType = pageType)

@app.route('/graph')
def graphpage():
   title="Graph"
   paragraph = ['This graph shows the last 30 entries, the data is updated once per hour.']
   pageType = 'graph'

   return render_template ("graph.html", title = title, paragraph=paragraph)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
