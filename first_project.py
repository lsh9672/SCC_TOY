#플라스크를 사용
from flask import Flask
#FLASK의 생성자로 __name__(현재 모듈을 의미함)을 인수로 받는다
app=Flask(__name__)
#라우팅 경로를 지정, URL에서 / 경로를 지정하면 아래에 써있는 함수를 실행
#route()의 인자가 바로 아래의 함수로 바인딩 되어서 브라우저에서 해당 URL을 입력하면 함수의 출력이 렌더링됨
@app.route('/')
def hello_toy():
	return "hello_toy_project"

@app.route('/text1')
def hello_toy2():
	return '<h1>hello_toy_priject2</h1>'

if __name__ == "__main__":
	#run()은 애플리케이션을 실행한다
	app.run(host=0.0.0.0,port='8899',debug=True)
