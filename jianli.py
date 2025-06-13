import streamlit as st
from datetime import datetime, time
from io import StringIO

st.set_page_config(page_title='个人简历生成器', page_icon='📝', layout='wide')

st.title('个人简历生成器')
st.text('使用Streamlit创建您的个性化简历')

c1, c2 = st.columns([1, 2])

with c1:
    st.markdown('## 个人信息表单')
    st.markdown('<hr style="height:2px;border:none;color:blue;background-color:blue">', 
                unsafe_allow_html=True)

    # 使用st.session_state存储所有表单数据
    name = st.text_input('姓名', key='name')
    danwei = st.text_input('单位', key='danwei')
    dianhua = st.text_input('电话', key='dianhua')
    email = st.text_input('邮箱', key='email')
    date = st.date_input("出生日期", value=None, key='date')
    sex = st.radio('性别', ['男', '女', '其他'], key='sex')
    xl = st.selectbox('学历', ['高中', '专科', '本科', '硕士研究生'], key='xl')
    yynl = st.selectbox('语言能力', ['中文', '英语'], key='yynl')
    jn = st.multiselect(
        '技能（可多选）',
        ['java', 'HTML/css', '机器学习', 'python'],
        ['python'],
        key='jn')
    age = st.slider('工作经验（年）', 0, 30, 6, key='age')
    xz = st.slider('薪资展望范围（元）', 0, 50000, (19123, 29399), key='xz')
    
    init_text = "人工智能领域研究员/工程师，专注机器学习、"\
               "深度学习与计算机视觉，具备3年+算法开发"\
               "与落地经验。擅长PyTorch/TensorFlow框架，"\
               "在CVPR/NeurIPS发表论文2篇，主导过金融风"\
               "控与医疗影像AI项目，获专利1项。致力于将"\
               "前沿AI技术转化为实际应用解决方案。"
    intro = st.text_area(label='个人简介', value=init_text, height=200, max_chars=200, key='intro')
    w3 = st.time_input("每日最佳联系时间段", datetime(2019, 7, 6, 21, 15), key='w3')
    uploaded_file = st.file_uploader('上传个人照片', type='png', key='photo')

with c2:
    st.markdown('## 简历实时预览')
    st.markdown('<hr style="height:2px;border:none;color:blue;background-color:blue">', 
                unsafe_allow_html=True)
    
    
    
    b1, b2 = st.columns([1, 1])
    with b1:
        if uploaded_file is not None:
            st.image(uploaded_file, width=150)
        st.markdown(f'**姓名**: {name}')
        st.markdown(f'**单位**: {danwei}')
        st.markdown(f'**电话**: {dianhua}')
        st.markdown(f'**邮箱**: {email}')
        st.markdown(f'**出生日期**: {date}')
    with b2:
        st.markdown(f'**性别**: {sex}')
        st.markdown(f'**学历**: {xl}')
        st.markdown(f'**工作经验**: {age}年')
        st.markdown(f'**期望薪资**: {xz[0]} - {xz[1]}元')
        st.markdown(f'**最佳联系时间**: {w3}')
        st.markdown(f'**语言能力**: {yynl}')
    
    st.markdown('### 技能')
    st.write(', '.join(jn))
    
    st.markdown('### 个人简介')
    st.write(intro)

