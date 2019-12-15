#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(log n) ==> I don't know what the specific answer is, but it seems to be growing in a logarithmic fashion.


c) O(2n) 

** I'm still not entirely sure about any of these.

## Exercise II

Instead of saying the building is n-stories high, I'm just going to say the building is 100 stories high for clarity's sake.  To find which floor is the one that breaks the egg being dropped from there, I would follow the subsequent steps:

  1. I would go the the 50th floor and drop an egg from there.  If it didn't break, I could eliminate half of the floors.  Anything under the 50th floor would not break an egg.  The reverse logic applies if the egg did break.  Anything above the 50th floor would break the egg.

  2. Again, I'd cut the remaining floors in half.  I'd go to the 25th floor and drop the egg.  If it didn't break, I'd assume that 75 floors 25-100 are safe to drop the egg without breaking.

  3. Repeat the process of halving until you find the 'breaking point.'

