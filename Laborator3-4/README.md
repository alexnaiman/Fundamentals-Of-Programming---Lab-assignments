# About this assignment
The problem statement I choose:

* A family wants to manage their monthly expenses. In order to complete this task, the family needs an
application to store, for a given month, all their expenses. Each expense will be stored in the
application using the following elements: day (of the month in which it was made, between 1 and 30),
amount of money (positive integer) and expense type (one of: housekeeping, food, transport,
clothing, internet, others). The family needs an application that provides the following functionalities
(each functionality is exemplified):

   
   1. Add a new expense into the list.
    
    
        add <sum> <category>
        insert <day> <sum> <category>
        
        # e.g.
        
        add 10 internet # add to the current day an expense of 10 RON for internet.
        
        insert 25 100 food # insert to day 25 an expense of 100 RON for food.
    
    
   2. Modify expenses from the list.
   
    
        remove <day>
        remove <start day> to <end day>
        remove <category>
     
        # e.g.
        remove 15 # remove all the expenses for day 15.
        remove 2 to 9 # remove all the expenses between day 2 and day 9.
        remove food # remove all the expenses for food from the current month.
   3. Write the expenses having different properties.
   
   
    list
    list <category>
    list <category> [ < | = | > ] <value>
    # e.g.
    list # write the entire list of expenses.
    list food # write all the expenses for food.
    list food > 5 # writes all expenses for food with an amount of money > 5.
    list internet = 44 # writes all expenses for internet with an amount of money = 44.
    
    
   4. Obtain different characteristics of sublists.
   
    sum <category>
    max <day>
    sort <day>
    sort <category>
    # e.g.
    sum food # write the total expense for category food.
    max day # write the day with the maximum expenses.
    sort day # write the total daily expenses in ascending order by amount of money spent.
    sort food # write the daily expenses for category food in ascending order by amount of money spent.
    
   5. Filter the list of expenses.
   
    filter <category>
    filter <category> [ < | = | > ] <value>
    #e.g.
    filter food # keep only expenses in category food.
    filter books < 100 # keep only expenses in category books with amount of money < 100 RON
    filter clothing = 59 # keep only expenses for clothing with amount of money = 59 RON
   
   6. Undo the last operation that modified program data.
    
    undo # the last operation that has modified program data will be reversed. The user has to be able to undo all operations performed since program start by repeatedly calling this function
### Requirements (the exact problem statement)
* You will be given one of the problems below to solve
* Use simple feature-driven software development process.
* The program must provide a console-based user interface that accepts the commands given
exactly as they are exemplified in the problem statements.
* Use Python’s built-in compound types to represent data in the problem domain.
* Iterations are scheduled for two laboratories:
    * Iteration 1
        * Implement features 1, 2 and 3
        * Use procedural programming
        * Have at least 10 items in your application at startup
        * Provide documentation
    * Iteration 2
        * Implement remaining features
        * Use modular programming (at least UI and functions modules)
        * Provide documentation, specification and tests (all functions except ones in UI)
        * This iteration will be tested by your lab professor 
* Data validation - when the user enters invalid commands or input values, they will be notified
about the mistake.
* The documentation will contain the problem statement, feature list, iteration plan, usage
scenario, work items/tasks, as shown within the Laboratory.03-04.sampleDoc.odt file. You can
reuse the same documentation file, but you must update it accordingly
