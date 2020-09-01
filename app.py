from flask import Flask,request, render_template
import os
from pyshortcuts import make_shortcut


app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')

def call_external_cmd(f_name):
    op= os.path.abspath(f_name)
    os.system(f'pyinstaller {op}')
    return


@app.route('/make_exe',methods=['POST'])
def make_exe():
    
    file_a_path  = [str(x) for x in request.form.values()]
    file_abs_path=file_a_path[0]
    print(file_abs_path)
    if os.path.exists(file_abs_path) == True:
        print()

        print('all cool')
        print()
        file_name = file_abs_path.split('\\')[-1]
        print('Processing your files..')
        print()
        path_exe = call_external_cmd(file_abs_path)
        print(path_exe)
        print()    
        
        a = file_abs_path.split('\\')[0:-1]
        a.append('dist')
        exe_name=file_name.split('.')[0]
        a.append(exe_name)
        a.append(file_name.split('.')[0]+ '.exe')
        d='\\'.join(a)
        print('Your Exe file is at location : ',d)
        
        
        make_shortcut(file_abs_path, name=exe_name)
        print('Shortcut for the your application is created on Desktop')
        
        return render_template('index.html',Processing='Processing your files..just hang on for a minute..\n', prediction_text='Your application is packed and ready as a shortcut on your Desktop')
    
    else:
        return render_template('index.html', prediction_text='unable to track the location on your system')


    


if __name__ == "__main__":
    app.run(debug=True)