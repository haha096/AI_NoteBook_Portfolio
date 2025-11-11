from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 프로젝트 정보를 딕셔너리 형태로 전달
    project_info = {
        "developer": "나은주",
        "intro_short": "뭐든 경험을 쌓고 싶은 개발자",
        "intro_long": "이 프로젝트로 AI와 친해져 내가 경험한 프로젝트로 이름 올리고 싶다.",
        "period": "2025/11/01 ~ 2025/11/17",
        "background": "AI와 함께 공부하는 학생들이 많이지면서 노트필기와 함께 공부할 수 있는 AI를 개발하고 싶다는 생각과 함께 개발하였습니다.",
        "tech_stack": ["Spring Boot", "Python", "FastAPI", "React", "JavaScript", "HTML5", "MySQL", "Figma", "Git"],
        "core_features": [
            {
                "title": "AI 핵심 요약 기능",
                "description": "DB와 FastAPI기능을 이용해 사용자는 자료(pdf, word, ppt...)를 추가해 AI에게 요약과 해석, 설명을 부탁할 수 있습니다.",
                "image": "image.png"
            },
            {
                "title": "관련 유튜브 영상 추천",
                "description": "AI가 자료를 읽어 관련된 영상을 찾아 사용자에게 추천합니다.",
                "image": "main.png"
            },
            {
                "title": "노트필기 형식의 AI모델",
                "description": "AI모델을 학습, 조립을 하여 사용자가 \"노트필기 형식\"이라는 프롬포트를 주면 AI가 자료와 맞게 노트필기형식으로 대답"
            }
        ],
        "problem_definition": "과연 기본적인 학습과정을 AI가 어느정도 대체가 가능한가",
        "solution_process": [
            "GPT API를 가져오면서 단순한 AI와 채팅하면서 공부하는 것이 아닌 소스를 추가하고 AI가 노트필기형식을 주면서 AI 모델을 강화",
            "노트필기를 할 때 가장 중요한 부분 중 하나가 중요한 부분에 색깔을 칠하고 제목은 굵은 글씨로 한 눈에 확인 이를 토대로 노트필기 방식을 유연하게 함"
        ],
        "results": "글씨와 정렬이 가능한 노트필기 UI로 구성, 옆의 AI와 함께 자료를 읽고 요약, 해석해주는 기능 확장",
        "learnings": "고작 API키를 가져와 간단한 AI채팅 기능을 구현했을 떄 우여곡절이 많아 아직 기술이 필요하다는 것을 느낌"
    }
    return render_template('index.html', info=project_info)

if __name__ == '__main__':
    app.run(debug=True)
