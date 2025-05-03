#스타일 변환 웹 
- Diffusion 모델을 사용하여 사용자가 업로드한 이미지의 스타일을 다른 스타일로 변환하는 웹.

## 주요 기능
- stramlit을 이용한 사용자 친화적인 웹 인터페이스
- 이미지 파일 형식 지원
- 텍스트 설명을 기반으로 이미지 스타일 변환
- Diffusion 모델 (Stable Diffusion) 활용
- 스타일 변환 결과 이미지 다운로드 기능

## 기술 스택
- 프런트엔드: Streamlit(Python)
- 백엔드: Flask(Python)
- 이미지 처리: PIL(Pillow)
- Diffusion 모델: Diffusers (Hugging Face Transformers)

## 설치 방법 (로컬 실행)
1. Python (3.9 이상 권장)을 설치합니다.
2. 이 저장소를 클론합니다.
```
git clone https://github.com/Hwang-Tae-Gum/style-transfer-web.git
cd style-transfer-web
```
3. 가상 환경을 생성하고 활성화합니다.
```
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```
4. 필요한 라이브러리를 설치합니다.
```
pip install -r app/requirements.txt
pip install -r frontend/requirements.txt
```
5. 백엔드 서버를 실행합니다.
```
python -m app.app
```
6. 새로운 터미널을 열고 프런트엔드 애플리케이션을 실행합니다.
```
cd frontend
streamlit run app.py
```
7. 웹 브라우저에서 http://localhost:8501로 접속합니다.

## 사용 방법
1. 웹사이트에 접속하면 이미지 업로드 섹션과 스타일 입력 필드가 나타납니다.
2. 원하는 콘텐츠 이미지를 업로드합니다.
3. 적용하고 싶은 스타일을 텍스트로 설명합니다(예: "a painting in the style of Van Gogh", "cyberpunk", "watercolor").
4. "스타일 변경" 버튼을 클릭하면 서버에서 이미지 스타일 변환이 진행됩니다.
5. 결과 이미지가 화면에 표시되며, 다운로드 버튼을 통해 PNG 형식으로 저장할 수 있습니다.

## 향후 계획 (Future Work)
- 모델 파인튜닝: 특정 스타일이나 이미지 유형에 더 잘 반응하도록 Diffusion 모델을 파인튜닝할 계획입니다. 사용자 피드백을 기반으로 데이터셋을 구축하고 추가 학습을 진행할 수 있습니다.
- 배포: 현재 로컬 환경에서 실행 가능하지만, 더 많은 사용자가 접근할 수 있도록 클라우드 플랫폼 (예: AWS, Google Cloud, Heroku)을 사용하여 배포를 진행할 예정입니다.
- 추가 스타일 옵션: 더 다양한 스타일 프리셋을 제공하고, 사용자가 직접 스타일 이미지를 업로드하여 적용하는 기능을 추가할 수 있습니다.
- 고급 설정: 이미지 생성 과정에 영향을 미치는 파라미터 (예: strength, guidance scale, inference steps)를 사용자가 조절할 수 있도록 인터페이스를 개선할 수 있습니다.
- 실시간 스타일 변환 (고려 중): 비디오 스트림이나 웹캠 입력에 실시간으로 스타일을 적용하는 기능을 연구 중입니다.
- 사용자 계정 및 저장 기능 (고려 중): 사용자가 생성한 이미지를 저장하고 관리할 수 있는 계정 시스템 도입을 고려하고 있습니다.
- 성능 개선: 모델 추론 속도를 최적화하고, 더 효율적인 리소스 관리를 위한 방안을 모색할 것입니다.
- 사용자 인터페이스/경험 개선: 더 직관적이고 사용하기 쉬운 인터페이스를 제공하기 위해 지속적으로 UI/UX를 개선할 예정입니다.

## 감사의 말씀

이 프로젝트는 [Hugging Face](https://huggingface.co/)의 [Diffusers](https://github.com/huggingface/diffusers) 라이브러리와, 
핵심 모델로 **[CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4)**를 사용합니다.
