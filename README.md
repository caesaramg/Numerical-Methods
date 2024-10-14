# Numerical-Methods
Solution of boundary value problems in one dimension by the finite element method

This repository contains the solution to a boundary value problem. The task involves solving a boundary value problem using the finite element method (FEM) in Python. This repository covers the implementation of various numerical methods such as Gaussian elimination, Jacobi iteration, and numerical quadrature, culminating in solving differential equations by discretising the domain into elements.

Problem Overview
The boundary value problem tackled in this coursework is:

\begin{equation}
- y'' = f \quad \text{on} \, [0,1] \quad \text{subject to} \, y(0) = y_0, \, y(1) = y_1
\end{equation}

 
This equation models physical systems like the displacement of a wire subjected to a load or the temperature distribution in a wire heated with an internal source.

The solution involves:

Transforming the problem into its weak (integral) form.
Discretising the domain using the finite element method.
Solving the resulting system of linear equations.
The repository implements a simple finite element solver that solves this problem using both direct and iterative methods.

Features

Finite Element Method: Implementation of a 1D FEM solver for second-order boundary value problems.
Numerical Quadrature: Use of the trapezoidal rule for numerical integration of right-hand side integrals.
Solvers:
Gaussian Elimination: Direct method for solving the tridiagonal matrix system.
Jacobi Iteration: Iterative method for solving the system with varying levels of tolerance.

Error Analysis: Calculation of error norms to evaluate the accuracy of the finite element solution.

Structure

Main.py: The main script that assembles the FEM matrix, applies boundary conditions, and solves the system using either Gaussian elimination or Jacobi iteration.
Gaussian_Elimination.py: Implementation of the direct solver using the Thomas algorithm for tridiagonal matrices.
Jacobi_Iteration_File.py: Implementation of the Jacobi iterative solver for the system of equations.
Numerical_Quadrature.py: Code for performing numerical integration using the trapezoidal rule.
Coursework Documentation: Detailed explanation of the methodology and tasks completed in the coursework.

Tasks
Code Analysis: Understanding and identifying key parts of the FEM procedure in the provided code.
Code Completion: Implementing the missing components, such as the right-hand side integral calculation and the Jacobi method.
Testing: Verifying the accuracy of the FEM solution using an analytical solution and conducting a performance analysis of the Jacobi method on different mesh sizes.
