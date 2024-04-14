

######## ASSIGNMENT TO CHECKOUT AND RESERVE BOOKS #############

Tech Stack - Python(FastAPI) and MongoDB

SUMMARY -
In this application, User can see multiple books present in the database. He/She can checkout any book (one BookID each time) and return the same. If no copies are available, a reservation for the bookID is made and he/she can Checkout it in future when a copy is available. If copies are available but less than the reservtions for that book, new person won't be able to borrow until reservations are fulfulled. In case the number of copies for that book are more than the unfulfilled reservations, any new person can borrow it.



DATABASE DESIGN -
Hence, all people who reserved the book are given a priority over new people. If extra copies are available, new person can borrow it.

Regarding the database, I have created 3 different collections to handle resrvation, circulation and number of copies. This way, it's very easy to track the status of the book and it's reservations.

Indexes have been created to fetch data faster.


CHALLENGES - 
The major challenge was to handle check - outs of books. A lot of factors were present which needed to be checked before allowing a checkout. For example, we need to see whether copies are available or not, automatically making a reservation if a copy wasn't available, storing timestamps for various events like reservation's RequestedAt and FulfilledAt.


IMPROVEMENTS -
Although a lot of things are already implemented in this assignment, we can set a time period for reservations(for example 7 days). This way, very old reservations for a bookID can be discared and new people would be allowed to borrow the books. Currently, a book is reserved for a person indefinitely.

Similarly, a time period can be set for borrowing books. If after 15 days the book is still not returned, we can fine members. The fine can be set according to the popularity of the book, its size, and number of people who have reserved it in the meanwhile.



DSA Problem:
The DSA problem given in the assignement is solved in a file named dsa_problem.py


