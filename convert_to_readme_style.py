#!/usr/bin/env python3
"""
나노바나나 커리큘럼의 모든 케이스를 README 스타일로 일괄 변환하는 스크립트
"""

import re

def convert_case_to_readme_style(content):
    """케이스 형태를 README 스타일 테이블로 변환"""
    
    # 패턴: **🖼️ Case N: 제목** 으로 시작하는 케이스들 찾기
    case_pattern = r'\*\*🖼️ (Case \d+: [^*]+)\*\*\n- \*\*입력\*\*: `([^`]+)` - ([^\n]+)\n- \*\*프롬프트\*\*: `([^`]+)`\n- \*\*출력\*\*: `([^`]+)` - ([^\n]+)'
    
    def replace_case(match):
        title = match.group(1)
        input_path = match.group(2)
        input_desc = match.group(3)
        prompt = match.group(4)
        output_path = match.group(5)
        output_desc = match.group(6)
        
        # README 스타일로 변환
        result = f"""**🖼️ {title}**

| 입력 | 결과물 |
|:---:|:---:|
| <img src="{input_path}" width="200" alt="Input Image"> | <img src="{output_path}" width="200" alt="Output Result"> |

**입력:** {input_desc} 업로드

**프롬프트:**
```
{prompt}
```"""
        
        return result
    
    # 케이스 변환 적용
    content = re.sub(case_pattern, replace_case, content, flags=re.MULTILINE)
    
    return content

def main():
    # 파일 읽기
    with open('나노바나나_영상_커리큘럼.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 변환 실행
    converted_content = convert_case_to_readme_style(content)
    
    # 파일 저장
    with open('나노바나나_영상_커리큘럼.md', 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print("✅ 모든 케이스가 README 스타일로 변환되었습니다!")

if __name__ == "__main__":
    main()
