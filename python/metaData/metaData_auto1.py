from PIL import Image
import piexif
import os

def remove_metadata_with_pillow(input_path, output_path):
    try:
        image = Image.open(input_path)
        
        data = list(image.getdata())
        image_without_metadata = Image.new(image.mode, image.size)
        image_without_metadata.putdata(data)
        
        image_without_metadata.save(output_path, "JPEG")
        print(f"✓ 메타데이터 제거 완료: {output_path}")
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}")

def remove_exif_with_piexif(input_path, output_path):
    try:
        image = Image.open(input_path)
        
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        
        image_without_exif.save(output_path, "JPEG")
        print(f"✓ EXIF 제거 완료: {output_path}")
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}")

def check_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        
        print(f"\n이미지: {image_path}")
        print(f"포맷: {image.format}")
        print(f"크기: {image.size}")
        print(f"모드: {image.mode}")
        
        if hasattr(image, '_getexif') and image._getexif() is not None:
            exif_data = image._getexif()
            print("EXIF 데이터 발견:")
            for tag_id, value in exif_data.items():
                tag_name = piexif.TAGS["0th"][tag_id]["name"]
                print(f"  {tag_name}: {value}")
        else:
            print("EXIF 데이터 없음")
            
    except Exception as e:
        print(f"✗ 오류 발생: {e}")

def remove_png_metadata(input_path, output_path):
    try:
        image = Image.open(input_path)
        
        data = list(image.getdata())
        image_without_metadata = Image.new(image.mode, image.size)
        image_without_metadata.putdata(data)
        
        image_without_metadata.save(output_path, "PNG")
        print(f"✓ PNG 메타데이터 제거 완료: {output_path}")
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}")

def remove_metadata_from_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    
    try:
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(supported_formats):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)
                
                image = Image.open(input_path)
                data = list(image.getdata())
                image_without_metadata = Image.new(image.mode, image.size)
                image_without_metadata.putdata(data)
                image_without_metadata.save(output_path)
                
                print(f"✓ 처리 완료: {filename}")
                
    except Exception as e:
        print(f"✗ 오류 발생: {e}")

if __name__ == "__main__":
    input_image = "original_image.jpg"
    output_image = "metadata_removed.jpg"
    
    # 1. 메타데이터 정보 확인
    # check_image_metadata(input_image)
    
    # 2. Pillow을 사용한 메타데이터 제거
    # remove_metadata_with_pillow(input_image, output_image)
    
    # 3. PNG 이미지 처리
    # remove_png_metadata("original.png", "output.png")
    
    # 4. 디렉토리의 모든 이미지 처리
    # remove_metadata_from_directory("./images", "./images_cleaned")

# ============================================
# 설치 필요 라이브러리
# ============================================
# pip install Pillow
# pip install piexif
