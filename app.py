import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# ========== 页面配置 ==========
st.set_page_config(
    page_title="石河子大学食堂管理系统",
    page_icon="🍜",
    layout="wide"
)

# ========== 模拟数据库（内存数据，无需安装MySQL） ==========
@st.cache_data
def load_data():
    # 学生表
    students = pd.DataFrame({
        'Sno': ['20241008167', '20241008224', '20241008001'],
        'SName': ['段鸿智', '杨博文', '张三'],
        'SKey': ['123456', '123456', '123456'],
        'SSex': ['男', '男', '女'],
        'SAge': [20, 20, 19],
        'SBalance': [100.00, 50.00, 200.00],
        'SDept': ['网安', '网安', '计算机']
    })

    # 食堂表
    canteens = pd.DataFrame({
        'Cno': ['001', '002', '003', '004', '005', '006', '007', '008'],
        'CName': ['中区食堂', '北区食堂', '南区食堂', '东区食堂', '西区食堂', '研究生食堂', '教工食堂', '清真食堂'],
        'CAddress': ['中区', '北区', '南区', '东区', '西区', '研究生区', '教工区', '清真区'],
        'CManager': ['王经理', '李经理', '张经理', '刘经理', '陈经理', '赵经理', '孙经理', '马经理'],
        'CPhone': ['13800138001', '13800138002', '13800138003', '13800138004', '13800138005', '13800138006', '13800138007', '13800138008']
    })

    # 窗口表
    windows = pd.DataFrame({
        'Wno': ['00101', '00102', '00201', '00301', '00401', '00501', '00601', '00701', '00801'],
        'WName': ['川菜窗口', '面食窗口', '快餐窗口', '小炒窗口', '自助餐', '盖饭窗口', '精品菜', '教职工专窗', '清真拉面'],
        'Cno': ['001', '001', '002', '003', '004', '005', '006', '007', '008'],
        'WManager': ['赵师傅', '钱师傅', '孙师傅', '周师傅', '吴师傅', '郑师傅', '王师傅', '冯师傅', '马师傅'],
        'WCategory': ['川菜', '面食', '快餐', '小炒', '自助', '盖饭', '精品', '教职工', '清真'],
        'WTime': '6:30-22:00'
    })

    # 菜品表
    dishes = pd.DataFrame({
        'Fno': ['000001', '000002', '000003', '000004', '000005', '000006', '000007', '000008', '000009', '000010'],
        'FName': ['宫保鸡丁', '麻婆豆腐', '牛肉面', '盖浇饭', '大盘鸡', '酸奶', '凉拌黄瓜', '紫菜蛋花汤', '可乐', '烤包子'],
        'FType': ['2', '2', '1', '1', '2', '5', '3', '4', '5', '6'],
        'FPrice': [12.00, 8.00, 10.00, 15.00, 28.00, 5.00, 6.00, 3.00, 4.00, 8.00],
        'FTaste': ['微辣', '麻辣', '清淡', '咸鲜', '中辣', '酸甜', '清爽', '清淡', '甜', '香'],
        'FNutrition': ['蛋白质丰富', '植物蛋白', '碳水+蛋白质', '均衡营养', '高热量', '益生菌', '维生素', '蛋白质', '糖分', '碳水'],
        'Wno': ['00101', '00101', '00102', '00201', '00301', '00201', '00101', '00201', '00301', '00801'],
        'FStatus': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    })

    # 订单表
    orders = pd.DataFrame({
        'Ono': ['202606200001', '202606200002', '202606200003', '202606200004', '202606200005'],
        'Userno': ['20241008167', '20241008224', '20241008001', '20241008167', '20241008224'],
        'OStatus': ['4', '4', '1', '4', '2'],
        'OTime': [datetime.now()-timedelta(days=5), datetime.now()-timedelta(days=3), datetime.now()-timedelta(days=1), datetime.now()-timedelta(days=2), datetime.now()-timedelta(hours=2)],
        'OCode': ['123456', '234567', '345678', '456789', '567890'],
        'OTotal': [20.00, 15.00, 28.00, 12.00, 23.00]
    })

    # 订单明细表
    order_details = pd.DataFrame({
        'Ono': ['202606200001', '202606200001', '202606200002', '202606200003', '202606200004', '202606200005', '202606200005'],
        'Fno': ['000001', '000002', '000004', '000005', '000001', '000003', '000007'],
        'ODQuantity': [1, 1, 1, 1, 1, 1, 1],
        'ODSubtotal': [12.00, 8.00, 15.00, 28.00, 12.00, 10.00, 6.00]
    })

    # 库存表
    inventory = pd.DataFrame({
        'Ino': ['000001', '000002', '000003', '000004', '000005'],
        'IName': ['大米', '食用油', '鸡肉', '面粉', '青菜'],
        'IQuantity': [50, 20, 30, 80, 15],
        'IUnit': ['kg', 'L', 'kg', 'kg', 'kg'],
        'IThreshold': [100, 30, 50, 40, 20],
        'Cno': ['001', '001', '001', '001', '001'],
        'ITime': datetime.now()
    })

    # 评价表
    reviews = pd.DataFrame({
        'Rno': ['000001', '000002', '000003'],
        'Ono': ['202606200001', '202606200002', '202606200004'],
        'RScore': [5, 4, 5],
        'RContent': ['味道很好，分量足', '出餐速度快', '宫保鸡丁很正宗'],
        'RTime': [datetime.now()-timedelta(days=4), datetime.now()-timedelta(days=2), datetime.now()-timedelta(days=1)]
    })

    return students, canteens, windows, dishes, orders, order_details, inventory, reviews

# 加载数据
students, canteens, windows, dishes, orders, order_details, inventory, reviews = load_data()

# 类型映射
TYPE_MAP = {'1': '主食', '2': '热菜', '3': '凉菜', '4': '汤品', '5': '饮品', '6': '小吃'}
STATUS_MAP = {'0': '待支付', '1': '已支付', '2': '制作中', '3': '待取餐', '4': '已完成', '5': '已取消'}
CANTEEN_MAP = dict(zip(canteens['Cno'], canteens['CName']))

# ========== 登录状态 ==========
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.session_state.cart = []

# ========== 登录页面 ==========
def login_page():
    st.title("🍜 石河子大学食堂管理系统")
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("用户登录")
        username = st.text_input("账号", placeholder="学号/管理员号")
        password = st.text_input("密码", type="password", placeholder="6位密码")
        role = st.selectbox("身份", ["学生", "食堂管理员", "后勤管理员"])

        if st.button("登录", use_container_width=True):
            if role == "学生" and username in students['Sno'].values:
                user = students[students['Sno'] == username].iloc[0]
                if password == user['SKey']:
                    st.session_state.logged_in = True
                    st.session_state.user = user.to_dict()
                    st.session_state.role = "student"
                    st.rerun()
                else:
                    st.error("密码错误")
            elif role == "食堂管理员" and username.startswith('3'):
                st.session_state.logged_in = True
                st.session_state.user = {'Ano': username, 'AName': '管理员', 'Cno': '001'}
                st.session_state.role = "admin"
                st.rerun()
            elif role == "后勤管理员" and username.startswith('9'):
                st.session_state.logged_in = True
                st.session_state.user = {'Hno': username, 'HName': '后勤'}
                st.session_state.role = "logistics"
                st.rerun()
            else:
                st.error("账号或密码错误")

# ========== 学生端 ==========
def student_page():
    st.sidebar.title(f"👤 {st.session_state.user['SName']}")
    st.sidebar.write(f"学号: {st.session_state.user['Sno']}")
    st.sidebar.write(f"学院: {st.session_state.user['SDept']}")
    st.sidebar.write(f"余额: ¥{st.session_state.user['SBalance']:.2f}")
    st.sidebar.markdown("---")

    menu = st.sidebar.radio("功能菜单", ["🏠 首页", "🍽️ 在线点餐", "📋 我的订单", "💰 消费查询", "⭐ 评价"])

    if menu == "🏠 首页":
        st.header("🏠 欢迎使用石河子大学食堂管理系统")
        st.markdown("---")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("今日营业食堂", f"{len(canteens)} 个")
        with col2:
            st.metric("上架菜品", f"{len(dishes)} 道")
        with col3:
            my_orders = orders[orders['Userno'] == st.session_state.user['Sno']]
            st.metric("我的订单", f"{len(my_orders)} 笔")

        st.subheader("🔥 热门菜品推荐")
        hot_dishes = dishes.sample(n=min(3, len(dishes)))
        cols = st.columns(3)
        for idx, (_, dish) in enumerate(hot_dishes.iterrows()):
            with cols[idx]:
                with st.container(border=True):
                    st.markdown(f"**{dish['FName']}**")
                    st.caption(f"{TYPE_MAP.get(dish['FType'], '未知')} | {dish['FTaste']}")
                    st.markdown(f"¥**{dish['FPrice']:.2f}**")

    elif menu == "🍽️ 在线点餐":
        st.header("🍽️ 在线点餐")

        col1, col2 = st.columns(2)
        with col1:
            canteen_sel = st.selectbox("选择食堂", canteens['CName'].tolist())
        with col2:
            type_sel = st.selectbox("菜品类别", ["全部"] + list(TYPE_MAP.values()))

        cno = canteens[canteens['CName'] == canteen_sel]['Cno'].values[0]
        canteen_windows = windows[windows['Cno'] == cno]['Wno'].tolist()
        available_dishes = dishes[(dishes['Wno'].isin(canteen_windows)) & (dishes['FStatus'] == '1')]

        if type_sel != "全部":
            type_code = [k for k, v in TYPE_MAP.items() if v == type_sel][0]
            available_dishes = available_dishes[available_dishes['FType'] == type_code]

        st.write(f"共找到 **{len(available_dishes)}** 道菜品")

        cols = st.columns(3)
        for idx, (_, dish) in enumerate(available_dishes.iterrows()):
            with cols[idx % 3]:
                with st.container(border=True):
                    st.markdown(f"### {dish['FName']}")
                    st.caption(f"类别: {TYPE_MAP.get(dish['FType'], '未知')}")
                    st.write(f"🌶️ 口味: {dish['FTaste']}")
                    st.write(f"🥗 营养: {dish['FNutrition']}")
                    st.markdown(f"**¥{dish['FPrice']:.2f}**")
                    qty = st.number_input("数量", min_value=1, max_value=10, value=1, key=f"qty_{dish['Fno']}")
                    if st.button("加入购物车", key=f"add_{dish['Fno']}", use_container_width=True):
                        st.session_state.cart.append({
                            'Fno': dish['Fno'],
                            'FName': dish['FName'],
                            'FPrice': dish['FPrice'],
                            'Qty': qty
                        })
                        st.success(f"已添加 {dish['FName']} x{qty}")

        # 购物车
        if st.session_state.cart:
            st.markdown("---")
            st.subheader(f"🛒 购物车 ({len(st.session_state.cart)} 项)")
            cart_df = pd.DataFrame(st.session_state.cart)
            cart_df['小计'] = cart_df['FPrice'] * cart_df['Qty']
            st.dataframe(cart_df[['FName', 'FPrice', 'Qty', '小计']], use_container_width=True, hide_index=True)
            total = cart_df['小计'].sum()
            st.markdown(f"**合计: ¥{total:.2f}**")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("清空购物车", use_container_width=True):
                    st.session_state.cart = []
                    st.rerun()
            with col2:
                if st.button("立即下单", type="primary", use_container_width=True):
                    st.success("订单提交成功！取餐码: " + str(random.randint(100000, 999999)))
                    st.session_state.cart = []

    elif menu == "📋 我的订单":
        st.header("📋 我的订单")
        my_orders = orders[orders['Userno'] == st.session_state.user['Sno']].copy()
        if my_orders.empty:
            st.info("暂无订单")
        else:
            my_orders['状态'] = my_orders['OStatus'].map(STATUS_MAP)
            my_orders['下单时间'] = pd.to_datetime(my_orders['OTime']).dt.strftime('%Y-%m-%d %H:%M')
            display_df = my_orders[['Ono', '状态', '下单时间', 'OTotal']].rename(columns={
                'Ono': '订单号', 'OTotal': '金额(元)'
            })
            st.dataframe(display_df, use_container_width=True, hide_index=True)

    elif menu == "💰 消费查询":
        st.header("💰 消费查询")
        my_completed = orders[(orders['Userno'] == st.session_state.user['Sno']) & (orders['OStatus'] == '4')]

        col1, col2 = st.columns(2)
        with col1:
            total = my_completed['OTotal'].sum()
            st.metric("累计消费", f"¥{total:.2f}")
        with col2:
            st.metric("完成订单", f"{len(my_completed)} 笔")

        if not my_completed.empty:
            st.subheader("📈 消费趋势")
            my_completed['月份'] = pd.to_datetime(my_completed['OTime']).dt.strftime('%Y-%m')
            monthly = my_completed.groupby('月份')['OTotal'].sum()
            st.bar_chart(monthly)

            st.subheader("📋 消费明细")
            detail = my_completed[['Ono', 'OTime', 'OTotal']].copy()
            detail['OTime'] = pd.to_datetime(detail['OTime']).dt.strftime('%Y-%m-%d')
            st.dataframe(detail.rename(columns={'Ono': '订单号', 'OTime': '日期', 'OTotal': '金额'}), 
                        use_container_width=True, hide_index=True)
        else:
            st.info("暂无消费记录")

    elif menu == "⭐ 评价":
        st.header("⭐ 订单评价")
        my_completed = orders[(orders['Userno'] == st.session_state.user['Sno']) & (orders['OStatus'] == '4')]
        rated_onos = reviews['Ono'].tolist()
        unrated = my_completed[~my_completed['Ono'].isin(rated_onos)]

        if unrated.empty:
            st.info("暂无待评价订单")
        else:
            for _, order in unrated.iterrows():
                with st.container(border=True):
                    st.write(f"**订单号:** {order['Ono']}")
                    st.write(f"**消费金额:** ¥{order['OTotal']:.2f}")
                    score = st.slider("评分", 1, 5, 5, key=f"score_{order['Ono']}")
                    content = st.text_area("评价内容", placeholder="请输入您的评价...", key=f"content_{order['Ono']}")
                    if st.button("提交评价", key=f"submit_{order['Ono']}"):
                        st.success("评价提交成功！")

# ========== 食堂管理员端 ==========
def admin_page():
    st.sidebar.title("👨‍🍳 食堂管理员端")
    st.sidebar.write(f"管理员: {st.session_state.user['AName']}")
    st.sidebar.write(f"管理食堂: {CANTEEN_MAP.get(st.session_state.user['Cno'], '未知')}")
    st.sidebar.markdown("---")

    menu = st.sidebar.radio("功能菜单", ["📊 数据概览", "🍳 菜品管理", "🏪 窗口管理", "📦 库存管理", "📋 订单处理", "⭐ 评价查看"])
    admin_cno = st.session_state.user['Cno']
    admin_windows = windows[windows['Cno'] == admin_cno]['Wno'].tolist()

    if menu == "📊 数据概览":
        st.header("📊 数据概览")
        admin_dishes = dishes[dishes['Wno'].isin(admin_windows)]
        admin_inventory = inventory[inventory['Cno'] == admin_cno]

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("窗口数", len(admin_windows))
        with col2:
            st.metric("菜品数", len(admin_dishes))
        with col3:
            low_stock = len(admin_inventory[admin_inventory['IQuantity'] < admin_inventory['IThreshold']])
            st.metric("库存预警", f"{low_stock} 项", delta="需补货" if low_stock > 0 else None, delta_color="inverse")
        with col4:
            admin_orders = order_details[order_details['Fno'].isin(admin_dishes['Fno'].tolist())]
            revenue = admin_orders['ODSubtotal'].sum()
            st.metric("累计营收", f"¥{revenue:.2f}")

    elif menu == "🍳 菜品管理":
        st.header("🍳 菜品管理")

        tab1, tab2 = st.tabs(["📋 菜品列表", "➕ 上架新菜品"])

        with tab1:
            admin_dishes = dishes[dishes['Wno'].isin(admin_windows)].copy()
            admin_dishes['类别'] = admin_dishes['FType'].map(TYPE_MAP)
            admin_dishes['状态'] = admin_dishes['FStatus'].apply(lambda x: '✅ 上架中' if x == '1' else '❌ 已下架')

            st.dataframe(admin_dishes[['Fno', 'FName', '类别', 'FPrice', 'FTaste', '状态']].rename(columns={
                'Fno': '菜品号', 'FName': '菜品名', 'FPrice': '价格', 'FTaste': '口味'
            }), use_container_width=True, hide_index=True)

            st.subheader("快速操作")
            for _, dish in admin_dishes.iterrows():
                col1, col2, col3 = st.columns([3, 2, 2])
                with col1:
                    st.write(f"**{dish['FName']}**")
                with col2:
                    st.write(f"{dish['状态']}")
                with col3:
                    if dish['FStatus'] == '1':
                        if st.button("下架", key=f"down_{dish['Fno']}"):
                            st.success(f"{dish['FName']} 已下架")
                    else:
                        if st.button("上架", key=f"up_{dish['Fno']}"):
                            st.success(f"{dish['FName']} 已上架")

        with tab2:
            with st.form("new_dish"):
                st.subheader("上架新菜品")
                d_name = st.text_input("菜品名称")
                d_type = st.selectbox("菜品类别", list(TYPE_MAP.values()))
                d_price = st.number_input("价格(元)", min_value=0.1, value=10.0)
                d_taste = st.text_input("口味标签", placeholder="如：微辣、清淡")
                d_nutrition = st.text_input("营养成分")
                d_window = st.selectbox("所属窗口", windows[windows['Cno'] == admin_cno]['WName'].tolist())
                submitted = st.form_submit_button("确认上架")
                if submitted and d_name:
                    st.success(f"菜品「{d_name}」上架成功！")

    elif menu == "🏪 窗口管理":
        st.header("🏪 窗口管理")
        admin_win_df = windows[windows['Cno'] == admin_cno].copy()
        st.dataframe(admin_win_df[['Wno', 'WName', 'WManager', 'WCategory', 'WTime']].rename(columns={
            'Wno': '窗口号', 'WName': '窗口名', 'WManager': '负责人', 'WCategory': '主营品类', 'WTime': '营业时间'
        }), use_container_width=True, hide_index=True)

        with st.expander("➕ 新增窗口"):
            with st.form("new_window"):
                w_name = st.text_input("窗口名称")
                w_manager = st.text_input("负责人")
                w_category = st.text_input("主营品类")
                w_time = st.text_input("营业时间", value="6:30-22:00")
                if st.form_submit_button("新增") and w_name:
                    st.success(f"窗口「{w_name}」新增成功！")

    elif menu == "📦 库存管理":
        st.header("📦 库存管理")
        admin_inventory = inventory[inventory['Cno'] == admin_cno].copy()
        admin_inventory['状态'] = admin_inventory.apply(
            lambda x: '⚠️ 预警' if x['IQuantity'] < x['IThreshold'] else '✅ 正常', axis=1
        )

        st.dataframe(admin_inventory[['Ino', 'IName', 'IQuantity', 'IUnit', 'IThreshold', '状态']].rename(columns={
            'Ino': '库存号', 'IName': '原材料', 'IQuantity': '当前数量', 'IUnit': '单位', 'IThreshold': '预警阈值'
        }), use_container_width=True, hide_index=True)

        warnings = admin_inventory[admin_inventory['IQuantity'] < admin_inventory['IThreshold']]
        if not warnings.empty:
            st.error(f"🚨 有 {len(warnings)} 项库存低于预警阈值，请及时补货！")
            for _, w in warnings.iterrows():
                st.warning(f"{w['IName']}: 当前 {w['IQuantity']}{w['IUnit']}，预警线 {w['IThreshold']}{w['IUnit']}")

        with st.expander("➕ 添加库存"):
            with st.form("add_inventory"):
                i_name = st.text_input("原材料名称")
                i_qty = st.number_input("数量", min_value=0, value=100)
                i_unit = st.text_input("单位", value="kg")
                i_threshold = st.number_input("预警阈值", min_value=1, value=50)
                if st.form_submit_button("添加") and i_name:
                    st.success(f"原材料「{i_name}」入库成功！")
                                insert into inventory (ingredent_id.stuct_num)
                valuse
                on duplicate key update stock_num=stock_num+ 
    elif menu == "📋 订单处理":
        st.header("📋 订单处理")
        admin_dishes_fno = dishes[dishes['Wno'].isin(admin_windows)]['Fno'].tolist()
        admin_order_details = order_details[order_details['Fno'].isin(admin_dishes_fno)]
        admin_onos = admin_order_details['Ono'].unique().tolist()
        admin_orders = orders[orders['Ono'].isin(admin_onos)].copy()
        admin_orders['状态'] = admin_orders['OStatus'].map(STATUS_MAP)

        if admin_orders.empty:
            st.info("暂无订单")
        else:
            st.dataframe(admin_orders[['Ono', 'Userno', '状态', 'OTime', 'OTotal']].rename(columns={
                'Ono': '订单号', 'Userno': '用户号', 'OTime': '下单时间', 'OTotal': '金额'
            }), use_container_width=True, hide_index=True)

    elif menu == "⭐ 评价查看":
        st.header("⭐ 评价查看")
        admin_dishes_fno = dishes[dishes['Wno'].isin(admin_windows)]['Fno'].tolist()
        admin_order_details = order_details[order_details['Fno'].isin(admin_dishes_fno)]
        admin_onos = admin_order_details['Ono'].unique().tolist()
        admin_reviews = reviews[reviews['Ono'].isin(admin_onos)].copy()

        if admin_reviews.empty:
            st.info("暂无评价")
        else:
            avg_score = admin_reviews['RScore'].mean()
            st.metric("平均评分", f"{avg_score:.1f} / 5.0")

            for _, rev in admin_reviews.iterrows():
                with st.container(border=True):
                    stars = "⭐" * rev['RScore']
                    st.markdown(f"{stars} **{rev['RScore']}分**")
                    st.write(rev['RContent'])
                    st.caption(f"{rev['RTime'].strftime('%Y-%m-%d %H:%M')}")

# ========== 后勤端 ==========
def logistics_page():
    st.sidebar.title("🏢 后勤管理端")
    st.sidebar.markdown("---")

    menu = st.sidebar.radio("功能菜单", ["📊 全局概览", "💰 财务报表", "🏪 食堂营收统计", "🍳 菜品评价汇总", "👥 用户管理"])

    if menu == "📊 全局概览":
        st.header("📊 全局数据概览")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("注册学生", len(students))
        with col2:
            st.metric("营业食堂", len(canteens))
        with col3:
            st.metric("上架菜品", len(dishes))
        with col4:
            completed = len(orders[orders['OStatus'] == '4'])
            st.metric("已完成订单", completed)

        st.subheader("📈 近7天订单趋势")
        orders['日期'] = pd.to_datetime(orders['OTime']).dt.date
        daily = orders.groupby('日期').size()
        st.line_chart(daily)

    elif menu == "💰 财务报表":
        st.header("💰 财务报表")

        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("开始日期", datetime.now() - timedelta(days=30))
        with col2:
            end_date = st.date_input("结束日期", datetime.now())

        completed_orders = orders[orders['OStatus'] == '4']
        total_revenue = completed_orders['OTotal'].sum()
        total_orders = len(completed_orders)
        avg_price = total_revenue / total_orders if total_orders > 0 else 0

        col1, col2, col3 = st.columns(3)
        col1.metric("总营业额", f"¥{total_revenue:.2f}")
        col2.metric("订单总量", f"{total_orders} 笔")
        col3.metric("客单价", f"¥{avg_price:.2f}")

        st.subheader("📊 营收趋势")
        completed_orders['月份'] = pd.to_datetime(completed_orders['OTime']).dt.strftime('%Y-%m')
        monthly = completed_orders.groupby('月份')['OTotal'].sum()
        st.bar_chart(monthly)

    elif menu == "🏪 食堂营收统计":
        st.header("🏪 各食堂营收统计")

        canteen_revenue = []
        for _, c in canteens.iterrows():
            c_windows = windows[windows['Cno'] == c['Cno']]['Wno'].tolist()
            c_dishes = dishes[dishes['Wno'].isin(c_windows)]['Fno'].tolist()
            c_order_details = order_details[order_details['Fno'].isin(c_dishes)]
            revenue = c_order_details['ODSubtotal'].sum()
            order_count = len(c_order_details)
            canteen_revenue.append({
                '食堂': c['CName'], 
                '营业额': revenue, 
                '订单量': order_count,
                '客单价': revenue / order_count if order_count > 0 else 0
            })

        revenue_df = pd.DataFrame(canteen_revenue).sort_values('营业额', ascending=False)
        st.dataframe(revenue_df, use_container_width=True, hide_index=True)

        st.subheader("🏆 营收排名")
        st.bar_chart(revenue_df.set_index('食堂')['营业额'])

    elif menu == "🍳 菜品评价汇总":
        st.header("🍳 菜品评价汇总")

        dish_reviews = []
        for _, d in dishes.iterrows():
            d_orders = order_details[order_details['Fno'] == d['Fno']]['Ono'].tolist()
            d_reviews = reviews[reviews['Ono'].isin(d_orders)]
            if not d_reviews.empty:
                dish_reviews.append({
                    '菜品': d['FName'],
                    '评分': d_reviews['RScore'].mean(),
                    '评价数': len(d_reviews)
                })

        if dish_reviews:
            review_df = pd.DataFrame(dish_reviews).sort_values('评分', ascending=False)
            st.dataframe(review_df, use_container_width=True, hide_index=True)
        else:
            st.info("暂无评价数据")

    elif menu == "👥 用户管理":
        st.header("👥 用户管理")
        tab1, tab2 = st.tabs(["学生列表", "管理员列表"])
        with tab1:
            st.dataframe(students[['Sno', 'SName', 'SSex', 'SAge', 'SBalance', 'SDept']].rename(columns={
                'Sno': '学号', 'SName': '姓名', 'SSex': '性别', 'SAge': '年龄', 'SBalance': '余额', 'SDept': '学院'
            }), use_container_width=True, hide_index=True)

# ========== 主程序 ==========
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        col1, col2 = st.columns([8, 1])
        with col1:
            st.caption("石河子大学食堂管理信息系统 | 数据库系统原理课程设计")
        with col2:
            if st.button("🚪 退出"):
                st.session_state.logged_in = False
                st.session_state.user = None
                st.session_state.role = None
                st.session_state.cart = []
                st.rerun()

        if st.session_state.role == "student":
            student_page()
        elif st.session_state.role == "admin":
            admin_page()
        elif st.session_state.role == "logistics":
            logistics_page()

if __name__ == "__main__":
    main()
