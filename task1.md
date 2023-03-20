# Task 1 Approach

1. Schedule and attend a requirements gathering session with SME
2. Write code (see `task1.py`)
3. Automation infrastructure. Assuming access to Apache Airflow (or similar workflow tool), I would set up a dag that calls my file generation script on a cadence specified by the SME, since they can tell us what time new data will be available from day to day. I'll set the dag to execute a few hours before 8pm so that there is ample time to catch any errors before expected delivery time.