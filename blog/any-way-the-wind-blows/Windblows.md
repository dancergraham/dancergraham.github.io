
# Adding leading zeros with Python
Various ways to add leading zeros to a number, for instance a wind direction, using Python. 

## generate a list of wind directions
First some definitions. The wind direction is measured in degrees clockwise from north and represents the direction the wind is blowing __from__. For instance an easterly wind, ie wind blowing __from__ the east has a direction of 90 degrees. Let's generate 16 wind directions from 0 (north) to 337.5 (north by northwest). 



```python
interval = 22.5
assert 360 % interval < 0.001

directions = [interval * x for x in range(0,int(360/interval))]
print(directions)
```

    [0.0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5]
    

## string zfill method
No doubt the most pythonic way to add leading zeros to a bare string, the built-in `str.zfill()` method is designed to do just that. 


```python
for dir in directions:
    print(str(int(dir)).zfill(3), str(dir).zfill(5))
```

    000 000.0
    022 022.5
    045 045.0
    067 067.5
    090 090.0
    112 112.5
    135 135.0
    157 157.5
    180 180.0
    202 202.5
    225 225.0
    247 247.5
    270 270.0
    292 292.5
    315 315.0
    337 337.5
    

We can immediately see our first quirk: the integer representation truncates decimal values rather than rounding up (as I learned to do at school) or rounding towards the nearest even number (as the Python round() funtion would do).

	
## String slicing
Very fast and arguably even more readable for people with a good understanding of basic python syntax but no desire to read the docs or explore the obscure corners of the language. Add the maximum possible number of leading zeros and then slice the desired number of digits. 


```python
for dir in directions:
    print(('00'+str(int(dir)))[-3:],
    ('00'+str(dir))[-5:])
```

    000 000.0
    022 022.5
    045 045.0
    067 067.5
    090 090.0
    112 112.5
    135 135.0
    157 157.5
    180 180.0
    202 202.5
    225 225.0
    247 247.5
    270 270.0
    292 292.5
    315 315.0
    337 337.5
    

## String format : integers
As part of a longer string this allows the  number to be inserted with leading zeros. Compatible with all current versions of Python. 

	


```python
for dir in directions:
    print('As integer: {:03d}  |  As float: {:05.1f}'.format(int(dir), dir))
```

    As integer: 000  |  As float: 000.0
    As integer: 022  |  As float: 022.5
    As integer: 045  |  As float: 045.0
    As integer: 067  |  As float: 067.5
    As integer: 090  |  As float: 090.0
    As integer: 112  |  As float: 112.5
    As integer: 135  |  As float: 135.0
    As integer: 157  |  As float: 157.5
    As integer: 180  |  As float: 180.0
    As integer: 202  |  As float: 202.5
    As integer: 225  |  As float: 225.0
    As integer: 247  |  As float: 247.5
    As integer: 270  |  As float: 270.0
    As integer: 292  |  As float: 292.5
    As integer: 315  |  As float: 315.0
    As integer: 337  |  As float: 337.5
    

## F Strings
From Python 3.6 this is even terser.


```python
for dir in directions:
    print(f'As integer: {int(dir):03d}  |  As float: {dir:05.1f}')
```

    As integer: 000  |  As float: 000.0
    As integer: 022  |  As float: 022.5
    As integer: 045  |  As float: 045.0
    As integer: 067  |  As float: 067.5
    As integer: 090  |  As float: 090.0
    As integer: 112  |  As float: 112.5
    As integer: 135  |  As float: 135.0
    As integer: 157  |  As float: 157.5
    As integer: 180  |  As float: 180.0
    As integer: 202  |  As float: 202.5
    As integer: 225  |  As float: 225.0
    As integer: 247  |  As float: 247.5
    As integer: 270  |  As float: 270.0
    As integer: 292  |  As float: 292.5
    As integer: 315  |  As float: 315.0
    As integer: 337  |  As float: 337.5
    

## Class
By overloading the built-in `__str__()` method for the class we can create our own custom string representation of the value. 



```python
class WindRecord(int):
    def __init__(self, dir):
        self.dir = dir

    def __str__(self):
        return f'Wind direction: {self.dir:05.1f} degrees'


for dir in directions:
    d = WindRecord(dir)
    print(d)
```

    Wind direction: 000.0 degrees
    Wind direction: 022.5 degrees
    Wind direction: 045.0 degrees
    Wind direction: 067.5 degrees
    Wind direction: 090.0 degrees
    Wind direction: 112.5 degrees
    Wind direction: 135.0 degrees
    Wind direction: 157.5 degrees
    Wind direction: 180.0 degrees
    Wind direction: 202.5 degrees
    Wind direction: 225.0 degrees
    Wind direction: 247.5 degrees
    Wind direction: 270.0 degrees
    Wind direction: 292.5 degrees
    Wind direction: 315.0 degrees
    Wind direction: 337.5 degrees
    
