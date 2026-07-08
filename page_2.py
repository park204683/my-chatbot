import streamlit as st
import pandas as pd

# 하위 페이지이므로 st.set_page_config는 절대 넣지 않습니다! 바로 본문 시작:
st.title("📊 엑셀 파일 업로더 & 뷰어")
st.write("엑셀 파일을 업로드하면 데이터프레임 형태로 화면에 즉시 시각화합니다.")

uploaded_file = st.file_uploader("컴퓨터에서 엑셀 파일을 선택하세요 (.xlsx, .xls)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success(f"✅ 파일 업로드 성공! (총 {df.shape[0]}행, {df.shape[1]}열)")
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            st.write("### 🔍 데이터 요약")
            st.write("**컬럼 목록:**")
            st.write(list(df.columns))
            
            if not df.select_dtypes(include=['number']).empty:
                st.write("**간단한 통계 요약:**")
                st.dataframe(df.describe().T[['mean', 'min', 'max']])
        
        with col2:
            st.write("### 📄 데이터 본문")
            st.dataframe(df, use_container_width=True)
            
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("👆 위 영역에 엑셀 파일을 드래그 앤 드롭하거나 클릭하여 업로드해 주세요.")