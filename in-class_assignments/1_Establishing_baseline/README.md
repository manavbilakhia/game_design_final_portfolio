# <center>For hw1_1.py</center>

* On the terminal navigate to the correct directory and please run the following command:
> python hw1_1.py
* It shall ask you the following questions:
* "Enter the distance in light years:"
* "Enter the percent of the speed of light:"
* Enter the details and press enter.
* It shall then print the result of the calculation.

* If you try to calculate the time taken when the speed of the space ship is 0% of the speed of light, it will generate a
* ZeroDivisionError as in general arithmetic, dividing by zero is not allowed. This occurs in line 7 while calculating the total time taken.
* If you try to calculate the time taken when the speed of the space ship is 100% of the speed of light, it will generate a
* ZeroDivisionError as in general arithmetic, dividing by zero is not allowed. This occurs in line 5 while calculating the lorentz factor as 1-(v^2/c^2) = 0 since v^2/c^2 = 1.

# <center>For hw1_2.py</center>

* On the terminal navigate to the correct directory and please run the following command:
> python hw1_2.py
* do as the instructions say and enter the details.

# <center>For nightsky.py</center>

* On the terminal navigate to the correct directory and please run the following command:
> python nightsky.py
* It shall then ask you to make a choice of viewing the night sky or my failed attempt of making shooting stars in a night sky.
* Please enter the number of your choice and press enter.
* A new window will open with the nightsky

## Revision Notes:

## HW1 - travel time

I like your very clearly named (if long) variables, and the fact that you correctly use `if __name__ ==`.

## HW2 - guessing game

I'm not thrilled with how you have `input()` in both if and elif clauses here.

## Night Sky

I'm not a huge fan of having all the games in the same file here, but it's fine for now.  I really really don't like `for in in range` loops, when you can do it in a much more elegant way (although with three separate lists you'd have to zip them together to loop through them.

## Overall Feedback

I'm glad you pushed yourself here.  I'd like to see how you manage with object oriented versions this week.

