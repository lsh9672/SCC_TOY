# SCC_TOY

* 우분투 서버에서 python 파일 생성 및 실행 (맛보기)

1. ssh를 이용해 우분투(20.04LTS) 서버 접속  
```
> ssh syslet@192.168.0.10
```
2. python-virtualenv(모듈 버전 충돌을 막기 위해)를 이용하여 가상환경 구축 
```
$ pip3 install virtualenv
```
```
$ sudo apt-get install virtualenv
```
3. 작업용 디렉토리(scc_toy) 생성 
```
$ mkdir scc_toy && cd scc_toy
$ virtualenv venv3
$ source venv3/bin/activate
```
4. python-flask 사용을 위해 pip를 이용해 설치
```
$ pip3 install flask
```
5. vim을 이용해 파이썬 파일생성 및 코드 작성
```
$ vim first_project.py
```
6. 포트번호 8899로 파일 실행
```
$ python3 first_project.py
```
7. 크롬을 이용해서 서버 접속(우분투서버 ip:8899 로 접속) - ip:포트/ => 텍스트 , ip:포트/text1 => 태그(1)를 넣은 텍스트 각각 실행
```
192.168.0.10:8899/
192.168.0.10:8899/text1
```
8. 추가로 flask run 명령어를 통해서도 실행 - 운영환경(default)으로 실행되어 발생하는 Warning 해결
```
$ export FLASK_ENV=development
$ flask run
```
