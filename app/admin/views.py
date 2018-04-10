from . import admin
@admin.route("/")
def index():
    return "<html><body><h1>admin views</h1></body></html>"