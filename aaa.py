import streamlit as st

# 设置页面配置
st.set_page_config(page_title="简易音乐播放器", layout="centered")

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
option=st.selectbox('1','使用说明')

st.title('音乐播放器功能说明:')

text1="""1. 播放/暂停：点击中间的播放/暂停按钮控制音乐播放 
2. 切歌功能：使用左右箭头按钮切换上一首/下一首 
3. 歌曲列表：从列表中选择任意歌曲播放
         """
st.write(text1)

st.title('课堂练习任务:')

text2="""1. 实现基本的播放控制功能
2. 添加专辑封面显示
3. 实现切歌功能（上一首/下一首）
4. 显示歌曲基本信息（标题、歌手、时长)
         """

st.write(text2)

st.title('拓展练习(可选):')
text3="""1. 添加随机播放功能
2. 实现音量控制
3. 添加播放进度显示
         """
st.write(text3)
