#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NUMBER 1 SOLUTION
import numpy as np
import pandas as pd

store = pd.read_excel('Book.xlsx')

# Store_perc is the markup percentage of the various category and store_cats is a list of all the categories
store_perc = [0.25, 0.15, 0.10, 0.125]
store_cats = ['Cosmetics', 'Toiletries', 'Pastry', 'Beverages']
check_fig = pd.Series(store_perc, store_cats)

count = 0
# while count is less than length of items in store

while count < len(store):
    for item in [store['Category'][count]]:
        
#       Finds the price = unit cost + (unit cost + markup amount)
        price = store.loc[count, 'Unit Cost'] + (store.loc[count, 'Unit Cost'] * check_fig[item])
#       Locate the unit sales price in the store dataframe and set to the new sales price
        store.loc[count,'Unit Sale Price'] = price
    count+=1
store


# In[5]:


# NUMBER 2 AND 3 SOLUTION
cust_item = ['CK Perfume', 'Ginger beer', 'Pepsi Cola']
cust_amt = [2, 10, 5]

new_list = []
cust_goods = []
for item,qty in zip(cust_item,cust_amt):
#   Sums Customer product price = Unit sales price * quantity
    sum_items = sum(store[store['Product name'] == item]['Unit Sale Price'] * qty)
    
#   new_qty = Quantity in inventory - customer quantity ordered
    new_qty = store[store['Product name'] == item]['Quantity in Stock'] - qty

#   new_val extracts the numbers in the new_qty object
    new_val = new_qty.values
    new_int = int(new_qty.index.values)

#   Locates the item in the store and set it to the new reduced value
    store.loc[new_int, 'Quantity in Stock'] = new_val

#   Add items customers order and single products sum to a list
    cust_goods.extend([item, sum_items])
    new_list.append(sum_items)
print(cust_goods)
print("-------------------------------------------")
print(f'Total = {sum(new_list)}')
print("###########################################")

# Returns the new reduced store list
store


# In[3]:


# NUMBER 4 SOLUTION
if (not store[store['Quantity in Stock'] < 10].empty):
    for items in store['Product name'].values:
         print(f'{items} is below 10 units and needs to be restocked ')
else:
    print("Our inventory is full")


# In[4]:


# NUMBER 5 AND 6 SOLUTION
Product_name = input('')
Quantity = input('')

item_lists = Product_name.split(',')
item_qty = Quantity.split(',')
total_price = []
cust_data = []
cust_labels = []
cust_items = []
print("-----------------------------------------------------------------------------------------------------")

for item,qty in zip(item_lists,item_qty):
    prod_check = not store[store['Product name'] == item.strip()].empty
    qty_check = int(qty.strip()) < sum(store[store['Product name'] == item.strip()]['Quantity in Stock'].values)
    qty_inventory = store[store['Product name'] == item.strip()]['Quantity in Stock']

#     Check if product is in the store
    if(not prod_check):
        print(f'{item.strip()} is not in our store.')

# Check if product is in the store and customers quantity is less than the product quantity in store
    elif(prod_check & qty_check):
        sale_price_per_product = store[store['Product name'] == item.strip()]['Unit Sale Price']
        qty_ordered = int(qty.strip())
        
#         Add customers items, product sales price and quantity orders in different list
        cust_items.append(item.strip())
        cust_data.append(float(sale_price_per_product.values))
        cust_labels.append(qty_ordered)
        unit_price = sum(sale_price_per_product  * qty_ordered)
        total_price.append(unit_price)

        print(f'{item.strip()} is on sale.Please proceed to checkout')
# Check if customer product quantity is available in store
    else:
         print(f'{item.strip()} is insufficient in the store. {sum(qty_inventory.values)} left in store.')
print("-----------------------------------------------------------------------------------------------------")
data = {
    "Items": cust_items,
    "Sales Price": cust_data,
    "Quantity": cust_labels
}
df = pd.DataFrame(data)
print(df)
print("-----------------------------------------------------------------------------------------------------")
print(f'Total = {sum(total_price)}')


# In[ ]:




