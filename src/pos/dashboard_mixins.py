from rest_api.models import *
from django.db.models import Sum, Min, Max, Count
from datetime import date, datetime


def get_annual_net_revenue(user):
    date_temp = date.today().year
    annual_order_subtotal = 0.0
    annual_expenses = 0.0
    order_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=date_temp).aggregate(Sum('order_subtotal'))
    annual_expense_sum = Expense.objects.filter(
        user=user, timestamp__year=date_temp).aggregate(Sum('amount'))
    if order_subtotal_sum['order_subtotal__sum']:
        annual_order_subtotal = order_subtotal_sum['order_subtotal__sum']
    if annual_expense_sum['amount__sum']:
        annual_expenses = annual_expense_sum['amount__sum']
    return annual_order_subtotal - annual_expenses


def get_monthly_net_revenue(user):
    month_temp = date.today().month
    monthly_order_subtotal = 0.0
    monthly_expenses = 0.0
    monthly_order_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__month=month_temp).aggregate(Sum('order_subtotal'))
    monthly_expense_sum = Expense.objects.filter(
        user=user, timestamp__month=month_temp).aggregate(Sum('amount'))
    if monthly_order_subtotal_sum['order_subtotal__sum']:
        monthly_order_subtotal = monthly_order_subtotal_sum['order_subtotal__sum']
    if monthly_expense_sum['amount__sum']:
        monthly_expenses = monthly_expense_sum['amount__sum']
    return monthly_order_subtotal - monthly_expenses


def get_daily_expense(user):
    day_temp = date.today().day
    daily_expense_total = 0.0
    daily_expense_sum = Expense.objects.daily().filter(
        user=user, timestamp__day=day_temp).aggregate(Sum('amount'))
    if daily_expense_sum['amount__sum']:
        daily_expense_total = daily_expense_sum['amount__sum']
    return daily_expense_total


def get_monthly_expense(user):
    month_temp = date.today().month
    month_expense_total = 0.0
    month_expense_sum = Expense.objects.filter(
        user=user, timestamp__month=month_temp).aggregate(Sum('amount'))
    if month_expense_sum['amount__sum']:
        month_expense_total = month_expense_sum['amount__sum']
    return month_expense_total


def get_session_no(user):
    month_temp = date.today().month
    month_session_no = 0
    month_session_temp = Session.objects.filter(
        user=user, opening_time__month=month_temp).count()
    if month_session_temp:
        month_session_no = month_session_temp
    return month_session_no


def get_monthly_order_no(user):
    month_temp = date.today().month
    monthly_order_no = 0
    monthly_order_temp = PosOrder.objects.orders().filter(
        user=user, timestamp__month=month_temp).count()
    if monthly_order_temp:
        monthly_order_no = monthly_order_temp
    return monthly_order_no


def get_monthly_return_no(user):
    month_temp = date.today().month
    monthly_return_no = 0
    monthly_return_temp = PosOrder.objects.monthly_return().filter(
        user=user, timestamp__month=month_temp).count()
    if monthly_return_temp:
        monthly_return_no = monthly_return_temp
    return monthly_return_no

# /////////////////////////////////////////////////////// Graph Data


def get_net_revenue_by_month(user):
    current_year = date.today().year
    # January
    january_subtotal = 0.0
    january_expenses = 0.0
    january_purchase = 0.0
    january_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="01").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    january_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="01").aggregate(Sum('amount'))
    if january_subtotal_sum['order_subtotal__sum']:
        january_subtotal = january_subtotal_sum['order_subtotal__sum']
    if january_subtotal_sum['order_purchase_price_total__sum']:
        january_purchase = january_subtotal_sum['order_purchase_price_total__sum']
    if january_expenses_sum['amount__sum']:
        january_expenses = january_expenses_sum['amount__sum']
    january_final = january_subtotal - january_expenses
    january_profit = january_subtotal - january_expenses - january_purchase
    # February
    february_subtotal = 0.0
    february_expenses = 0.0
    february_purchase = 0.0
    february_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="02").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    february_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="02").aggregate(Sum('amount'))
    if february_subtotal_sum['order_subtotal__sum']:
        february_subtotal = february_subtotal_sum['order_subtotal__sum']
    if february_subtotal_sum['order_purchase_price_total__sum']:
        february_purchase = february_subtotal_sum['order_purchase_price_total__sum']
    if february_expenses_sum['amount__sum']:
        february_expenses = february_expenses_sum['amount__sum']
    february_final = february_subtotal - february_expenses
    february_profit = february_subtotal - february_expenses - february_purchase
    # March
    march_subtotal = 0.0
    march_expenses = 0.0
    march_purchase = 0.0
    march_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="03").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    march_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="03").aggregate(Sum('amount'))
    if march_subtotal_sum['order_subtotal__sum']:
        march_subtotal = march_subtotal_sum['order_subtotal__sum']
    if march_subtotal_sum['order_purchase_price_total__sum']:
        march_purchase = march_subtotal_sum['order_purchase_price_total__sum']
    if march_expenses_sum['amount__sum']:
        march_expenses = march_expenses_sum['amount__sum']
    march_final = march_subtotal - march_expenses
    march_profit = march_subtotal - march_expenses - march_purchase
    # April
    april_subtotal = 0.0
    april_expenses = 0.0
    april_purchase = 0.0
    april_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="04").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    april_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="04").aggregate(Sum('amount'))
    if april_subtotal_sum['order_subtotal__sum']:
        april_subtotal = april_subtotal_sum['order_subtotal__sum']
    if april_subtotal_sum['order_purchase_price_total__sum']:
        april_purchase = april_subtotal_sum['order_purchase_price_total__sum']
    if april_expenses_sum['amount__sum']:
        april_expenses = april_expenses_sum['amount__sum']
    april_final = april_subtotal - april_expenses
    april_profit = april_subtotal - april_expenses - april_purchase
    # May
    may_subtotal = 0.0
    may_expenses = 0.0
    may_purchase = 0.0
    may_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="05").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    may_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="05").aggregate(Sum('amount'))
    if may_subtotal_sum['order_subtotal__sum']:
        may_subtotal = may_subtotal_sum['order_subtotal__sum']
    if may_subtotal_sum['order_purchase_price_total__sum']:
        may_purchase = may_subtotal_sum['order_purchase_price_total__sum']
    if may_expenses_sum['amount__sum']:
        may_expenses = may_expenses_sum['amount__sum']
    may_final = may_subtotal - may_expenses
    may_profit = may_subtotal - may_expenses - may_purchase
    # June
    june_subtotal = 0.0
    june_expenses = 0.0
    june_purchase = 0.0
    june_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="06").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    june_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="06").aggregate(Sum('amount'))
    if june_subtotal_sum['order_subtotal__sum']:
        june_subtotal = june_subtotal_sum['order_subtotal__sum']
    if june_subtotal_sum['order_purchase_price_total__sum']:
        june_purchase = june_subtotal_sum['order_purchase_price_total__sum']
    if june_expenses_sum['amount__sum']:
        june_expenses = june_expenses_sum['amount__sum']
    june_final = june_subtotal - june_expenses
    june_profit = june_subtotal - june_expenses - june_purchase
    # July
    july_subtotal = 0.0
    july_expenses = 0.0
    july_purchase = 0.0
    july_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="07").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    july_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="07").aggregate(Sum('amount'))
    if july_subtotal_sum['order_subtotal__sum']:
        july_subtotal = july_subtotal_sum['order_subtotal__sum']
    if july_subtotal_sum['order_purchase_price_total__sum']:
        july_purchase = july_subtotal_sum['order_purchase_price_total__sum']
    if july_expenses_sum['amount__sum']:
        july_expenses = july_expenses_sum['amount__sum']
    july_final = july_subtotal - july_expenses
    july_profit = july_subtotal - july_expenses - july_purchase
    # August
    august_subtotal = 0.0
    august_expenses = 0.0
    august_purchase = 0.0
    august_subtotal_sum = PosOrder.objects.filter(user=user, timestamp__year=current_year, timestamp__month="08").aggregate(
        Sum('order_subtotal'), Sum('order_purchase_price_total'))
    august_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="08").aggregate(Sum('amount'))
    if august_subtotal_sum['order_subtotal__sum']:
        august_subtotal = august_subtotal_sum['order_subtotal__sum']
    if august_subtotal_sum['order_purchase_price_total__sum']:
        august_purchase = august_subtotal_sum['order_purchase_price_total__sum']
    if august_expenses_sum['amount__sum']:
        august_expenses = august_expenses_sum['amount__sum']
    august_final = august_subtotal - august_expenses
    august_profit = august_subtotal - august_expenses - august_purchase
    # September
    september_subtotal = 0.0
    september_expenses = 0.0
    september_purchase = 0.0
    september_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="09").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    september_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="09").aggregate(Sum('amount'))
    if september_subtotal_sum['order_subtotal__sum']:
        september_subtotal = september_subtotal_sum['order_subtotal__sum']
    if september_subtotal_sum['order_purchase_price_total__sum']:
        september_purchase = september_subtotal_sum['order_purchase_price_total__sum']
    if september_expenses_sum['amount__sum']:
        september_expenses = september_expenses_sum['amount__sum']
    september_final = september_subtotal - september_expenses
    september_profit = september_subtotal - september_expenses - september_purchase
    # October
    october_subtotal = 0.0
    october_expenses = 0.0
    october_purchase = 0.0
    october_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="10").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    october_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="10").aggregate(Sum('amount'))
    if october_subtotal_sum['order_subtotal__sum']:
        october_subtotal = october_subtotal_sum['order_subtotal__sum']
    if october_subtotal_sum['order_purchase_price_total__sum']:
        october_purchase = october_subtotal_sum['order_purchase_price_total__sum']
    if october_expenses_sum['amount__sum']:
        october_expenses = october_expenses_sum['amount__sum']
    october_final = october_subtotal - october_expenses
    october_profit = october_subtotal - october_expenses - october_purchase
    # November
    november_subtotal = 0.0
    november_expenses = 0.0
    november_purchase = 0.0
    november_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="11").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    november_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="11").aggregate(Sum('amount'))
    if november_subtotal_sum['order_subtotal__sum']:
        november_subtotal = november_subtotal_sum['order_subtotal__sum']
    if november_subtotal_sum['order_purchase_price_total__sum']:
        november_purchase = november_subtotal_sum['order_purchase_price_total__sum']
    if november_expenses_sum['amount__sum']:
        november_expenses = november_expenses_sum['amount__sum']
    november_final = november_subtotal - november_expenses
    november_profit = november_subtotal - november_expenses - november_purchase
    # December
    december_subtotal = 0.0
    december_expenses = 0.0
    december_purchase = 0.0
    december_subtotal_sum = PosOrder.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="12").aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
    december_expenses_sum = Expense.objects.filter(
        user=user, timestamp__year=current_year, timestamp__month="12").aggregate(Sum('amount'))
    if december_subtotal_sum['order_subtotal__sum']:
        december_subtotal = december_subtotal_sum['order_subtotal__sum']
    if december_subtotal_sum['order_purchase_price_total__sum']:
        december_purchase = december_subtotal_sum['order_purchase_price_total__sum']
    if december_expenses_sum['amount__sum']:
        december_expenses = december_expenses_sum['amount__sum']
    december_final = december_subtotal - december_expenses
    december_profit = december_subtotal - december_expenses - december_purchase
    # Finals
    revenue_data = {
        "January": january_final,
        "February": february_final,
        "March": march_final,
        "April": april_final,
        "May": may_final,
        "June": june_final,
        "July": july_final,
        "August": august_final,
        "September": september_final,
        "October": october_final,
        "November": november_final,
        "December": december_final,
    }

    profit_data = {
        "January": january_profit,
        "February": february_profit,
        "March": march_profit,
        "April": april_profit,
        "May": may_profit,
        "June": june_profit,
        "July": july_profit,
        "August": august_profit,
        "September": september_profit,
        "October": october_profit,
        "November": november_profit,
        "December": december_profit,
    }

    expense_data = {
        "January": january_expenses,
        "February": february_expenses,
        "March": march_expenses,
        "April": april_expenses,
        "May": may_expenses,
        "June": june_expenses,
        "July": july_expenses,
        "August": august_expenses,
        "September": september_expenses,
        "October": october_expenses,
        "November": november_expenses,
        "December": december_expenses,
    }

    pos_dict = {
        "revenue_data": revenue_data,
        "profit_data": profit_data,
        "expense_data": expense_data,
    }
    return pos_dict


"""
'SELECT product.name, product.quantity, SUM(shoppingCartProduct.product_quantity) AS product_quantity, 
SUM(shoppingCartProduct.product_subtotal) AS product_subtotal, SUM(shoppingCartProduct.product_discount) AS product_discount 
FROM product INNER JOIN shoppingCartProduct ON product.id = shoppingCartProduct.product_id 
INNER JOIN posOrder ON posOrder.cart_id = shoppingCartProduct.shopping_cart_id 
WHERE posOrder.order_subtotal > 0 GROUP BY product.name ORDER BY SUM(shoppingCartProduct.product_quantity) DESC');
"""


def get_top_product(user):
    products = Product.objects.filter(user=user)
    orders = PosOrder.objects.filter(user=user, order_subtotal__gt=0)
    pure_data_temp = {}
    for order in orders:
        for product in products:
            filtered_data_temp = ShoppingCartProduct.objects.filter(user=user, product_id=product.product_pk, shopping_cart_id=order.cart_id).aggregate(
                Sum('product_quantity'), Sum('product_subtotal'), Sum('product_discount'))
            if filtered_data_temp['product_quantity__sum'] is not None:
                # in here we do update the dictionary value if the product_pk is existed other wise we add more
                if product.product_pk in pure_data_temp:
                    single_product_dict = pure_data_temp.get(
                        product.product_pk)
                    product_quantity_sum = single_product_dict.get(
                        'sold_quantity')
                    product_subtotal_sum = single_product_dict.get(
                        'product_subtotal')
                    product_discount_sum = single_product_dict.get(
                        'product_discount')
                    data_temp = {
                        "product_pk": product.product_pk,
                        "product_name": product.name,
                        "stock_amount": product.quantity,
                        "sold_quantity": filtered_data_temp['product_quantity__sum'] + product_quantity_sum,
                        "product_subtotal": filtered_data_temp['product_subtotal__sum'] + product_subtotal_sum,
                        "product_discount": filtered_data_temp['product_discount__sum'] + product_discount_sum,
                    }
                    pure_data_temp.update({product.product_pk: data_temp})
                else:
                    data_temp = {
                        "product_pk": product.product_pk,
                        "product_name": product.name,
                        "stock_amount": product.quantity,
                        "sold_quantity": filtered_data_temp['product_quantity__sum'],
                        "product_subtotal": filtered_data_temp['product_subtotal__sum'],
                        "product_discount": filtered_data_temp['product_discount__sum'],
                    }
                    pure_data_temp.update({product.product_pk: data_temp})

    # iterate throught a dictionary
    pure_data = [value for key, value in pure_data_temp.items()]
    top_six_subtotal = []
    top_six_quantity = []
    ordered_subtotal = sorted(
        pure_data, key=lambda i: i['product_subtotal'], reverse=True)
    for order in ordered_subtotal:
        top_six_subtotal.append(order)
        if len(top_six_subtotal) == 6:
            break
    ordered_quantity = sorted(
        pure_data, key=lambda i: i['sold_quantity'], reverse=True)
    for order in ordered_quantity:
        top_six_quantity.append(order)
        if len(top_six_quantity) == 6:
            break
    top_six_data = {
        "top_six_subtotal": top_six_subtotal,
        "top_six_quantity": top_six_quantity,
    }
    return top_six_data

