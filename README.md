# SCC_TOY

* 우분투 서버에서 python 파일 생성 및 실행 (맛보기)

1. ssh를 이용해 우분투(20.04LTS) 서버 접속  
'''
print()
'''
3. python-virtualenv(모듈 버전 충돌을 막기 위해)를 이용하여 가상환경 구축 및 작업용 디렉토리(scc_toy) 생성 
4. vim을 이용해 파이썬 파일(first_project.py) 생성
5. python-flask 사용을 위해 pip를 이용해 설치(pip3 install flask)
6. 포트번호 8899로 파일 실행(python3 first_project.py)
7. 크롬을 이용해서 서버 접속(우분투서버 ip:8899 로 접속) - ip:포트/ => 텍스트 , ip:포트/text1 => 태그(1)를 넣은 텍스트 각각 실행
8. 추가로 flask run 명령어를 통해서도 실행 - 운영환경(default)으로 실행되어 발생하는 Warning 해결(export FLASK_ENV=development - 리눅스)
