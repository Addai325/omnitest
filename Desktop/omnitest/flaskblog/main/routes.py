from flask import request,Blueprint, render_template
from flaskblog.models import Post


main = Blueprint('main', __name__)
  



@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=9, page=page)
    # posts = Post.query.filter_by(title=str(current_user.username)).order_by(Post.date_posted.desc())
    return render_template('home.html', posts=posts)



@main.route("/about")
def about():
    return render_template('about.html', title='About')
