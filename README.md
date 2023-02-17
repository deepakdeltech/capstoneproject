# current API endpoints for the **LittleLemon** Restaurant

## Homepage
- http://127.0.0.1:8000/                    `GET`   returns homepage (rendered index.html file, using static assets)

## User API
- http://127.0.0.1:8000/auth/users/         `POST`    provide *username* and *password* to create a user (sign up)
- http://127.0.0.1:8000/auth/token/login/   `POST`    provide *username* and *password* for given user to generate a token (login)
- http://127.0.0.1:8000/auth/token/logout/  `POST`    provide *username* and *token* for given user to destroy corresponding token (logout)
- http://127.0.0.1:8000/auth/users/         `GET`     provide valid *token* to return all users

## Menu API
- http://127.0.0.1:8000/menu/               `POST`    provide *title*, *price* and *inventory* to create a new **MenuItem**
- http://127.0.0.1:8000/menu/               `GET`     returns all **MenuItems**
- http://127.0.0.1:8000/menu/1              `GET`     returns **MenuItem** with specified pk in the URL-parameter (this case 1)
- http://127.0.0.1:8000/menu/1              `PUT`     provide *title*, *price* and *inventory* to update **MenuItem** with specified pk
- http://127.0.0.1:8000/menu/1              `PATCH`   provide one or many of *title*/ *price*/ *inventory* to modify **MenuItem** with specified pk
- http://127.0.0.1:8000/menu/1              `DELETE`  delets **MenuItem** with specified pk

## Booking API
- http://127.0.0.1:8000/booking/            `POST`    provide *name*, *num_guests*, *booking_date (YYYY-MM-DD)* and valid *token* to add a booking
- http://127.0.0.1:8000/booking/            `GET`     provide valid *token* to return all bookings
