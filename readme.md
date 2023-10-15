Python program for compressing and decompressing the Code 128 barcode symbol table.
Each symbol is stored in just 8 bits versus the 11 bits normally needed.
This can be useful for memory limited devices which need to display barcodes.

## Method
Each symbol is a total of 11 units long.
Symbols always begin with a bar and end with a space.
The sum of the width of bars must be even, whereas the sum of the widths of the spaces must be odd.  

Symbol patters can be stored in an 11 digit binary string where a 1 represents a bar, and a 0 represents a space.
Consider the pattern for the space symbol: ```11011001100```.
Here, the pattern is a 2 unit bar, 1 unit space, 2 unit bar, 2 unit space, 2 unit bar, 2 unit space.
Considering the above rules;
the pattern is 11 units long (2 + 1 + 2 + 2 + 2 + 2),
it begins with a bar and ends with a space,
the sum of the width of the bars is even (2 + 2 + 2 = 6),
and the sum of the width of the spaces is odd (1 + 2 + 2 = 5).  

For compression, we can simply omit the first and last two digits in the binary symbol pattern.
This leaves us with 8 bits.
The space symbol would result to ```10110011```.

For decompression, simply start with a 1, add the compressed string, then count the number of 1s in the string.
If the number of 1s is odd,
the next digit must be a 1 inorder to satisfy the condition of the sum of the widths being even,
if the number of 1s is even, the next digit must be a 0.
Finally, append the trailing 0 to the string.  

For the compressed space symbol ```10110011```:
1. Add the leading 1 to the start: ```110110011```
1. Count the number of 1s in the string: 6. 
This is an even number meaning the condition of the sum of the width of bars must be even is already satisfied,
therefore the next digit must be a 0: ```1101100110```
1. Add the trailing 0 to the end: ```11011001100```