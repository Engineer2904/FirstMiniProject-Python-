#taking input from user
customer_name = str(input("Enter the name of the customer: "))
phone_number= str(input("Enter the phone number: ")) 
#opening the product file to select product_id
print ( "Choose the product_id from the given data: " , "\n")
x= open("product.csv","r" )
xString=(x.read())
print (xString)
#closing product file 
x.close()
product_id= str(input("Enter the product id: "))
quantity= str(input("Enter the number of items: "))
#code to print the total amount and creating html file
x= open("product.csv","r" )
arr=[]
total=0
for i in x:
    rows= i.split(",")
    arr.append(rows)
x.close()
#print(arr)
#static element for html
invoice ="<html> <head>  </head> <body> "
invoice+= "<table> <tr> <td> Description </td> <td> Quantity </td> <td> Unit Price </td> <td>Total Price</td> </tr> "
file_customer= open("customer.csv","a")
customer_detail=""
#for invoice creation and appending into customer file
for j in range (len(arr)):
  if (product_id==arr[j][0]):
    price1= arr[j][2]
    total = int(quantity)*int(price1)
    #print(total)
    #dynamic elements
    invoice+= "<tr> <td>" + str(arr[j][1]) +"</td> <td>" + quantity + "</td><td>" + str(arr[j][2]) + "</td><td>" + str(total) +"</td></tr>"
    customer_detail+= product_id + ","+ customer_name + "," + phone_number + ","+ quantity + "," + str(total)
    file_customer.write("\n"+ customer_detail)
file_customer.close()
#invoice file
file_name= customer_name + ".html"
invoice_file= open(file_name, "x")
invoice_file.write(invoice)
#print(invoice)
invoice_file.close()
  


                                        






