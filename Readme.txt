#1. To get all menu items
GET
/restaurant/menu/


#2. To access booking table (need credentials)
GET
/restaurant/booking/tables/
credentials superuser:
username:Ricardos
password:1223
token:c86c6d133ae26c275004ba4d3dfe8c0fd31f6bdc

for this in insomnia i had to go to headers tab and add: 
header:Authorization
value:Token c86c6d133ae26c275004ba4d3dfe8c0fd31f6bdc


#3. Create user 
POST
/auth/users/

#4. Generate user token 
POST
/restaurant/api-token-auth/
