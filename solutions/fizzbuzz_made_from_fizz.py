# A one line solution that also spells the word fizz.

print(
      [''.join((ix, x)          [1]) if ''.join((            ix, x)[1]) !=       '' else (ix, x)
      [0]                            +1                               for                ix, 
      x in enumerate(                zip                           ([''               if 
      i%3                            !=                          0                 else             
     'fizz'                          for                       i                 in       
     range                           (1,                     101                )]      
     ,[''                      if i%5 != 0 else           'buzz' for i in      range(1, 101)]))]
)