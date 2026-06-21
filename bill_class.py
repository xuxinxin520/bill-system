import json
from datetime import datetime
import os

class Bill:
    def __init__(self):
        self.file_name = "bill.json"
        # 如果文件不存在，初始化空账单文件
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding="utf‑8") as f:
                json.dump([], f, ensure_ascii=False)

    def add_bill(self, money, bill_type, category, note=""):
        """
        添加一笔账单
        :param money: 金额，正数代表收入，负数代表支出
        :param bill_type: 收入 / 支出
        :param category: 分类：餐饮，交通，娱乐，学习，其他
        :param note: 备注
        """
        # 读取原有全部账单
        with open(self.file_name, "r", encoding="utf‑8") as f:
            bill_list = json.load(f)
        # 构造单条账单字典
        one_bill = {
            "time": datetime.now().strftime("%Y‑%m‑%d %H:%M:%S"),
            "date": datetime.now().strftime("%Y‑%m"),
            "money": money,
            "bill_type": bill_type,
            "category": category,
            "note": note
        }
        bill_list.append(one_bill)
        # 写回json文件
        with open(self.file_name, "w", encoding="utf‑8") as f:
            json.dump(bill_list, f, ensure_ascii=False, indent=2)
        print("账单添加成功！")

    def get_all_bills(self):
        # 获取全部账单，返回列表
        with open(self.file_name, "r", encoding="utf‑8") as f:
            return json.load(f)

    def select_by_time(self, start_time, end_time):
        """根据起止日期筛选账单，格式 YYYY‑MM‑DD"""
        bills = self.get_all_bills()
        res = []
        for item in bills:
            t = item["time"].split(" ")[0]
            if start_time <= t <= end_time:
                res.append(item)
        return res