import streamlit as st
import datetime

# 设置页面标题和图标
st.set_page_config(
    page_title="生日快乐！",
    page_icon="🎂",
    layout="centered"
)

# 隐藏默认的Streamlit菜单和页脚
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# 应用标题
st.title("🎉 生日快乐！ 🎉")

# 获取寿星名字
name = st.text_input("请输入寿星名字：", "亲爱的冯露云宝宝")

# 生日日期选择
birthday = st.date_input("选择生日日期：", datetime.date.today())

# 检查是否是生日当天
today = datetime.date.today()
is_birthday = (birthday.month == today.month) and (birthday.day == today.day)

# 显示不同的祝福语
if is_birthday:
    st.balloons()
    st.success(f"🎂 今天是{name}的生日！祝你生日快乐！ 🎈")
else:
    st.info(f"🎁 提前祝{name}生日快乐！美好的祝福送给你！")

# 添加祝福语
st.header(f"给{name}的祝福")
col1, col2 = st.columns(2)

with col1:
    st.write("""
    🌟 愿你所有的梦想都能实现
    🌈 愿你每一天都充满欢笑
    💖 愿你被爱包围
    """)

with col2:
    st.write("""
    🎈 愿你的生活像彩虹一样绚丽
    🍀 愿好运常伴你左右
    🥂 为你的幸福干杯
    """)

# 添加生日蛋糕图片
st.header("🎂 心目中最漂亮的女孩")
try:
    # 使用公开可用的生日蛋糕图片链接
    cake_img_url = "https://raw.githubusercontent.com/Cccw110/my-image/main/6e87879285525680b2440b5494a13c1.jpg"
    st.image(cake_img_url, caption="特制生日蛋糕", use_column_width=True)
except:
    st.image("https://raw.githubusercontent.com/Cccw110/my-image/main/6e87879285525680b2440b5494a13c1.jpg", 
             caption="虚拟生日蛋糕", use_column_width=True)

# 添加生日音乐
st.header("🎵 生日歌")
try:
    # 使用公开可用的音频链接
    st.audio("https://music.163.com/song/media/outer/url?id=1396028550", format="audio/mp3")
except:
    st.warning("音乐无法加载，点击下面的链接收听生日快乐歌")
    st.markdown("[生日快乐歌 (YouTube)](https://music.163.com/song/media/outer/url?id=1396028550)")

# 互动元素 - 生日许愿
st.header("✨ 许个生日愿望")
wish = st.text_area(f"{name}，在这里写下你的生日愿望：", 
                   "我希望...")
if st.button("放飞愿望气球"):
    st.balloons()
    st.success("🎈 你的愿望已经飞向天空，一定会实现的！")

# 生日倒计时
if not is_birthday:
    next_birthday = datetime.date(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
    
    delta = next_birthday - today
    st.header("⏳ 生日倒计时")
    st.write(f"距离{name}的下一个生日还有 {delta.days} 天")

# 页脚
st.markdown("---")
st.markdown("❤️ 用爱制作的生日贺礼 ❤️")

# 添加一些特效
if st.button("点击获取特别祝福"):
    st.snow()
    st.write(f"🌟 {name}，你是最棒的！愿这一年带给你无尽的快乐和成功！")    