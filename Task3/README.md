# GET APIs <br/>
**6 APIs required, <br/>
 3 for the statistics for each hour in the last 24 hours , and was done using cronjobs to collect the data <br/>
 3 for current Memory/CPU/Disk usage, and was collected using python modules**

  ![image](https://github.com/user-attachments/assets/86c6f307-f3ef-4769-b545-53d899fa7b3d)

# Logging
**Logging is configured to write INFO level messages and above to a file named log.log. <br/>**

**A logger object is created using logging.getLogger(__name__). Additionally, a decorator is applied to functions to automatically log their calls and results.<br/>**

**The @wraps(fn) decorator ensures the wrapper retains the original function’s metadata.**

![image](https://github.com/user-attachments/assets/b9ce2a41-b1bc-4732-8963-7fcbf4eeda0d)

#Unit-Testing

