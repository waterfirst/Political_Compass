# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# 정적 파일 경로 설정
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    # 필요시 추가 질문 데이터를 API로 제공
    questions = {
        "status": "success",
        "message": "Questions loaded successfully"
    }
    return jsonify(questions)

@app.route('/api/save-result', methods=['POST'])
def save_result():
    """결과 저장 API (선택사항)"""
    try:
        data = request.json
        economic_score = data.get('economic_score')
        social_score = data.get('social_score')
        
        # 여기서 데이터베이스에 저장하거나 로그 파일에 기록 가능
        print(f"결과 저장: 경제={economic_score}, 사회={social_score}")
        
        return jsonify({"status": "success", "message": "결과가 저장되었습니다."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # 개발 환경에서 실행
    app.run(debug=True, host='0.0.0.0', port=5000)