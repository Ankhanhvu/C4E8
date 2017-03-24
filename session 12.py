from flask import Flask

app = Flask(__name__)

image_list = [
    {
        "src": "https://s-media-cache-ak0.pinimg.com/originals/83/35/a3/8335a3c583e5b7ffeb01606ec141c612.jpg",
        "title": " cute",
        "text": "vietnam"
    },
    {
        "src": "https://s-media-cache-ak0.pinimg.com/originals/ac/20/09/ac20090f0d3b0ce879419d7968156b2a.jpg",
        "title": "adorable",
        "text": "korea"
    },
    {
        "src": "http://cdn.dogbreedsdb.com/img/2016-11-20/corgi-butt-2-1_1479630898785.jpg",
        "title": "sexy",
        "text": "US"
    },
    {
        "src": "http://cdn.dogbreedsdb.com/img/2016-11-20/corgi-11-1_1479648681136.jpg",
        "title": "fluffy"
        "text": "japan"
    }
]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/pets")
def pets():
    return render_template("pets.html", image_list = image_list)

if __name__ == '__main__':
    app.run()
