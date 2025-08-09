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
5. 라이브러리 설치
    ```
    pip install google-adk
    pip install google-genai
    ```
6.  Key 생성

    > https://aistudio.google.com -> Get API Key