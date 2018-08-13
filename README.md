# Angular Aot Fixer
Do you have a bunch of private component-variables (which you created back at that time when private variables was OK to use in templates) which makes the AOT compilation fails?
Don't worry. Run this script and your application will soon compile!

# Usage
0. Make sure to have your project backed up before using this script. This script also assumes that your components and your templates has the same file name (except the file endings). **Use at own risk**.
1. Try to compile your program. Copy the error-messages and paste them in the **log.txt** file.
*Example*:
```
ERROR in src/app/auth/components/login.component.html(16,119): : Expected 0 arguments, but got 1.
src/app/auth/components/login.component.html(22,131): : Expected 0 arguments, but got 1.
src/app/match/components/layout/layout.component.html(6,67): : Property 'counts' is private and only accessible within class 'LayoutComponent'.
src/app/match/components/layout/layout.component.html(6,67): : Property 'counts' is private and only accessible within class 'LayoutComponent'.
src/app/match/components/layout/layout.component.html(11,70): : Property 'counts' is private and only accessible within class 'LayoutComponent'.
src/app/match/components/layout/layout.component.html(11,70): : Property 'counts' is private and only accessible within class 'LayoutComponent'.
```

2. Update the **PROJECT_ROOT** variable in **main.py** to the absolute path of your project.
*Example*:
```python
PROJECT_ROOT = '/home/Users/marcus/Desktop/my-angular-project/'
```

3. Run the program **main.py** from the terminal (This will edit your **.ts** files)
```
python3 main.py
```

4. Go back to **step 1** and repeat until no errors occurs
