from flask import flash,redirect, url_for, render_template, abort, request,Blueprint
from flaskblog.posts.forms import PostForm
from flaskblog.users.utils import save_post_picture
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form=PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_post_picture(form.picture.data)
        else:
            picture_file = 'default_post.jpg'
        post = Post(title=form.title.data, content=form.content.data, image_file=picture_file, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Post has successfully been added', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', legend='NEW POST', form=form)




@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='Post', post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_post_picture(form.picture.data)
            post.image_file=picture_file
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash('Your Post Has Been Updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='UPDATE POST')






@posts.route("/post/<int:post_id>/delete", methods=['GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post has been Deleted', 'success')
    return redirect(url_for('main.home'))


@posts.route("/post/<int:post_id>/delete_confirmation", methods=['GET', 'POST'])
@login_required
def delete_confirmation(post_id):
    post = Post.query.get_or_404(post_id)
    should_delete = True
    return render_template('post.html', post=post, should_delete=should_delete)
