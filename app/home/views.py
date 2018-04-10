from . import home
@home.route("/")
def index():
    return "<html><body><h1>home views</h1></body></html>"