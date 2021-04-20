#!/bin/bash
value =`cat t.txt`
value2 = ${value,,} 
eval $value2
