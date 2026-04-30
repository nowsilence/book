import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===================== 1. 配置 Tushare Token =====================
# 把这里换成你自己的 Token！
ts.set_token("c1ce41af3e64f3ace28f2dff2d61325445b7d373f38a2f6772c21ca5")
pro = ts.pro_api()

# ===================== 2. 获取 A股数据 =====================
start_date = "20250415"
code = "600519.SH"  # 贵州茅台
# 后复权 规则：保住上市第一天原价不变，把后面所有价格往上抬高
# 前复权 保住现在价格不变，把历史所有价格往下压低
# daily 不复权（除权
df = pro.daily(ts_code=code, start_date=start_date)
# 前复权 需要2000积分才能使用
# df = pro.pro_bar(
#     ts_code=code, 
#     start_date="20250101", 
#     adj="qfq"   # qfq = 前复权！
# )



# 整理数据（关键：时间正序 + 设索引）
df = df.sort_values("trade_date").reset_index(drop=True)

# 3. 获取复权因子（关键！）
# adj_factor = pro.adj_factor(ts_code=code, start_date="20250101")
# 4. 合并复权因子
# df = pd.merge(df, adj_factor, on="trade_date", how="left")
# 获取的是后复权的因子 前复权价 = 当日收盘价 × 当日后复权因子 ÷ 最新后复权因子
adj = pro.adj_factor(ts_code=code, start_date=start_date)

# 两张表合并到一起 按哪一列合并？ → 按日期对齐 how="left" 以左边的表（日线）为准！
df = pd.merge(df, adj, on="trade_date", how="left")
df = df.sort_values("trade_date").reset_index(drop=True)

# ====================== 前复权收盘价======================
df["close_qfq"] = df["close"] * df["adj_factor"] / df["adj_factor"].iloc[-1]

df["trade_date"] = pd.to_datetime(df["trade_date"])
df.set_index("trade_date", inplace=True)
df.rename(columns={"close_qfq": "price"}, inplace=True)

# ===================== 3. 双均线指标 =====================
df["ma_short"] = df["price"].rolling(window=5, min_periods=5).mean()   # 5日均线
df["ma_long"] = df["price"].rolling(window=10, min_periods=10).mean()   # 100日均线

# 删除任何一列有空值的行
# inplace=True：直接修改原表，不创建新表
df.dropna(inplace=True)

# ===================== 4. 交易信号 =====================
'''
双均线金叉死叉
均线：对于每一个交易日，都可以计算出前 N 天的移动平均值，然后把这些平均值连起来，
     成为一条线，就叫做 N 日移动平均线。移动平均线常用线有 5 日、10 日、30 日、60 日、120 日的指标。
5 日和 10 日的是短线操作参照指标，称作日均线指标；
30 日和 60 日的是中期均线指标，称作季均线指标；
120 日和 240 日的是长期均线指标，称作年均线指标。
金叉：短期均线上穿长期均线，买入信号。
死叉：短期均线下穿长期均线，卖出信号。
交易策略：金叉买入，死叉卖出。

低位金叉大胆买，高位金叉不要睬
低位死叉别恐慌，高位死叉快离场
短均跟着长均走，顺势操作不用愁
震荡交叉别乱动，趋势明朗再出手

短期均线 > 长期均线 → 上涨趋势 → 持有股票 = 1
短期均线 < 长期均线 → 下跌趋势 → 空仓不买 = 0

signal 1 表示持有 0 表示空仓
'''
df["signal"] = np.where(df["ma_short"] > df["ma_long"], 1, 0)
'''
diff = 后一天 - 前一天
order = 1 → 买入
order = -1 → 卖出
order = 0 → 不操作（持仓或者空仓）

用来表示买入卖出动作的
'''
df["order"] = df["signal"].diff()

# ===================== 5. 策略回测 =====================
df["position"] = df["signal"]
'''
df["price"].pct_change() 
股票涨跌幅: 涨2% → 0.02, 跌1% → -0.01

昨天有没有持仓
shift(1) 取下一行，即前一天的数据

昨天我有没有股票？shift(1)
今天股票涨跌多少？pct_change()
两者相乘 = 我今天赚或者亏多少钱
返回的是Series对象
'''
df["strategy_return"] = df["position"].shift(1) * df["price"].pct_change()
df["base_return"] = df["price"].pct_change()

# 累计收益
# cumprod累积积(cumulative product) 从第一天开始，一路乘到今天
# df["strategy_cum"]存的是一个series
df["strategy_cum"] = (1 + df["strategy_return"]).cumprod()
df["base_cum"] = (1 + df["base_return"]).cumprod()

# ===================== 6. 输出结果 =====================
'''
第一个参数必须是索引的值，若只有一个参数，则取所有列
df.loc[行标签, 列标签]

# 取单行
df.loc["2025-01-01"]

# 取多行（一段日期）
df.loc["2025-01-01":"2025-02-01"]

# 取某日期 + 某一列
df.loc["2025-01-01", "price"]

# 取多行多列
df.loc["2025-01-01":"2025-02-01", ["price","ma_short"]]

# 单行
df.iloc[5]

# 多行 第0行~第9行
df.iloc[0:10]

# 倒数最后一行（你代码用的）
df.iloc[-1]

# 第几行，第几列
df.iloc[5, 2]
'''
print("="*50)
print(f"【{code} A股双均线策略回测】")
print(f"策略累计收益率：{(df['strategy_cum'].iloc[-1] - 1)*100:.2f}%")
print(f"持有不动收益率：{(df['base_cum'].iloc[-1] - 1)*100:.2f}%")
print("="*50)

# 绘图
# plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文显示，windows可用
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# fig 画布 ax1 坐标系 / 子图（白纸上用来画线的区域）
# fig, ax1 = plt.subplots(figsize=(12,6))

# # 左边：股价、5日线、10日线
# ax1.plot(df["trade_date"], df['price'], label='股价', color='gray', alpha=0.5)
# ax1.plot(df["trade_date"], df['ma_short'], label='5日均线', color='red')
# ax1.plot(df["trade_date"], df['ma_long'], label='10日均线', color='blue')
# ax1.set_ylabel('股价价格', color='black')
# # 给我把左边 Y 轴的数字样式，按默认风格显示出来
# ax1.tick_params(axis='y')

# # 右边：收益曲线 创建一个和左边 Y 轴 共享同一个 X 轴（日期） 的右边 Y 轴！
# ax2 = ax1.twinx()
# ax2.plot(df["trade_date"], df["strategy_return"], label='策略收益', color='orange', linewidth=2)
# ax2.plot(df["trade_date"], df["base_return"], label='持股不动收益', color='green', linewidth=2)
# ax2.set_ylabel('累计收益（初始=1）', color='red')
# ax2.tick_params(axis='y', colors='red')

# # 合并图例
# lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# plt.title('双均线走势 vs 策略收益对比')
# plt.grid(alpha=0.3)
# plt.show()


plt.figure(figsize=(12, 6)) # 创建一张新图画布，宽度12英寸 高度6英寸 Matplotlib 默认dpi = 100， 像素英寸 = dpi * 英寸
# plt.plot(x轴数据, y轴数据)
# plt.plot(df["strategy_cum"], label="策略收益", linewidth=2)
# plt.plot(df["base_cum"], label="持有不动", linewidth=2)
plt.plot(df["ma_short"], label="5日线", linewidth=2)
plt.plot(df["ma_long"], label="10日线", linewidth=2)

plt.title(f"{code} 量化策略收益对比")
plt.xlabel("日期")
plt.ylabel("收益倍数")
plt.legend()
plt.grid(True)
plt.show()
