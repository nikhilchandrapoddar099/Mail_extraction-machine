
#for mail Extraction online
import pymysql
import time
from flask import Flask, render_template, request
import regex
app = Flask(__name__)


@app.route('/')
def student():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])

def fun1():
   if request.method == 'POST':
      result1= request.form["message"]
      mg = result1
      mg=mg.split(' ')

      n=request.form['names']
      nm=n
      t = time.asctime(time.localtime(time.time()))
      n=n.split(' ')
      n=n[0]

      result1=regex.findall(r'[\w.-]+@[\w\.-]+', result1)

      d = {}
      k = 1
      o=' '
      for i in result1:
         d[k]=i

         k+=1
         o=o+','
         o=o+i

      s=''
      for i in mg:
          if "'" in i:
              i=i.replace("'","_")
              i=i+" "
              s+=i
          else:
              i=i+" "
              s+=i


      print(nm)
      print(s)
      print(o)
      print(t)
      con = pymysql.connect(host="remotemysql.com", port=3306, user="AbiYhOmhEP", password="nO6VcgUDwU",db="AbiYhOmhEP")
      c = con.cursor()

      qry = "insert into try(name,message,output,times) values('%s','%s','%s','%s')" % (nm,s,o,t)
      c.execute(qry)
      con.commit()
      con.close()


      return render_template("result.html",result = d,name=n)


if __name__ == '__main__':
   app.run(host="127.0.0.1",port=8080,debug=True)