This repository contains work related to the prompt for the Jr. Data Integration Developer assessment for Clear Spring Health. 

Please find my methodology for prioritizing these tasks under `priorities.md`
I have broken each task into a markdown file describing my approach and - where appropriate - a .py file containing the basic idea for how I would solve the respective problem programmatically. These scripts are effectively pseudocode, so it is not expected that you should be able to execute the scripts in their current state.

This work represents my approach to the business problems described below:

You have been given following three tasks to be completed as soon as possible. 
You may work on them one after other or you may work on those simultaneously

Please identify how you will prioritize each of those in order to finish most effectively so they can be completed in earliest possible time.

For each of those tasks, please write your approach to complete those. You may describe steps as free text, pseudo code, SQL code, flow charts as you feel appropriate

Task 1 :  You have been given a task to generate a  Comma Separated (.csv)  File  on daily basis per specifications as in attached Excel  file. For this task you will need to extract data from database tables.  There are some unknowns and you are required to work with subject matter expert (SME) to identify data elements. (sample has few fields but there could be several fields in reality)

Refer to csv files below for Task2 and Task 3

Task2:
From the attached .csv files, you need to compare records from above files dated 02_07_2021 and 02_08_2021 and identify if there are any members that are in one file but not in other and return a record with latest date range (span)  on End Date for each Member Id that exists in any of the files.
Empty End Date means its open span that has not yet ended.

Task 3 : File  sent to dated 02_07_2021 failed to load. Issue has been identified at lines 
Line 28
Line 63
Line 324
Since files need to be loaded in sequential manner, files sent after this cannot be loaded until this file is fixed, resulting member eligibility not getting updated in production.
What steps will you take to identify the issue, which records (specify MemberIds) need to be fixed, why and what you can do to fix those. You do not have ability to fix data in source tables, but you have ability to fix SSIS, Query or generated files.