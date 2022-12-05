# Service Plan 

## About
service Plan은 QA 또는 기획과정에 필요한 flow를 효율적으로 정리하기 위한 파일럿 프로젝트입니다. 
기획과 개발을 동시에 진행한 프로젝트로 이전 파일럿 프로젝트(QA 웹앱) 기초로 개발되었습니다. 
개발에 사용한 프레임워크는 백엔드 Django(python), 프론트엔드 Bootstrap5, sortablejs 를 사용하였습니다. 
기본 컨셉은 사용자가 테스크(블럭)을 생성하고 블럭의 우선순위(위치)를 정하거나 코멘트를 입력, 공유하는 어플리케이션입니다. 
사용자 인증과 관련된 작업은 진행하지 않았고 비즈니스로직 부분만 개발 완료한 프로젝트입니다. 


### 서비스 구조
어플리케이션 구조는 아래와 같습니다. 
```
├── TESTSET1
│   ├── Scenario1
│   ├── Scenario2
│   └── Scenario3
│    	├── Task1
│       │   ├── comment1
│       │   └── comment2
│       └── Task2
└── TESTSET2
```
1. TESTSET은 가장 큰 범주에 속하고 하위 범주로 Scenario와 Task 그리고 comment를 가집니다. 
2. Scenario는 두번째 큰 범주로 TESTSET에 포함되고 하위 범주로 TASK를 가집니다. 
3. TASK는 Scenairo에 포함되고 TASK 사이에 순서(order)를 사용자가 설정할 수 있습니다. 
4. comments는 Task에 대한 댓글로서 상태(select)값을 입력할 수 있습니다. 

## Structure

### Django App folder Structure

```
├── async_jobs
├── landing
├── media
├── node_modules
├── quality
├── servicePlan
├── templates
├── user_profile
├── manage.py
├── package.json
├── package-lock.json
├── requirements.txt
└── README.md
```
#### 앱 설명
1. async_jobs : 본 프로젝트는 DRF 같은 3rd party 기능을 이용하지 않고 django view를 이용여 프론트엔드의 비동기 작업을 진행하였고 위와 같은 기능을 담당하기 위해 async_jobs 앱을 이용하였습니다.  
2. landing : 랜딩페이지를 출력하는 앱
3. node_modules : sortablejs 패키지 설치 폴더
4. quality : 서비스의 CRUD 관련 앱 
5. servicePlan : project folder
6. templates : allauth 등 템플릿 파일 폴더 
7. user_profile : 사용자 정보 입력 앱(작업 전)
8. ...

### Part1. User Flow
### Part2. Service Flow
### Part3. Business logic

