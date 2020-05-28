from flask import Flask, render_template, request
import hashlib
a = Flask(__name__)
@a.route('/')
def fun():
    return render_template('sha.html')

@a.route('/',methods=['POST'])
def fun1():
    text = request.form['example']
    print(request.form['sha'])
    if request.form['sha']=='SHA-256':
        t1 = hashlib.sha256()
        text1=text.split("\n")
        for byte_block in text1:
            byte_block=byte_block.encode('utf-8')
            t1.update(byte_block)
        t2=t1.hexdigest()
    elif request.form['sha']=='SHA-512':
        t1 = hashlib.sha512()
        text1 = text.split("\n")
        for byte_block in text1:
            byte_block = byte_block.encode('utf-8')
            t1.update(byte_block)
        t2 =t1.hexdigest()
    elif request.form['sha']=='SHA-1':
        t1 = hashlib.sha1()
        text1 = text.split("\n")
        for byte_block in text1:
            byte_block = byte_block.encode('utf-8')
            t1.update(byte_block)
        t2 =t1.hexdigest()
    elif request.form['sha']=='MD-5':
        t1 = hashlib.md5()
        text1 = text.split("\n")
        for byte_block in text1:
            byte_block = byte_block.encode('utf-8')
            t1.update(byte_block)
        t2 =t1.hexdigest()
    print(t2)
    return render_template("sha.html", t2=t2, text=text)


if __name__ == '__main__':
    a.run()