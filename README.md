# budget

Budget Analyzer is an application which can be used to keep track of person's money flow ( income and expense ).

The user can store expenses and income by running the script. 

The user can review and look where he is spending a lot of money.
Expenses are into different categories. They are:

	1. Food
	2. Travel
	3. Bills
	4. Clothing
	5. Grocery
	6. Shopping
	7. Health
	8. Other Expenses.
	
In a monthly review, user will be able to view his incomes and expenses for the last 30 days. 
It will be a visual representation. Expenses will be broken into categories and a cumulative expenses.
Planning to use bar graph here. One bar for income and a stacked bar for expenses.

Weekly review is same as monthly review, except that it is for last 7 days.

What I have done:

	1. Back end has 3 data bases ( mongo collections ).
			user_details : Contains user name and password for every user.
							Used during login to verify password.
			balance: Contains user name and balance.
						Used in get balance function.
			expense_tracker: Contains the incomes and expenses.
						We query this database to find the ecpenses.

What is yet to be done:

	1. To make the code self explanatory ( add comments, meaningful names ).
	2. Review - Plot graphs for review. ( Use seaborn ) ( Generate test records for review )
	3. Backup option which will write the data into a excel file or store it in a human readable format.
	4. Add Exception Handling

Requiring your kind contribution.

Test username:  test
Password:		test