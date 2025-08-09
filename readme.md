# 🗳️ 정치적 성향 테스트 (Political Compass Test)

당신의 정치적 좌표를 2차원 평면에서 확인해보세요!

## 📖 프로젝트 소개

이 프로젝트는 경제적 성향(좌파-우파)과 사회적 성향(자유주의-권위주의)을 측정하여 
사용자의 정치적 위치를 2차원 좌표계에서 시각화해주는 웹 애플리케이션입니다.

총 28개의 질문(경제 14개, 사회 14개)에 답하면 Political Compass 차트에서 
자신의 정치적 성향을 확인할 수 있습니다.

## ✨ 주요 기능

- 📊 **28개 질문 기반 정치 성향 측정**
  - 경제적 성향: 좌파 ↔ 우파
  - 사회적 성향: 자유주의 ↔ 권위주의

- 📈 **실시간 진행률 표시**
  - 답변 진행 상황을 시각적으로 확인

- 🎯 **2D 좌표계 결과 시각화**
  - Plotly.js를 활용한 인터랙티브 차트
  - 4개 사분면으로 나뉜 정치적 스펙트럼

- 📱 **반응형 웹 디자인**
  - 모바일, 태블릿, 데스크톱 지원

- 🔄 **테스트 재시작 기능**
  - 언제든지 새로운 테스트 가능

## 🛠️ 기술 스택

### Backend
- **Python 3.8+**
- **Flask** - 웹 프레임워크
- **Flask-CORS** - CORS 처리

### Frontend  
- **HTML5/CSS3** - 마크업 및 스타일링
- **JavaScript (ES6+)** - 동적 기능
- **Plotly.js** - 데이터 시각화

### Design
- **CSS Grid/Flexbox** - 레이아웃
- **CSS Animations** - 인터랙션 효과

## 🚀 설치 및 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/yourusername/political-compass-test.git
cd political-compass-test
```

### 2. 가상환경 설정 (권장)
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python app.py
```

### 5. 브라우저에서 접속
```
http://localhost:5000
```

## 📁 프로젝트 구조

```
political-compass-test/
│
├── app.py                 # Flask 메인 애플리케이션
├── requirements.txt       # Python 의존성 목록
├── README.md             # 프로젝트 설명서
│
├── templates/            # HTML 템플릿
│   └── index.html        # 메인 페이지
│
└── static/              # 정적 파일 (선택사항)
    ├── css/
    ├── js/
    └── images/
```

## 🎮 사용 방법

1. **테스트 시작**: 웹사이트 접속 후 첫 번째 질문부터 시작
2. **질문 답변**: 각 질문에 대해 5단계 척도로 답변
   - 강하게 반대 (-2점)
   - 반대 (-1점)  
   - 중립 (0점)
   - 동의 (+1점)
   - 강하게 동의 (+2점)
3. **진행률 확인**: 상단 진행률 바에서 진행 상황 확인
4. **결과 확인**: 모든 질문 완료 후 "결과 확인하기" 버튼 클릭
5. **결과 분석**: 2D 차트에서 자신의 정치적 위치 확인

## 📊 결과 해석

### 4개 사분면
- **🔴 권위주의 좌파**: 경제적 평등 + 사회적 통제
- **🔵 권위주의 우파**: 자유시장 + 전통적 가치
- **🟢 자유주의 좌파**: 경제적 평등 + 사회적 자유
- **🟣 자유주의 우파**: 자유시장 + 개인의 자유

## 🤝 기여하기

1. 이 저장소를 Fork
2. 새로운 기능 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경사항 커밋 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

### 기여 아이디어
- [ ] 더 많은 질문 추가
- [ ] 다국어 지원
- [ ] 결과 공유 기능
- [ ] 통계 데이터 저장
- [ ] 모바일 앱 버전
- [ ] 역대 유명 정치인들과 비교 기능

## 📝 할 일 목록

- [ ] 데이터베이스 연동 (사용자 결과 저장)
- [ ] 소셜 미디어 공유 기능
- [ ] 결과 PDF 다운로드
- [ ] 정치인/정당과의 비교 기능
- [ ] 영어 번역
- [ ] Docker 컨테이너화
- [ ] 배포 자동화 (CI/CD)

## 🌐 데모

[라이브 데모 보기](https://your-demo-url.com) (추후 배포 후 링크 추가)

## 📸 스크린샷

### 메인 화면
![메인 화면](screenshots/main.png)

### 질문 화면  
![질문 화면](screenshots/questions.png)

### 결과 화면
![결과 화면](screenshots/result.png)

## ⚠️ 주의사항

- 이 테스트는 교육 및 오락 목적으로 제작되었습니다
- 실제 정치적 성향을 100% 정확히 반영하지 않을 수 있습니다
- 질문과 가중치는 주관적 해석이 포함되어 있습니다

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👨‍💻 개발자

**당신의 이름**
- GitHub: [@yourusername](https://github.com/yourusername)
- 이메일: your.email@example.com

## 🙏 감사의 말

- [Political Compass](https://www.politicalcompass.org/) - 원본 아이디어 영감
- [Plotly.js](https://plotly.com/javascript/) - 차트 라이브러리
- [Flask](https://flask.palletsprojects.com/) - 웹 프레임워크

---

⭐ 이 프로젝트가 유용하다면 Star를 눌러주세요!
```

## 추가로 필요한 파일들:

### 1. LICENSE 파일
```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 2. .gitignore 파일
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Flask
instance/
.webassets-cache

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log


