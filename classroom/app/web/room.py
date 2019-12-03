import os

from app.forms.room import UploadForm
from app.models.room import Room
from app.models.base import db
from . import web
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


# curriculum 课程
@web.route('/curriculum')
def curriculum():
    return '111'


# curriculum 课程
@web.route('/latelyupload')
def LatelyUpload():
    return '最近上传'


# chapter 章节
@web.route('/chapter')
def chapter():
    return 'chapter'


# 上传
@web.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm(request.form)
    if request.method == 'POST' and form.validate():
        room = Room()
        room.set_attrs(form.data)

        # image = request.files.get('image')
        # # 对文件名进行包装，为了安全,不过对中文的文件名显示有问题
        # filename = secure_filename(image.filename)
        # image.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
        # room
        # room.set_attrs(form.data)

        db.session.add(room)
        db.session.commit()
        return redirect(url_for('web.LatelyUpload'))

    elif request.method == 'GET':
        return render_template('upload.html', form={'data': {}})
    else:
        return form.errors
