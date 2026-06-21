from flask import Flask, render_template, request, redirect, url_for
from bill_class import Bill
from statistics import Statistic

app = Flask(__name__)
bill_obj = Bill()

# 主页，展示账单，接收所有表单提交
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    # 添加收入
    if request.method == "POST" and "income" in request.form:
        money = float(request.form["money"])
        category = request.form["category"]
        note = request.form["note"]
        bill_obj.add_bill(money, "收入", category, note)
        message = "收入添加成功！"
    # 添加支出
    elif request.method == "POST" and "expend" in request.form:
        money = -float(request.form["money"])
        category = request.form["category"]
        note = request.form["note"]
        bill_obj.add_bill(money, "支出", category, note)
        message = "支出添加成功！"
    # 统计收支
    month_data = None
    if request.method == "POST" and "count_month" in request.form:
        month = request.form["month"]
        stat = Statistic(bill_obj.get_all_bills())
        month_data = stat.calculate_balance(month)

    all_bills = bill_obj.get_all_bills()
    return render_template("index.html", bills=all_bills, msg=message, month_result=month_data)

# 绘图接口，网页展示饼图（简单方案：保存图片再展示）
@app.route("/draw", methods=["POST"])
def draw():
    import matplotlib.pyplot as plt
    month = request.form["month"]
    stat = Statistic(bill_obj.get_all_bills())
    stat.draw_pie(month)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)