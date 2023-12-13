#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:37:29 2023

@author: jennitran
"""
# =============================================================================
# Project 3
# Code correction
# author: Group 11
# last modified: December 13, 2023
# =============================================================================


# Must be the updated versions 
import pandas as pd
from plotnine import *
import os
import numpy as np

# Must be from the correct directory
os.chdir("/Users/leah/Desktop/2450 Spyder/Notes")
# Must be from the correct folder
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
# Must be the correct file name
dat  = dat["Combined Mileage (mpg)"]

# Class for calculating bootstrap confidence intervals
class Boot_CI():
    def __init__(self, data = None):
        """
        Initialize the Boot_CI object.

        Parameters
        ----------
        data : pd.Series, optional
            Input data for which the bootstrap confidence interval will be calculated.
            The default is None.

        Returns
        -------
        None.

        Attributes
        ----------
        stat : str
            The statistic to calculate from the bootstrap samples (default is "mean").
        dat : pd.Series
            The input data for which the bootstrap confidence interval will be calculated.
        n_boot : int
            The number of bootstrap samples to generate (default is 0).
        boot_stat : list
            List to store the calculated statistic for each bootstrap sample.
        ci_level : float
            Confidence level for the bootstrap confidence interval (default is 0.95).
        """
        "Initialize the simulation"
        
        # these are the values that things are auto set to 
        self.stat = "mean"
        self.dat = data
        # Set the value of bootstrap samples according to the number of samples
        # that you want to generate
        self.n_boot = 0 
        self.boot_stat = []
        # #3. kept the line below(chose CI level attribute over user input CI level) 
        self.ci_level = .95

        
    # Method for counting simulations   
    def add_sims(self, n, boot_sample): #1. Added parameters to be passed to the method

        """

        Calculates number of simulations and appends statistic chosen by user

 

        Parameters

        ------

        n: int

            length of sample used in bootstrap.

        boot_sample: list

            Sample used within bootstrap.

 

        Returns

        -------

        None.

 

        """

        #5. Fixed error when no data loaded but add_sims is ran by creating 
        # a check for if data is loaded
        if self.dat is None:
            print("No data loaded. Please load data before running simulations.")
            return


        # Assigns "n" (int) to length of sample data
        n = len(self.dat)

        

        # For i within number of times bootstrap sample runs
        for i in range(self.n_boot):

            # Establishes sample for bootstrap as "boot_sample" (list)
            boot_sample = self.dat.sample(n, replace = True)

           

            # If chosen statistic is median
            if self.stat == "median":

                # Append "boot_sample" median to "boot_stat" (list)
                self.boot_stat.append(float(boot_sample.median()))

           

            # Else/if chosen statistic is mean
            elif self.stat == "mean":

                # Append "boot_sample" mean to "boot_stat" (list)
                self.boot_stat.append(float(boot_sample.mean()))

           

            # Else/if chosen statistic is standard deviation
            elif self.stat == "std dev":

                # Append "boot_sample" standard deviation to "boot_stat" (list)
                self.boot_stat.append(float(boot_sample.std()))

          

            # Else give User communicating an incorrect chosen statistic
            else:
                # This is the error that is raised 
                raise TypeError("Wrong Statistic name")
         
    

    # Define clear sims funciton       
    def clear_sims(self):
        """cleares out boot_stat to be rerun"""
        # Clear the list of bootstrapped statistics
        self.boot_stat = []
    
    # Define the load fuction  
    def load_data(self,data):
        """Allows users to load in data, expecting data frame."""
        #2. Cleared boot_stat
        self.boot_stat = None  # Or set it to desired initial state
        self.dat = data
        
    # Define the function to update the number of bootstraps   
    def update_n_boot(self, new_n_boot):
        """this allows you change the value of n_boot, is an integer"""
        #this updates n_boot to be the specified the new level of boots put in
        self.n_boot = new_n_boot
    
    # This allows us to input a new stat 
    def set_statistic(self, stat):
        #6. Fixed docstring below
        """Set the statistic to be calculated from the bootstrap samples.

        Parameters
        ----------
        stat : str
            The statistic to calculate from the bootstrap samples.
            Should be one of {"mean", "median", "std dev"}.

        Returns
        -------
        None.
        """
        # Clears boot_stat
        self.boot_stat = []
        
        # Changes the new stat to be what was specified 
        self.stat = stat

     
    # Method to plot boot_stat on a histogram
    def plot_boot(self):
        """ intakes the list, boot_stat and returns a picture of a histogram """
        
        # Creates boot_df to be a data frame
        boot_df = pd.DataFrame({'x': self.boot_stat})
    
        # Create a ggplot histogram with column x of boot_stat
        p = (
            ggplot(boot_df, aes(x='x')) +
            geom_histogram()
            )
        
        # Returns the histogram p to have it show up 
        return p
    
    # This is a method that creates a confidence interval from the list boot_stat
    def conf_interval(self):
        """Assumes boot_stat is a list. Calculates a confidence interval off the list
        returns the value of the confidence interval in an array """
        
        # If the length of boot_stat is 0, meaning nothing has run, then the
        #method will not work and print an error message
        if len(self.boot_stat) == 0:
            # The message that is printed if the length is 0
            print("Boot_stat is 0. Must run sample first")
        
        # If boot_stat is not 0, then this runs
        else: 

            # Uses the percentile function in numpy and returns a confidence 
            # interval
            ci = np.percentile(self.boot_stat, [((1 - self.ci_level) / 2) * 100, (1 - (1 - self.ci_level) / 2) * 100])
                #4. Change. This adjusts the confidence interval calculation based on the self.ci_level attribute, 
                # which is a better approach than using the user-inputted alpha. This way, the method uses the 
                # confidence level specified during the initialization of the class (self.ci_level).   
        
        # Returns the two values of confidence interval   
        return ci 
            
            
    
# Creates the class       
test = Boot_CI()

# Runs method to load data
test.load_data(data = dat)

# Sets the number of times to bootstrap
test.update_n_boot(10000)

# Actually runs the boot strap 
test.add_sims()

# Creates a plot of the boot
test.plot_boot()

# Calculates the confidence interval 
test.conf_interval()


############################################
 
# 1. Importing packages
import pandas as pd
from plotnine import *
import os
import numpy as np

# Setting the directory to where my data is
os.chdir("C:/Users/Ryan/OneDrive/Desktop/STA 2450")

# 2. Imported data
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]

# 3. Ran class, only error fixed was an indentation error in the docstring on
# line 23, which was the init function.


# 4. Initialized class as sim1 and tried to run sims
sim1 = Boot_CI()
sim1.add_sims()  # Change: Added line to fix the reported error

# Received TypeError: object of type 'NoneType' has no len() because data was
# defaulted to None.
    # Change: Added the line sim1.add_sims() to fix the reported error. 
    # This line was missing, and it is necessary to run simulations

# 5. Initialized class as sim2 and tried to run sims with data.
sim2 = Boot_CI(data=dat)
sim2.add_sims()

# No bootstrap samples created because n_boot is set to zero and we could not
# specify the number we wanted in this function.
    # I believe that this mistake was due to user error. The group was able to
    # replace the value that n_boot was set to in order to suit their needs

# 6. Initialized class as sim3 and tried to run sims with data.
sim3 = Boot_CI(data=dat)
sim3.update_n_boot(10000)
sim3.add_sims()

# Ran 10000 simulations.

# 7. Tried to run 5000 more to see if we get 15000 total or just 5000 total.
sim3.update_n_boot(5000)
sim3.add_sims()

# It worked because we had 15000 total sims.

# 8. Tried to plot our distribution
sim3.plot_boot()

# It worked and gave us a plot.

# 9. Tried to run it with a different statistic
sim3.set_statistic("mean")  # Changed the input to match the expected string
sim3.add_sims()

# set_statistic says to enter an integer, so we did and got
# TypeError: Wrong Statistic name
    # Change: Modified the input to sim3.set_statistic("mean") to match the expected
    # string input for the statistic

# 10. Tried to change the statistic to one of the three in the function (which
# are strings and not integers)

sim3.set_statistic("median")
sim3.add_sims()

    # Change: Changed the input to sim3.set_statistic("median") to match the expected string
    # input for the statistic

# Worked, but we had to disobey what the docstring told us to do.  
    # I dont understand what they had to disobey. No changes were made.


############################################
"""
Comments by Dr. Patrick

1. In add_sims, docstring says there are parameters but there are no parameters
passed to the method. Fix this. 

    ****DONE**** 

2. In load_data, need to clear boot_stat 

    ****DONE, set to None, effectively clearing its previous content. 
    If you want to set it to a specific initial state other than None, you can 
    replace self.boot_stat = None with the desired value or initialization. 
    This step ensures that the boot_stat attribute starts fresh with the new 
    dataset.****

3. You have ci_level in __init__ but you ask the user for confidence level
in the method. Choose one or the other. 

    ****DONE chose user create an attribute for CI level, made changes to the method
    to use the confidence level specified during the initialization of the class (self.ci_level).****

4. alpha in conf_interval is not correct. Fix this. 

    ****DONE; Deleted 
    alpha = float(input("Please enter confidence level percentage. Must be an 
    integer: ")), deleted alpha = alpha/2 and ci = np.percentile(self.boot_stat, 
    [alpha, 100-alpha]) 

    The modification I provided is better because it adheres to the logic 
    established for 'alpha' as a confidence level, which is typically expressed as 
    a percentage between 0 and 100. In the original version, we asked the user to 
    input a percentage (e.g., 95 for a 95% confidence level), and then we correctly 
    adjusted this to a two-tailed test by dividing it by 2 before using it in the 
    np.percentile function.
    ****

5. Fix error when no data loaded but add_sims is ran.  

    ****WHAT I DID WAS: include a check for whether data is loaded (self.dat is 
    None). If no data is loaded, it prints an error message and returns from the 
    method, preventing the simulation code from running. This should address the 
    issue of running add_sims when no data is loaded.****

6. Fix docstring for set_statistic

    ****DONE****
"""


# FOR THE STUDENT COMMENTS: It seems that most of the comments were legitimate 
# errors. I did not understand the issue that was presented in comment #10.