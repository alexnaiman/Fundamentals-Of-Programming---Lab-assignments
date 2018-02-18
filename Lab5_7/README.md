# About this assignment
You can configure the project settings from the `settings.properties` file 

You can modify:
* the type of repository: `repository=` oneOf(`sql`, `json`, `in-memory`, `binary`, `text-file`)
    * `sql` - it connect through mysql-connector-python to your mysql server 
    * `json` - it reads and writes the data to .json files
    * `binary` - it serializes and deserializes the data with pickle
    * `in-memory` - the data is represented only on run time
    * `text-file` - the data is persisted in a CSV formatted file
* the data source files for the selected repository type can be changed - `path/to/file.correctTypeOfFIle` 
    * `clients=` - for the client repo (see the actual settings.properties file for more)
    * `movies=` - for the movie repo
    * `rentals=` - for the rentals repo
* you can change the ui of the app:
    * `ui=` - oneOf(`console`, `gui`)
## Important
**If you want to use the sql repository you need to change the config object from the [Settings.py file](/Config/Settings.py). You also need to create the database on your server (you can use dump.sql to create a basic example)**


The problem statement I chose:

Write an application for movie rental. The application will store:
* Movie: `movieId`, `title`, `description`, `genre`.
* Client: `clientId`, `name`
* Rental: `rentalID`, `movieId`, `clientId`, `rented date`, `due date`, `returned date`.

Create an application which allows the user to:
1. Manage the list of clients and available movies. The application must allow the user to add,
remove, update, and list both clients and movies.
2. Rent or return a movie. A client can rent an available movie until a given date, as long as they
have no rented movies that passed their due date for return. A client can return a rented movie
at any time. Only available movies are available for renting.
3. Search for clients or movies using any one of their fields (e.g. movies can be searched for using
id, title, description or genre). The search must work using case-insensitive, partial string
matching, and must return all matching items.
4. Create statistics:
    * Most rented movies. This will provide the list of movies, sorted in descending order of
the number of times they were rented or the number of days they were rented.
    * Most active clients. This will provide the list of clients, sorted in descending order of the
number of movie rental days they have (e.g. having 2 rented movies for 3 days each
counts as 2 x 3 = 6 days).
    * All rentals. All movies currently rented
    * Late rentals. All the movies that are currently rented, for which the due date for return
has passed, sorted in descending order of the number of days of delay.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation
performed by the user. Undo/redo operations must cascade and have a memory-efficient
implementation (no superfluous list copying).

### Requirements (the exact problem statement)
You will be given one of the problems below to solve.
* Use simple feature-driven software development process.
* Use object oriented programming for the program from the first iteration. Implement classes that
represent the entities in the problem domain, as well as the application’s layers, including the user
interface.
* The program must provide a console-based user interface based on a menu system. Exact
implementation details are up to you.
* Iterations are scheduled for three successive labs:
    * Iteration 1
         Implement features 1 and 2.
         Have at least 10 items in your application at startup.
         Provide specification and tests for all classes and methods except those of the UI.
    * Iteration 2
        * Also implement features 3 and 4.
        * Provide specification for all classes and methods except those of the UI.
        * Unit tests must be implemented using PyUnit
    * Iteration 3
        * All required features must be implemented
        * Have at least 100 items in your application at startup.
        * This iteration will be tested by your lab professor 
* Data validation - when the user enters invalid input values, they will be notified about the mistake.
####  BONUS POSSIBILITY (0.1P) - Done
* Have 95% code coverage using PyUnit tests, for all modules except the UI. Install the coverage module,
examine and improve your test code coverage until you reach this threshold. Deadline is week 9.
#### BONUS POSSIBILITY (0.2P) - Done
* In addition to the menu-based user interface required, also implement a graphical user interface (GUI)
for the program.
* To receive the bonus, both user interfaces (menu-based and graphical) must use the same program
layers. You have to be able to start the application with either user interface.
