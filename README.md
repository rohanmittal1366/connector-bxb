
## **Overview**

Connecter BxB is a platform designed by keeping in mind to ease the communication gap between wholesalers and retailers. The idea was to make B2B trade transparent and eliminate the third party. In this platform the retailer can order the product and amount of products they want by themselves without any kind of third party and the wholesaler can deliver the product. Likewise, the wholesaler can manage the product incorporation and distribution.

**Web Application Architecture**

First user request to server for connector Bxb. View sees the user request, retrieves appropriate data from the database, then renders back the template along with retrieved data

![](RackMultipart20211115-4-107dodn_html_cb401dde868755ac.jpg)

## **Use Case Diagram**

- Above figure shows the use case diagram for web applications.
- We have two types of users: Admin and User
- The functionalities accessed by Admin are : Create Product, Update Product, Delete Product, View Products, View Profile, View All Profiles and Assign Privileges.
- The functionalities accessed by User are : View Products, View Profile and Make Request
- Users can make a request to the admin for products

![](RackMultipart20211115-4-107dodn_html_1b4bffd56a843906.png)

## **Sequence Diagram**

- Above diagram shows a sequence diagram for our web application.
- First user will be redirected to the Login Page. If the user does not have an account, then he/she can go to the Register Page.
- After filling the register form, the user will be redirected to the Login Page.
- After login, the user will be redirected to the Staff Dashboard and admin will be redirected to Admin Dashboard after interacting with databases whether the user exists or not.

![](RackMultipart20211115-4-107dodn_html_e66e9d119724ca3b.jpg)

# **Templates**

1. **Dashboard**

1. **Index.html**

- This is the index page of the admin dashboard.
- Information contains the message that we want to show on a daily basis.
- The Statistics section contains three cue cards: Staff, Products and Order. The number shows the quantity of cue cards. We have 9 staff members, 11 products and 11 orders.
- The Pie Chart shows the number of orders requested by users for any particular product and the area shows the quantity of product.
- The Bar chart shows the products and quantity of products we have.

![](RackMultipart20211115-4-107dodn_html_1a0c18c3d8f1c8a0.png)

1. **Product.html**

- This is the product template. It shows the Navigation bar , Information and Statistics section same as other pages.
- Here it shows the products in table format with name, category, quantity and activity.
- Admin can search by applying filters like name, category and quantity.
- To add the product it contains product form with the field name, category and quantity.
- To modify or delete any product admin is required to click on edit or delete button of a particular product.

![](RackMultipart20211115-4-107dodn_html_22f20b5b51633d45.png)

1. **Staff.html**

- This is the staff template and contains information about staff. It shows the Navigation bar , Information and Statistics section same as other pages.
- Here it shows the users information in table format with username, email and phone no.
- Admin can view profiles by clicking the view button of any particular user.
- Admin can use search by applying filters like username.

![](RackMultipart20211115-4-107dodn_html_c6931f42f4cb2ad2.png)

1. **Order.html**

- This is the order template and contains information about orders. It shows the Navigation bar, Information and Statistics section similar to other pages.
- Here it shows the order placed by users in table format with product, category, quantity and order date.
- Admin can search by filters like product name, product category and staff.

![](RackMultipart20211115-4-107dodn_html_3d17abf8358604c8.png)

1. **User**

  1. **Login.html**

- Login can be done via email id and password.
- Validation is provided for email and password and respective warning will be provided
- Forgot password feature is provided which will take mail ID as input and send new password generation mail to that ID.
- After login, users can be redirected to either admin or user dashboard depending on the privilege provided.

![](RackMultipart20211115-4-107dodn_html_ffc1a8fb5b273d84.png)

  1. **Register.html**

- Users can register themselves by submitting their username, email, password.
- After clicking on the submit button user can redirect to login page.

![](RackMultipart20211115-4-107dodn_html_36a955336fa024cf.png)

  1. **Logout.html**

- User logout from the session after clicking on the logout button.
- Users can login after clicking login button.

![](RackMultipart20211115-4-107dodn_html_7c12f5a9f674a882.png)

  1. **Index.html**

- It shows the Navigation bar, Make request form and Order requests.
- Navigation bar contains a view profile and logout button.
- User can make request by filling a form with product name and product quantity fields.
- Order Request contains the request made by user in ascending order.

![](RackMultipart20211115-4-107dodn_html_40267679173699e7.png)

  1. **Profile.html**

- User can see the details of his own
- After clicking on the edit button the user can edit all the details including profile pic.

![](RackMultipart20211115-4-107dodn_html_2f4257c3b3f96890.png)

  1. **Forgot\_password.html**

- Users can change the password by entering an email and submitting the details.

![](RackMultipart20211115-4-107dodn_html_d460602c80d6c488.png)

# **Features**

1. **Admin**

  1. **Add product**

- Admin can add products by filling a form which contains the name of the product, category and quantity as a field.
- If admin wants to add a One Plus product of Electronics category and 50 quantities.

![](RackMultipart20211115-4-107dodn_html_a8fe797cbf99dbb0.png)

- Green flash message shows that One Plus product is added. In table product number 12 One plus is added.

![](RackMultipart20211115-4-107dodn_html_f4401af977b9d9d.png)

  2. **Edit product**

- Admin can edit a product by clicking the edit button in the activity center of that product. Form is populated with data of that product.

![](RackMultipart20211115-4-107dodn_html_2816a01320da962f.png)

- Quantity is changed from 50 to 100.

![](RackMultipart20211115-4-107dodn_html_99ff33b59764acfd.png)

- One plus quantity is modified in 12 number row.

![](RackMultipart20211115-4-107dodn_html_1b86656fd0441bca.png)

  3. **Delete Product**

- To delete a product admin is required to click on the delete button besides that product. Then it shows the confirmation message like below.

![](RackMultipart20211115-4-107dodn_html_260d2fa12ee9c1f8.png)

- One plus product is deleted from the database. Here row no 12 is deleted.

![](RackMultipart20211115-4-107dodn_html_3b1edadb4b4525fc.png)

  4. **Searching by data**

- Admin can search in a table using a search filter. Here the clothing category is selected and the table shows all the products with category clothing.

![](RackMultipart20211115-4-107dodn_html_f50028ddd2868a5c.png)

- Here rohan is selected as a staff member in the order table. And it shows all orders placed by rohan.

![](RackMultipart20211115-4-107dodn_html_a216389c52531544.png)

- Rohan is selected as the username in the user table.

![](RackMultipart20211115-4-107dodn_html_806e2dd47103b65a.png)

  5. **Edit Profile**

- After clicking on the profile button in the navigation bar admin is redirected to the profile page. It shows the image of admin, name, email, phone, address as profile information.

![](RackMultipart20211115-4-107dodn_html_dd55d5708c6b6317.png)

- After clicking on the edit button, the form is populated with all the information. Here address and profile photo are changed.

![](RackMultipart20211115-4-107dodn_html_ead3fadfb5f3044e.png)

- After clicking on the update button profile is updated which is given below.

![](RackMultipart20211115-4-107dodn_html_82e8ec93e5efabf1.png)

  6. **Pie Chart &amp; Histogram**

- This pie chart shows the order placed by all the users
- Area shown by the chart is the quantity of the order like pencil have 100 quantities.

![](RackMultipart20211115-4-107dodn_html_ee8ca7bd4ed0f892.png)

- We can see the remaining order by clicking on the name of the order and chart changed the area accordingly.

![](RackMultipart20211115-4-107dodn_html_31891f48bb23f6d1.png)

- Here histogram shows all the products with frequency of its quantity. For example Paracetamol has 250 quantity and Pencil has 150 quantity.

![](RackMultipart20211115-4-107dodn_html_b3687fcc6f1de78a.png)

1.
## **Staff**

  1. **Register**

- User can register by submitting the details like username, password and email
- Users can register themself by clicking on the register button.

![](RackMultipart20211115-4-107dodn_html_63a59f16d44befd5.png)

- After clicking on submit button user redirect to login page
- Green message flash on the screen saying register successfully.

![](RackMultipart20211115-4-107dodn_html_3780cddbf31c9364.png)

  2. **Login**

- Users after submitting details like username and password, user can be able to login and redirect to dashboard

![](RackMultipart20211115-4-107dodn_html_3b5410a44662ecda.png)

- This is the user dashboard shown after login page

![](RackMultipart20211115-4-107dodn_html_6ff204ecea1abf7c.png)

  3. **Logout**

![](RackMultipart20211115-4-107dodn_html_dbe5325de5da2e01.png)

  4. **Make request**

- If the user wants to make a request for a particular product of a particular category and a certain quantity.
- Users can submit the details like product and order quantity like USB-100 and 50 respectively.

![](RackMultipart20211115-4-107dodn_html_8d64b89c1a177d4f.png)

- After submitting the details, the user can see the request on the screen below.

![](RackMultipart20211115-4-107dodn_html_2e6a7c3a667d0a6b.png)

  5. **Edit profile**

- If the user/admin wants to edit their profile they can edit by clicking on the button.

![](RackMultipart20211115-4-107dodn_html_9115aaeda02f375e.png)

- User can edit the details like username email address, address, phone, image.

![](RackMultipart20211115-4-107dodn_html_bf55edde59a83f8f.png)

- After clicking on submit button user can see the changes on the screen as below

![](RackMultipart20211115-4-107dodn_html_44f6561f2bb08dee.png)

  6. **Forgot password**

![](RackMultipart20211115-4-107dodn_html_445359f7b462d265.png)

- If the user forgot the password and want to change it, user have to submit the email id.

![](RackMultipart20211115-4-107dodn_html_3339e1fe3a590158.png)

- Reset mail sent after entering email

.

![](RackMultipart20211115-4-107dodn_html_91a902116c76292c.png)

- Password reset mail came to the user after entering his/her mail ID.

![](RackMultipart20211115-4-107dodn_html_719208b87f4785ff.png)

- By clicking on the link sent on mail we are taken to the new password page.

![](RackMultipart20211115-4-107dodn_html_cf48030d7cc5970.png)

- After entering a new password, the success page is shown.

![](RackMultipart20211115-4-107dodn_html_72710df23aeeedad.png)
