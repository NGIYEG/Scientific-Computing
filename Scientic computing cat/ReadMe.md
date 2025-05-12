ICS 2207 Scientific Computing – CAT 

Instructions: Answer ALL questions. Each question is worth 20 marks.

Question 1: Practical Gradient Descent Implementation (20 marks) 
You are provided with the function f(x) = x^2 - 6x + 9. 
a) Implement a Python function that performs gradient descent to minimize this function. 
The function should take as parameters: - the initial guess x0, - learning rate alpha, - and number of iterations n. 
The function should return the list of x-values and f(x)-values for each iteration. [10 
Marks] 
b) Run your function with x0 = 2, alpha = 0.1, and n = 10. Present the output as a table 
with columns: iteration, x-value, f(x)-value.                                                          
[6 Marks] 
c) Explain what would happen if the learning rate were set to 1 instead of 0.1, using 
insights from your code and outputs.                                                                     
[4 Marks] 

Question 2: Linear Systems with Application Context (20 marks) 
A researcher is modeling a simple electrical circuit where: - 2I1 + 3I2 = 8 (KVL Equation 1) - 5I1 + 7I2 = 19 (KVL Equation 2) 
a) Formulate this system of equations as a matrix problem and solve it using NumPy in 
Python.                                                                                                                   
[6 Marks] 
b) Modify your code to read the coefficients and constants from a `.txt` file that has the 
system in this format: 
2 3 8 
5 7 19 
Write code to parse the file and solve the system. [8 Marks] 
c) Explain one real-world implication if the matrix of coefficients were nearly singular. 
How would that affect the solution, and what could you do about it computationally? [6 
Marks] 

Question 3: Data Visualization and Interpretation (20 marks) 
Given a file data.csv with two columns: Time (s) and Temperature (°C), your task is to 
analyze a heat transfer process. 
a) Write a Python script that: - reads the data using pandas, - plots a line graph of temperature vs time, - and adds labels, title, and grid.                                                                          
[10 Marks] 
b) Based on your graph, explain any two observations you can make about the heating 
process (e.g., steady state, rate of change).                                                            
[4 Marks] 
c) Describe a situation in engineering where such visualization can be used to influence 
decision-making.                                                                                                    
[6 Marks] 

Question 4: ODE Simulation of Real System (20 marks) 
You are simulating population growth using the differential equation dy/dt = 0.5y, where 
y(0) = 100. 
a) Use Euler’s Method to approximate the population size after 4 time steps with step size 
h = 0.5. Show all computations.                                                                             
[8 Marks] 
b) Write a Python function that generalizes the Euler’s method to solve any first-order 
ODE given f(t, y), initial condition, step size, and number of steps.                   
[6 Marks] 
c) Briefly explain two limitations of using Euler’s Method for real-world systems, and 
suggest one alternative method.  
