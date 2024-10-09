import streamlit as st

st.title("내가 만든 스트림릿앱")
markdown_text = """
# 이건 헤더입니다.
## 이건 서브헤더입니다.
- 첫번째
- 두번째
## 다음은 숫자
1. 시작
2. 다음

**Bold text** and *italic text*

[This is a link](https://www.streamlit.io)


```
def hello_world():
    print("Hello, World!")
```

| Column 1 | Column 2 |
|----------|----------|
| Row 1    | Value 1  |
| Row 2    | Value 2  |

> This is a blockquote

---

![Cute Cat](https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg)

---

"""

st.markdown(markdown_text)
