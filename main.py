from bill_class import Bill
from statistics import Statistic

def show_menu():
    print("====个人记账系统====")
    print("1. 添加一笔收入")
    print("2. 添加一笔支出")
    print("3. 查询全部账单")
    print("4. 按月统计收支并查看结余")
    print("5. 绘制月度消费饼图")
    print("6. 导出账单到Excel")
    print("0. 退出系统")
    print("====================")

def main():
    bill_obj = Bill()
    category_list = ["餐饮", "交通", "娱乐", "学习", "其他"]
    while True:
        show_menu()
        try:
            choice = int(input("请输入功能序号："))
        except ValueError:
            print("输入错误，请输入数字！")
            continue
        if choice == 1:
            # 收入
            try:
                money = float(input("输入收入金额："))
            except ValueError:
                print("金额格式错误！")
                continue
            print("选择分类：", category_list)
            cate = input("输入分类：")
            if cate not in category_list:
                print("分类不存在，默认设为其他")
                cate = "其他"
            note = input("添加备注(直接回车为空)：")
            bill_obj.add_bill(money, "收入", cate, note)
        elif choice == 2:
            # 支出，金额存为负数
            try:
                money = -float(input("输入支出金额："))
            except ValueError:
                print("金额格式错误！")
                continue
            print("选择分类：", category_list)
            cate = input("输入分类：")
            if cate not in category_list:
                print("分类不存在，默认设为其他")
                cate = "其他"
            note = input("添加备注(直接回车为空)：")
            bill_obj.add_bill(money, "支出", cate, note)
        elif choice == 3:
            bills = bill_obj.get_all_bills()
            for b in bills:
                print(b)
        elif choice == 4:
            month = input("请输入查询月份，格式例如2026‑06：")
            stat = Statistic(bill_obj.get_all_bills())
            stat.calculate_balance(month)
        elif choice == 5:
            month = input("输入要绘图的月份：")
            stat = Statistic(bill_obj.get_all_bills())
            stat.draw_pie(month)
        elif choice == 6:
            stat = Statistic(bill_obj.get_all_bills())
            stat.export_excel()
        elif choice == 0:
            print("程序退出")
            break
        else:
            print("序号超出范围，请重新输入")
        input("\n按下回车继续...")

if __name__ == "__main__":
    main()