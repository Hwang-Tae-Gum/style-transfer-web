from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import io
import base64
import torch

model_id = "CompVis/stable-diffusion-v1-4"

pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(model_id).to("cuda" if torch.cuda.is_available() else "cpu")

def diffusion_style_transfer(content_images_bytes, style_prompts):
    try:
        content_image = Image.open(io.BytesIO(content_images_bytes)).convert("RGB")
        resized_image = content_image.resize((512, 512))

        prompt = f"a photo of a dog in {style_prompts} style"
        negative_prompt = "ugly, deformed, blurry, low quality, grotesque, mutated"
        image = pipeline(prompt=prompt, image=resized_image, guidance_scale=7.5, strength=0.6, negative_prompt=negative_prompt).images[0]

        buffered = io.BytesIO()
        image.save(buffered, format='png')
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    except Exception as e:
        raise Exception(f"Stable Diffusion 모델 처리 오류: {e}")

if __name__ == '__main__':
    try:
        with open("test_content.jpg", "rb") as f:
            content_bytes = f.read()
        style = "a painting in the style of Van Gogh"
        result = diffusion_style_transfer(content_bytes, style)
        print(f"결과 이미지 (base64): {result[:100]}...")
        result_image_bytes = base64.b64decode(result)
        result_image = Image.open(io.BytesIO(result_image_bytes))
        result_image.save("result_style.jpg")
        print("결과 이미지가 result_style.jpg로 저장되었습니다.")
    except FileNotFoundError:
        print("테스트를 위해 'test_content.jpg' 파일을 현재 디렉토리에 넣어주세요.")
    except Exception as e:
        print(f"테스트 중 오류 발생: {e}")