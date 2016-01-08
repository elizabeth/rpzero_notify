# rpzero_notify

Python script which alerts if Adafruit has the Raspberry Pi Zero in stock. Checks the page every 120 seconds (2 minutes) and opens a windows alert box in stock, otherwise prints to the console. 

Could easily be modified to send a text alert or e-mail instead.

If error occurs with using the time and sleep, run with '-u' so that it is 'python -u zero_script.py'.
