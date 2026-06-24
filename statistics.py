import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 修复：使用英文短横线 -
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文乱码
plt.rcParams["axes.unicode_minus"] = False

class Statistic:
    def __init__(self, bill_data):
        self.df = pd.DataFrame(bill_data)
        if not self.df.empty:
            self.df["money"] = self.df["money"].astype(float)

    def get_month_data(self, month):
        """筛选指定月份数据，参数格式：2026-06"""
        if self.df.empty:
            return pd.DataFrame()
        return self.df[self.df["date"] == month]

    def calculate_balance(self, month=None):
        """计算总收入，总支出，结余"""
        data = self.get_month_data(month) if month else self.df
        income = data[data["money"] > 0]["money"].sum()
        expend = abs(data[data["money"] < 0]["money"].sum())
        balance = income - expend
        print(f"总收入：{income:.2f} 元")
        print(f"总支出：{expend:.2f} 元")
        print(f"本月结余：{balance:.2f} 元")
        return income, expend, balance

    def draw_pie(self, month=None):
        """绘制各类消费占比饼图（只统计支出）"""
        data = self.get_month_data(month) if month else self.df
        expend_data = data[data["money"] < 0]
        if expend_data.empty:
            print("暂无支出数据，无法绘图")
            return
        expend_data["money"] = abs(expend_data["money"])
        group_data = expend_data.groupby("category")["money"].sum()
        group_data.plot(kind="pie", autopct="%.1f%%", figsize=(6, 6))
        plt.title("各类消费占比")
        plt.ylabel("")
        plt.show()

    def export_excel(self, filename="账单.xlsx"):
        # 导出全部账单到excel
        self.df.to_excel(filename, index=False)
        print(f"账单已导出至{filename}")
