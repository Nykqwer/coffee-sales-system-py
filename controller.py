import matplotlib.pyplot as pt
#from mysql.connector import connect, Error
from mysql.connector import connect, Error
connection = None

try:
    connection = connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="coffe_salesdb",
        port="3308"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")


    def checkUser(username, password=None):
        cmd = f"Select count(username) from user where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a

      # Add a order
    def add_order(name,orders,total_price):
        try:
            query = "INSERT INTO ordertb (name, orders,total) VALUES (%s, %s, %s)"
            values = (name, orders,total_price)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_orders():
        try:
            cmd = "SELECT id,name,orders,total FROM ordertb;"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []  # Return an empty list if there's an error or no results
        
     # update order
    def update_order(id,order):
        cmd = f"update ordertb set orders ='{order}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True
            
        
        # Delete a order
    def delete_order(id):
        cmd = f"delete from ordertb where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    

         # ========================== Add Inventory =================================
          # ========================== Add Inventory =================================
           # ========================== Add Inventory =================================

    def add_inventory(p_name,descp,qty,cost,measure):
        try:
            query = "INSERT INTO inventorytb (p_name,description,quantity,cost,measure) VALUES (%s,%s,%s,%s,%s)"
            values = (p_name,descp,qty,cost,measure)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_inventory():
        try:
            cmd = "SELECT id,p_name,description,quantity,cost,measure FROM inventorytb;"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []
        

     # update inv
    def update_inventory(id,p_name,descp,qty,cost,measure):
        cmd = f"update inventorytb set id ='{id}', p_name ='{p_name}',description ='{descp}',quantity ='{qty}',cost ='{cost}',measure ='{measure}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True
            
        
        # Delete a order
    def delete_inventory(id):
        cmd = f"delete from inventorytb where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    

except Error as e:
    print(f"Error: {e}")