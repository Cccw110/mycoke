import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='🗺多页面应用',page_icon='📝',layout='wide')

st.markdown("""
<h2 style="font-family: 'SimSun', serif; color: blue; margin-bottom: 0;">
    广西职业师范学院 <a name="Name"></a>
</h2>
<p style="color: blue; font-size: 1rem; margin-top: 0;">Ghuangxi Vocational Normal University</p>
</p>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["数字档案", "南宁美食数据"])

with tab1:
    st.title("学生 牛魔-数字档案")
    st.header("🔑基础信息")
    st.markdown('学生ID: :green[123456]')
    st.markdown('当前时间: :green[2025-6-4 16:15:59]')
    st.text("|精神状态✅正常")
    st.markdown('当前教室  :green[实训楼301] |安全等级:安全')

    st.subheader('技能矩阵')
    # 定义列布局，分成3列
    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言", value="90%", delta="5%")
    c2.metric(label="python", value="76%", delta="6%")
    c3.metric(label="java", value="80%", delta="-10%", delta_color="off")

    st.header("streamlit课程进度")
    st.progress(33)

    st.subheader('🔐 最新代码成果')
    # 创建要显示的Python代码块的内容
    python_code = '''def matrix_breach():
        while True:
              if detect_vulnerablity():
                  exploit()
                  return "ACCESS GRANTED"
              else:
                   stealth_evade()
    '''
    # 创建一个代码块，用于展示python_code的内容
    # 并设置language为None，即该代码块无语法高亮
    st.code(python_code, language=None)

    # 定义数据,以便创建数据框
    data = {
        '日期':["2023-10-01", "2023-10-05", "2023-10-12"],
        '任务':["学生数学档案", "课程管理系统", "数据图表展示"],
        '状态':["✅完成"," 进行中","❌未完成"],
         '难度':["★★☆☆☆","★☆☆☆☆","★★★☆☆"]
    }
    # 定义数据框所用的索引
    index = pd.Series([0,1,2])
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)
    st.table(df)

    st.subheader('🔐 最新代码成果')
    # 创建要显示的Python代码块的内容
    python_code = '''def matrix_breach():
        while True:
              if detect_vulnerablity():
                  exploit()
                  return "ACCESS GRANTED"
              else:
                   stealth_evade()
    '''
    # 创建一个代码块，用于展示python_code的内容
    # 并设置language为None，即该代码块无语法高亮
    st.code(python_code, language=None)

    st.text('>> SYSTEM NESSAGE:下一个任务目标已解锁...')
    st.text('>>TARGET:课程管理系统')
    st.text('>> COUNTDOWNN:2025-06-03 15:24:58')
    st.text('系统状态：在线 连接状态：已加密')

with tab2:
    st.header("")

    df = pd.DataFrame({
        "latitude":[22.833023,22.849208,22.814160,22.818192,22.830622],
        "longitude":[108.403855,108.320469,108.321510,108.292848,108.371383]})
    # 设置索引列的名称
    df.index.name='序号'

    st.subheader('南宁地图')
    st.map(df)
    data = {
        '  ': ['复记老友粉', '好友缘', '星艺会尝不忘', '白妈螺蛳粉', '高峰柠檬鸭'],
        ' ': [4, 4.8, 4.2, 4.3, 4.4],
    }

    df=pd.DataFrame(data)
    st.header('⭐️餐厅评分')
    st.bar_chart(df,y=' ',x='  ')
    df.set_index=('name')


    st.header('🔔不同类型餐厅价格')

    # 餐厅数据

    data=({
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "位置X": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "位置Y": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    })
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3,4,5], name='序号')
    # 将新索引应用到数据框上
    df.index = index
    df_indexed=df.set_index('类型')
    st.line_chart(df_indexed)

    # 定义数据,以便创建数据框
    data = {
        '时段':[11.0, 11.5,12.5],
        '复记老友粉':[200, 150, 180],
        '星艺会尝不忘':[120, 160, 123],
        '高峰柠檬鸭':[110, 100, 160],
    }


    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    # 修改df，用月份列作为df的索引，替换原有的索引
    df.set_index('时段', inplace=True)
    index = pd.Series([1, 2, 3,], name='序号')

    st.subheader("⏰用餐高峰时段")
    # 通过y参数筛选显示1、2、3号门店的数据
    st.area_chart(df, y=['星艺会尝不忘','高峰柠檬鸭','复记老友粉'])

    # 模拟数据
    data = {
        "餐厅名称": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "价格（元）": [15, 20, 25, 35, 50],
    }
    df = pd.DataFrame(data)



    # 餐厅详情
    st.header("餐厅详情")
    selected_restaurant = st.selectbox("选择餐厅查看详情", df["餐厅名称"])
    selected_df = df[df["餐厅名称"] == selected_restaurant]
    st.write(f"评分：{selected_df.iloc[0]['评分']}/5.0")
    st.write(f"价格：{selected_df.iloc[0]['价格（元）']}元")
    st.write("推荐菜品:特色套餐,地方小吃,时令蔬菜")
    # 当前拥挤程度
    import streamlit as st
    import pandas as pd
    st.header("拥挤程度")
    st.progress(94)

    st.header("当前拥挤程度")
    st.markdown('###### 94%拥挤')
    st.progress(94)
    st.title("🎲今日午餐推荐")
    if st.button('帮我选午餐'):
        st.write('`*星怡会尝不忘*`')
        st.image("https://tse2-mm.cn.bing.net/th/id/OIP-C.i982znXoIr1SAPGvh_VfVwHaFd?w=239&h=180&c=7&r=0&o=5&pid=1.7")
