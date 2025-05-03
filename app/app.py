from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
from .model import diffusion_style_transfer
import time

app = Flask(__name__)

@app.route('/style_transfer', methods=['POST'])
def style_transfer_endpoint():
    if 'content_image' not in request.files or 'style_prompt' not in request.form:
        return jsonify({'error': '콘텐츠 이미지와 스타일 설명을 입력해주세요.'}), 400

    content_image_file = request.files['content_image']
    style_prompt = request.form['style_prompt']

    content_image_bytes = content_image_file.read()

    try:
        result_image_base64 = diffusion_style_transfer(content_image_bytes, style_prompt)
        return jsonify({'result_image': result_image_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)