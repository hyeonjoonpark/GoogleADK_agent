# Google ADK를 활용한 agent 개발

### 환경설정

1. Python 3.9 버전 이상 설치
2. Visual Studio Code 설치
3. Workspace 생성
4. Python 가상환경 생성

    ```
    # Window
    python -m venv .venv // 가상환경 생성
    ```
   
    ```
    # Window
    .venv\Scripts\activate.bat // 가상환경 접속
    ```

    가상화면에서 계속 빠져나가는 경우
    보기 > 명령팔레트 (Ctrl + Shift + P) > Python Interpreter > .venv 선택 : 터미널의 디폴트를 가상환경으로 설정
5. 라이브러리 설치
    ```
    pip install google-adk
    pip install google-genai
    ```
6.  Key 생성

    > https://aistudio.google.com -> Get API Key


### 폴더 구조
```
PROJECT_FOLDER
    - /.venv(가상환경)
    - /agents(실제 개발 폴더)
        - /greeting_agent
        - /capital_agent
        - /search_agent
    - README.md
```

### ADK 생성 (CMD)

```
adk create [이름]
```

### ADK 실행
```
adk web [이름] // Web버전으로 실행
```

`adk web [상위폴더이름]` 을 실행하면 하위에 생성된 agent가 전부 WEB버전으로 실행된다

ETC) `adk web agents` -> 하위에 있는 greeting_agent, capital_agent, search_agent를 전부 실행

### .env 파일
`adk create 생성할 이름` 으로 생성시 .env 파일이 만들어진다
.env 파일 안에 GOOGLE_API_KEY 부분에 자신이 발급받은 API_KEY가 들어있다 (중요 정보이기 때문에 GIT등에 올릴 때는 조심하자)