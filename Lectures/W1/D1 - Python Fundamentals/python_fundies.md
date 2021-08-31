# What are the differences betweeen Javascript and Python?

## Variables

<table>
<thead>
<tr>
<th> Javascript </th>
<th> Python </th>
</tr>
</thead>
<tr>
<td>

In `Javascript`( js ), we use declaration statements such as `var`, `const`, and `let`

```js
var x = 25;
const y = 11;
let z = "apples"
```
</td>

<td>

In Python, we don't need any of that.

```py
x = 25
y = 11
z = 'apples'
```
</td>
</table>

## Conditionals

If/else statements, where you set a condition for the code following to run.

<table>
<thead>
<tr>
<th> Javascript </th>
<th> Python </th>
</tr>
</thead>
<tr>
<td>

```js
var min_height = 65;
var your_height = 72;

if(your_height >= min_height){
    console.log("You may ride the ride");
} else {
    console.log("Come back when you're taller");
}

```

</td>

<td>

```py
min_height = 65
your_height = 66
max_height = 74

if your_height >= min_height or your_height <= max_height:
    print("You may ride the ride")
elif your_height <= min_height and your_height >= max_height:
    print("You might want to see a doctor")
elif your_height <= min_height:
    print("Come back when you're taller")
elif your_height >= max_height:
    print("Come back when you're shorter")

```

</td>
</table>

## Looping
- For loops
- While loops

<table>
<thead>
<tr>
<th> Javascript </th>
<th> Python </th>
</tr>
</thead>
<tr>
<td>

```js

for(var i = 0; i < 10; i++){
    console.log(i);
}

while(i > 10){
    console.log(i);
    i++;
}

```

</td>

<td>

```py

for i in range(10): 
    print(i)

while i > 10:
    print(i)
    i++

```
</td>
</table>

# Lists/Arrays
<table>
<thead>
<tr>
<th> Javascript </th>
<th> Python </th>
</tr>
</thead>
<tr>
<td>

```js
var empty_list = []
var fruits = ['apples', 'bananas', 'tomatoes', 'mango']

//looping through array
for(var i = 0; i < fruits.length; i++){
    console.log(fruits[i])
}

for(var fruit of fruits){
    console.log(fruit)
}

//adding to end of array
fruits.push("Watermelon")

//remove at end of array
fruits.pop()

//remove at a certain element in the array
fruits.splice(2, 1)
// .splice(indexToRemoveAt, how many elements to remove)
```
</td>

<td>

```py
empty_list = []
fruits = ['apples', 'bananas', 'tomatoes', 'mango']

#looping through array
for i in range(len(fruits)):
    print(fruits[i])

for fruit in fruits:
    print(fruit)

#adding to array in python
fruits.append("Tangerines")

#remove at the end of array
fruits.pop()

#remove at a certain element in the array
fruits.pop(2)
```
</td>
</table>

## Dictionaries

```py
pizza = {
    "crust" : "thin",
    "cheese" : "mozzarella",
    "toppings" : ["mushrooms", "pepperoni", "bacon"]
}

print(pizza.crust)
print(pizza.cheese)

for topping in pizza.toppings:
    print(topping)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],

   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

for key,val in dojo.items():
    print(key + ":")
    for location in val:
        print(location)

#OUTPUT
#Location:
#San Jose
#Seattle
#Dallas .... so on so forth
```




