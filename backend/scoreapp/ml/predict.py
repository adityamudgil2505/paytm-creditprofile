from sklearn.externals import joblib
import numpy as np

MLPCOD = joblib.load("./save/MLPCOD.save")
MLPEMI = joblib.load("./save/MLPEMI.save")
sc = joblib.load("./save/scaler.save")

# X = np.array([[52, 1, 0, 0,
#        0, 6,
#        1, 5,
#        30000,
#        0, 30000,
#        5000, 1]])
X = np.array([[35, 0, 1, 1,
       0, 25,
       12, 13,
       12000,
       0, 12000,
       100, 1]])


X_sc = sc.transform(X)
y_cod = MLPCOD.predict(X_sc)
y_emi = MLPEMI.predict(X_sc)

print(y_cod)
print(y_emi)




# X = np.array(['age', 'Is_auto_billing_on', 'Is_paytm_first', 'Is_postpaid',
#        'postpaid_outstanding', 'Orders_placed_in_6months',
#        'Orders_placed_in_6months_via_epay', 'Orders_placed_in_6months_via_cod',
#        'Total_money_on_order_from_mall_6months',
#        'Total_money_on_order_on_travel_6months', 'Total_money_spent',
#        'Total_money_added_on_wallet', 'RatioDvP'])


# X contains in this order:  ['age', 'Is_auto_billing_on', 'Is_paytm_first', 'Is_postpaid',
#        'postpaid_outstanding', 'Orders_placed_in_6months',
#        'Orders_placed_in_6months_via_epay', 'Orders_placed_in_6months_via_cod',
#        'Total_money_on_order_from_mall_6months',
#        'Total_money_on_order_on_travel_6months', 'Total_money_spent',
#        'Total_money_added_on_wallet', 'RatioDvP']

# where RatioDvP is ("Orders_delivered_in_6months")/("Orders_placed_in_6months"+1)

# master data contains ['age', 'Id', 'Is_auto_billing_on', 'Is_paytm_first', 'Is_postpaid',
#        'postpaid_outstanding', 'Orders_placed_in_6months',
#        'Orders_placed_in_6months_via_epay', 'Orders_placed_in_6months_via_cod',
#        'Orders_placed_in_6months_via_emi', 'Orders_delivered_in_6months',
#        'Total_money_on_order_from_mall_6months',
#        'Total_money_on_order_on_travel_6months',
#        'Total_money_on_order_on_movie_6months', 'Total_money_spent',
#        'Total_money_added_on_wallet', 'CODorNot', 'EMIorNot', 'RatioDvP']