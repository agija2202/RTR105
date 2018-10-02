Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=5
>>> if x < 10
SyntaxError: invalid syntax
>>> if x < 10:
	print ('Smaller')
	if x>20:
		print('Bigger')
		print ('Finis')
		x=5
		if x==5
		
SyntaxError: invalid syntax
>>> x=5
>>> if x==5:
	print ('Equals 5')
	if x > 4:
		print ('Great than 4')
		if x>=5:
			print('Great than or Equals 5')
			if x <6 : print('Less than 6')
			if x<=5:
				print('Less tan or Equals 5')
				if x!=6 :
					print ('Not equal 6')

					
Equals 5
Great than 4
Great than or Equals 5
Less than 6
Less tan or Equals 5
Not equal 6
>>> x=5
>>> print ('Before 5')
Before 5
>>> if x==5:
	print ('ls 5')
	print('ls Still 5')
	print ('Third 5')
	print('Afterwards 5 ')
	print ('Before 6')
	if x==6:
	print ('ls 6')
	
  File "<pyshell#31>", line 8
    print ('ls 6')
        ^
IndentationError: expected an indented block
>>> if x==6:
	print('ls 6')
	print('Is Still 6')
	print('Third 6')
	print('Afterwards 6')

	
>>> x=5
>>> print('Before')
>>> if x==5:
	print ('ls 5')
	print('ls Still 5')
	print ('Third 5')
	print('Afterwards 5 ')
	print ('Before 6')
	
>>> if x==6
SyntaxError: invalid syntax
>>> if x==6:
	print ('ls 6')
	print ('Is Still 6')
	print ('Third 6')
	print ('Afterwards 6')

	
>>> 
================== RESTART: /home/user/RTR105/if_test_1.py ==================
>>> 
================== RESTART: /home/user/RTR105/if_test_1.py ==================
Afterwards 6
>>> 
================== RESTART: /home/user/RTR105/if_test_1.py ==================
Is 5
Is Still 5
Third 5
Afterwards 5
Afterwards 6
>>> x=5
>>> if x>2:
	print('Biger than 2')
	print('Still bigger')
print('Done with 2')
SyntaxError: invalid syntax
>>> x=5
>>> if x>2:
	print('Biger than 2')
	print('Still bigger')
        print('Done with 2')
        
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)
	if i >2:
		print('Bigger than 2')
		print('Done with i',i)
		print('Alll Done')

		
0
1
2
3
Bigger than 2
('Done with i', 3)
Alll Done
4
Bigger than 2
('Done with i', 4)
Alll Done
>>> x=5
>>> if x > 2:
	print ('Bigger than 2')
	print ('Still bigger')
	print ('Done with 2')

	
Bigger than 2
Still bigger
Done with 2
>>> for i in range(5):
	print9i)
	
SyntaxError: invalid syntax
>>> print(i)
4
>>> for i range(5):
	
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)
	if i > 2:
		print('Bigger than 2')
		print ('Done with i',i)
		print('All Done')

		
0
1
2
3
Bigger than 2
('Done with i', 3)
All Done
4
Bigger than 2
('Done with i', 4)
All Done
>>> x=42
>>> if x>1:
	print('More tahn one')
	if x<100 :
		print('Less than 100')
		print('All Done')]
		
SyntaxError: invalid syntax
>>> print ('All Done')
All Done
>>> x=42
>>> if x>1:
	print('More tahn one')
	if x<100 :
		print('Less than 100')
		print('All Done')
		
>>> 
>>> x=42
>>> if x>1:
	print('More than one')
	if x<100:
		print('Less tahn 100')
		print('All Done')

		
More than one
Less tahn 100
All Done
>>> x=4
>>> if x>2:
	print('Bigger')
	else:
		
SyntaxError: invalid syntax
>>> x=4
>>> if x>2:
	print ('Bigger')
	else :
		
SyntaxError: invalid syntax
>>> x=4
>>> if x>2:
	print ('Bigger')
	else:
		
SyntaxError: invalid syntax
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Is 5
Is Still 5
Third 5
Afterwards 5
Afterwards 6
Biger than 2
Still bigger
Done with 2
Bigger
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Bigger
All done
>>> if x<2:
	print('small')
	elif x<10:
		
SyntaxError: invalid syntax
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/if_test_2.py", line 1, in <module>
    if x<2:
NameError: name 'x' is not defined
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
LARGE
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
All done
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================

Traceback (most recent call last):
  File "/home/user/RTR105/if_test_2.py", line 1, in <module>
    if x<2 :
NameError: name 'x' is not defined
>>> 
================== RESTART: /home/user/RTR105/if_test_2.py ==================
Medium
>>> 
