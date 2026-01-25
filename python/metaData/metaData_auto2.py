from PIL import Image
import os

def remove_metadata(image_path, output_path=None):
    try:
        img = Image.open(image_path)
        
        file_name = os.path.basename(image_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        file_extension = os.path.splitext(file_name)[1].lower()
        
        if output_path is None:
            output_path = os.path.join(
                os.path.dirname(image_path),
                f"{file_name_no_ext}_removed{file_extension}"
            )
        
        data = list(img.getdata())
        img_without_metadata = Image.new(img.mode, img.size)
        img_without_metadata.putdata(data)
        
        if file_extension.lower() in ['.jpg', '.jpeg']:
            img_without_metadata.save(output_path, 'JPEG', quality=95)
        elif file_extension.lower() == '.png':
            img_without_metadata.save(output_path, 'PNG')
        else:
            print(f"지원하지 않는 형식입니다: {file_extension}")
            return
        
        print(f"✓ 원본 파일: {file_name}")
        print(f"✓ 메타데이터 제거 완료!")
        print(f"✓ 저장 경로: {output_path}")
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}")

def print_metadata(image_path):
    """
    이미지의 메타데이터를 출력합니다.
    
    Args:
        image_path (str): 이미지 파일 경로
    """
    try:
        img = Image.open(image_path)
        file_name = os.path.basename(image_path)
        
        print("\n" + "=" * 60)
        print(f"파일명: {file_name}")
        print("=" * 60)
        
        # 기본 이미지 정보
        print(f"형식: {img.format}")
        print(f"크기: {img.size[0]} x {img.size[1]} (가로 x 세로)")
        print(f"모드: {img.mode}")
        print()
        
        # EXIF 메타데이터
        exif_data = img.getexif()
        if exif_data:
            print("📷 EXIF 메타데이터:")
            print("-" * 60)
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                # 길이가 긴 값은 일부만 표시
                if isinstance(value, bytes):
                    value = f"<bytes: {len(value)} bytes>"
                elif len(str(value)) > 50:
                    value = str(value)[:50] + "..."
                print(f"  {tag_name}: {value}")
        else:
            print("📷 EXIF 메타데이터: 없음")
        
        print()
        
        # PNG 메타데이터
        if img.format == 'PNG' and hasattr(img, 'info'):
            if img.info:
                print("🖼️ PNG 메타데이터:")
                print("-" * 60)
                for key, value in img.info.items():
                    if isinstance(value, bytes):
                        value = f"<bytes: {len(value)} bytes>"
                    elif len(str(value)) > 50:
                        value = str(value)[:50] + "..."
                    print(f"  {key}: {value}")
            else:
                print("🖼️ PNG 메타데이터: 없음")
        
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"✗ 메타데이터 읽기 오류: {e}")

def main():
    user_input = input().strip()
    if not user_input:
        print("이미지 경로를 입력하세요.")
        return

    img_path = user_input.strip('"')
    print(f"이미지 경로: {img_path}")

    print_metadata(img_path)
    remove_metadata(img_path)

    print_metadata(img_path.replace(
        os.path.basename(img_path),
        os.path.splitext(os.path.basename(img_path))[0] + "_removed" + os.path.splitext(os.path.basename(img_path))[1]
    ))

if __name__ == '__main__':
    main()