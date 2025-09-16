#!/usr/bin/env python3
"""
나노바나나 커리큘럼을 특별편과 정규편으로 분리하는 스크립트
"""

def split_curriculum():
    # 정규 커리큘럼 파일 읽기
    with open('나노바나나_정규_커리큘럼.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 특별편 시작과 끝 찾기
    special_start = content.find('## 🔥 **특별 영상: 나노바나나로 만드는 놀라운 8가지 마법**')
    level1_start = content.find('## 🎯 **LEVEL 1: 기초 입문편**')
    
    if special_start == -1 or level1_start == -1:
        print("❌ 섹션을 찾을 수 없습니다.")
        return
    
    # 정규 커리큘럼 부분 추출 (특별편 제거)
    regular_content = content[:special_start] + content[level1_start:]
    
    # 정규 커리큘럼 파일 저장
    with open('나노바나나_정규_커리큘럼.md', 'w', encoding='utf-8') as f:
        f.write(regular_content)
    
    print("✅ 파일 분리가 완료되었습니다!")
    print("📚 정규 커리큘럼: 나노바나나_정규_커리큘럼.md")
    print("🔥 특별편: 나노바나나_특별편.md")

if __name__ == "__main__":
    split_curriculum()
