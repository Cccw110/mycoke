import streamlit as st
from datetime import datetime, time
from io import StringIO
import numpy as np
import pandas as pd

# 侧边栏选择页面
page = st.sidebar.selectbox("选择页面", ["首页", "个人简历生成器", "音乐播放器", "南宁美食数据", "数字档案"])

# 根据选择显示不同页面内容
if page == "首页":
    st.title("首页")
    st.title('主页')
    st.image("https://www.gxvnu.edu.cn/__local/7/4F/5D/AD938A49125924C082992B16BDD_98ECEA17_BD556.jpg")
    st.text("广西职业师范学院（原广西经济管理干部学院）坐落于广西首府南宁市风景秀丽的邕江之滨、相思湖畔，是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培               养区域经济社会发展所需要的高素质应用型、技术技能型人才和职业教育师资。学校随着广西的解放而诞生，其前身为创建于1951年5月的广西省行政干部训练班。其后，为适应不同历史               时期广西经济建设需要，学校历经了广西人民革命大学、广西行政干部学校、广西经济干部学校、广西经济管理干部学院等历史沿革，并于2019年6月经教育部批准设置为“广西职业师范                   学院”。在不同历史时期，学校聚焦“服务广西经济建设”发展主线，不忘建校初心、勇担办学使命，为广西经济建设和社会发展作出了不可磨灭的突出贡献，享有良好的办学声誉和广泛               的社会影响。近年来，学校围绕“地方性、应用型、职师类”办学定位，落实“以本为本、应用为先、职师特色”办学思路，在服务地方产业转型升级和职业教育提质增效上取得显著成效              。学校拥有一支师德师风优良、学术水平较高、教学经验丰富的专兼职师资队伍，其中，取得硕士、博士学位教师427人。拥有包含自治区教学名师、模范教师、优秀专家、高校思想政治教                育卓越教师等在内的高水平教师团队，其中，广西高等学校高水平创新团队2个，自治区课程思政教学团队5个，自治区劳模创新工作室1个。在近年教学成果评选中，获国家级、自治区级              教学成果奖16项，其中，获国家级教学成果奖一等奖1项、二等奖1项；获自治区教学成果一等奖4项、二等奖6项，三等奖4项。近五年来，获厅级及以上纵向科研项目立项285项，其中国家              级1项、省部级57项、厅级227项；获省部级科研成果奖6项，其中二等奖1项、三等奖5项。学校现有12个二级学院（部），普通本科专业33个，涵盖经济学、管理学、工学、理学、教育学             、文学、法学、艺术学等八个学科。获教育部“新工科”研究与实践项目1个，自治区级新工科、新文科研究与实践项目2项，广西高等学校特色专业及课程一体化建设项目3个，自治区级本            科一流课程4门，自治区级课程思政示范课5门,自治区级虚拟教研室建设试点2个，广西高校重点实验室1个，自治区级实验教学中心2个，自治区级协同育人平台1个，自治区中小学生研学实践             教育基地、劳动教育实践基地各1个。建有新工科协同育人中心等100多个校内外实习实训基地，与多所广西中职学校共建职业教育实习基地。近年来，以加强创新创业教育为抓手，全面促进             人才培养供给侧和产业发展需求侧结构要素全方位融合，应用型人才培养质量广受认可，连续被评为广西普通高校毕业生就业创业工作突出单位，也是全区普通高校招生录取工作表现突出单位             。学校曾中标获得6项广西重大课题，并承担“推动广西经济高质量发展的重点方向和路径对策研究”等多项自治区党委、政府资政课题以及自治区工信厅、国家发展改革委、财政厅等部门          专项课题的研究工作，完成自治区两化融合项目“广西新能源汽车监测平台”的建设，凸显了服务广西的特色和优势。与广西西江开发投资集团高质量共建“广西船联网工程技术研究中心”等            多个校企深度合作项目，积极推进产教融合、科技创新成果转化工作，大力开展面向中小微企业的技术服务、咨询服务活动。学校还是广西干部教育培训高校基地、第七批自治区级专业技术人            员继续教育基地、自治区职业教育师资培养培训基地、广西知识产权培训基地、广西生态环境保护综合行政执法实训基地以及企业经营管理人员培训基地，培训了一大批高素质党政干部、“双          师型”职教师资和企业经营管理人才。面向未来，学校将坚守建校初心、牢记办学使命，紧扣“创新性驱动，特色化建设，内涵式提升，高质量发展”总要求，深化产教融合、校企合作，推进          工学结合、知行合一，努力将学校办成特色鲜明的高水平普通本科学校，在全面建设新时代壮美广西新征程中再谱新篇、再续华章。（学校办公室提供，数据信息统计截至2025年3月14日）")
elif page == "个人简历生成器":
    st.title("个人简历生成器")
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

elif page == "音乐播放器":
    st.title("音乐播放器")
    st.markdown("""
# 🎵 简易音乐播放器
使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制  
""")

    # 初始化状态变量
    if 'a' not in st.session_state:
        st.session_state['a'] = 0

    # 初始化按钮索引状态
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 图片数组
    image_arr = [{
            'url': 'https://p2.music.126.net/RvMT4b2CidXPzjmxtdpgVA==/109951170969007319.jpg?param=200y200',
            'title': '跳楼基',
            'artist': 'man',
            'time': '0:37'
        },{
            'url': 'https://p1.music.126.net/1rY2NfI9bM9QLMljUFxMVQ==/109951167589523192.jpg?param=200y200',
            'title': '鸡你太美',
            'artist': '坤坤',
            'time': '0:19'
        },{
            'url': 'https://p2.music.126.net/2Kg4bjgF2Ehab04wHlr06g==/109951169771888585.jpg?param=200y200',
            'title': '孤高曼波',
            'artist': 'man',
            'time': '0:23'
        }]

    # 音频数组
    audio_arr = [{
            'url': 'https://music.163.com/song/media/outer/url?id=2704552579.mp3',
        },{
            'url': 'https://music.163.com/song/media/outer/url?id=1949699283.mp3',
        },{
            'url': 'https://music.163.com/song/media/outer/url?id=2607065824.mp3',
      }]

    # 使用两列布局：一列显示图片，一列显示信息和控制按钮
    col1, col2 = st.columns([1, 2])

    with col1:
        # 显示当前图片
        st.image(image_arr[st.session_state['ind']]['url'], width=200)

    with col2:
        # 在右侧显示歌曲信息
        st.subheader(image_arr[st.session_state['ind']]['title'])
        st.write(f"歌手: {image_arr[st.session_state['ind']]['artist']}")
        st.write(f"时长: {image_arr[st.session_state['ind']]['time']}")
        
        # 显示当前音频
        st.audio(audio_arr[st.session_state['ind']]['url'])
        
        # 控制按钮移至此处
        c1, c2 = st.columns(2)
        
        with c1:
            st.button('上一首', on_click=lambda: st.session_state.update(ind=(st.session_state['ind'] - 1) % len(image_arr)), use_container_width=True)
        
        with c2:
            st.button('下一首', on_click=lambda: st.session_state.update(ind=(st.session_state['ind'] + 1) % len(image_arr)), use_container_width=True)

    # 使用说明部分
    st.selectbox('使用说明', ['请选择...', '基本操作', '高级功能'])

    st.title('音乐播放器功能说明:')
    text1 = """1. 播放/暂停：点击中间的播放/暂停按钮控制音乐播放 
2. 切歌功能：使用左右箭头按钮切换上一首/下一首 
3. 歌曲列表：从列表中选择任意歌曲播放"""
    st.write(text1)

    st.title('课堂练习任务:')
    text2 = """1. 实现基本的播放控制功能
2. 添加专辑封面显示
3. 实现切歌功能（上一首/下一首）
4. 显示歌曲基本信息（标题、歌手、时长)"""
    st.write(text2)

    st.title('拓展练习(可选):')
    text3 = """1. 添加随机播放功能
2. 实现音量控制
3. 添加播放进度显示"""
    st.write(text3)

elif page == "南宁美食数据":
    st.title("南宁美食数据")
    
    # 修正地图数据
    df = pd.DataFrame({
        "latitude": [22.833023, 22.849208, 22.814160, 22.818192, 22.830622],
        "longitude": [108.403855, 108.320469, 108.321510, 108.292848, 108.371383]
    })
    
    # 设置索引列的名称
    df.index.name = '序号'
    st.subheader('南宁地图')
    st.map(df)
    
    # 修正餐厅评分数据
    data = {
        '餐厅': ['复记老友粉', '好友缘', '星艺会尝不忘', '白妈螺蛳粉', '高峰柠檬鸭'],
        '评分': [4, 4.8, 4.2, 4.3, 4.4],
    }
    
    df = pd.DataFrame(data)
    st.header('⭐️餐厅评分')
    st.bar_chart(df, y='评分', x='餐厅')
    
    st.header('🔔不同类型餐厅价格')
    # 餐厅数据
    data = {
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "位置X": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "位置Y": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }
    
    # 创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3, 4, 5], name='序号')
    # 将新索引应用到数据框上
    df.index = index
    df_indexed = df.set_index('类型')
    st.line_chart(df_indexed['人均消费(元)'])
    
    # 定义数据,以便创建数据框
    data = {
        '时段': [11.0, 11.5, 12.5],
        '复记老友粉': [200, 150, 180],
        '星艺会尝不忘': [120, 160, 123],
        '高峰柠檬鸭': [110, 100, 160],
    }
    
    # 创建数据框
    df = pd.DataFrame(data)
    # 修改df，用月份列作为df的索引，替换原有的索引
    df.set_index('时段', inplace=True)
    
    st.subheader("⏰用餐高峰时段")
    # 通过y参数筛选显示1、2、3号门店的数据
    st.area_chart(df, y=['星艺会尝不忘', '高峰柠檬鸭', '复记老友粉'])
    
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
    st.header("当前拥挤程度")
    st.markdown('###### 94%拥挤')
    st.progress(94)
    
    st.title("🎲今日午餐推荐")
    if st.button('帮我选午餐'):
        st.write('`*星怡会尝不忘*`')
        st.image("https://tse2-mm.cn.bing.net/th/id/OIP-C.i982znXoIr1SAPGvh_VfVwHaFd?w=239&h=180&c=7&r=0&o=5&pid=1.7")

elif page == "数字档案":
    st.title("数字档案")
    
    # 主标题
    st.title("🕶️ 学生 小陆 - 数字档案")

    # 基础信息章节
    st.header("🔑 基础信息")
    st.text("学生ID: NEO-2023-001")
    st.markdown("**注册时间**: `2023-10-01 08:30:17` | **精神状态**: ✅ 正常")
    st.markdown("**当前教室**: `实训楼301` | **安全等级**: `绝密`")

    # 技能矩阵章节
    st.header("📊 技能矩阵")
    col1, col2, col3 = st.columns(3)
    col1.metric("C语言", "95%", "2%", help="近期训练提升") 
    col2.metric("Python", "87%", "-1%")
    col3.metric("Java", "68%", "-10%", help="用则进废则退")

    # 进度条展示
    st.subheader("Streamlit课程进度")
    st.progress(28, text="Streamlit课程进度")

    # 任务日志章节
    st.header("📝 任务日志")
    mission_data = {
        "日期": ["2023-10-01", "2023-10-05", "2023-10-12"],
        "任务": ["学生数字档案", "课程管理系统", "数据图表展示"],
        "状态": ["✅ 完成", "🕒 进行中", "❌ 未完成"],
        "难度": ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆"]
    }
    mission_df = pd.DataFrame(mission_data)
    st.table(mission_df.style.applymap(
        lambda x: 'color: #0f0' if x == "✅ 完成" else 'color: #ff0')
    )

    # 代码块展示
    st.subheader("🔐 最新代码成果")
    st.code('''def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()''', language='python')

    # 动态信息流
    st.write("---")
    st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")
    st.write("`>> TARGET:` 课程管理系统")
    st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 终端效果
    st.markdown("""
系统状态: 在线
连接状态: 已加密
""")
