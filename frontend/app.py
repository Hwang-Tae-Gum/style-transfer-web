import streamlit as st
import requests
from PIL import Image
import io
import base64

st.title("이미지 스타일 변경 (Diffusion Model)")

st.write("원하는 콘텐츠 이미지를 업로드하고 적용할 스타일을 설명해주세요.")

col1, col2 = st.columns(2)

with col1:
    content_image_file = st.file_uploader("콘텐츠 이미지 업로드", type=["png", "jpg", "jpeg"])
    style_prompt = st.text_input("적용할 스타일 (예: van gogh painting, cyberpunk, watercolor)", "")
    if content_image_file is not None:
        st.image(Image.open(content_image_file), caption="업로드된 콘텐츠 이미지", use_container_width=True)

with col2:
    if st.button("스타일 변경"):
        if content_image_file is None or not style_prompt:
            st.warning("콘텐츠 이미지와 스타일 설명을 모두 입력해주세요.")
        else:
            st.write("스타일 변경 중...")
            files = {'content_image': content_image_file.getvalue()}
            data = {'style_prompt': style_prompt}
            try:
                response = requests.post("http://localhost:5000/style_transfer", files=files, data=data)
                response.raise_for_status()
                result_data = response.json()
                if 'result_image' in result_data:
                    result_image_base64 = result_data['result_image']
                    result_image_bytes = base64.b64decode(result_image_base64)
                    result_image = Image.open(io.BytesIO(result_image_bytes))
                    st.image(result_image, caption="스타일 변경 결과", use_container_width=True)
                    image_bytes_download = io.BytesIO()
                    result_image.save(image_bytes_download, format="PNG")
                    st.download_button(
                        label="결과 이미지 다운로드 (PNG)",
                        data=image_bytes_download.getvalue(),
                        file_name="styled_image.png",
                        mime="image/png",
                    )
                elif 'error' in result_data:
                    st.error(f"오류: {result_data['error']}")
                else:
                    st.error("알 수 없는 오류가 발생했습니다.")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 오류: {e}")
            except Exception as e:
                st.error(f"처리 오류: {e}")