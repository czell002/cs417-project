# Requirements

	* Python 3.11
	

# Sample Execution & Output

If run using 

```
python src/main.py data/raw/sensors-2018.12.26-no-labels.txt
```

within the project root, four output files will be created, one for each core:
1. output/sample-input-core-0.txt
2. output/sample-input-core-1.txt
3. output/sample-input-core-2.txt
4. output/sample-input-core-3.txt

The first of which will contain the first 10 lines:

```
       0 <= x <=       30 ; y =      61.0000 +       0.6333 x ; interpolation
      30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
      60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
      90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation
     120 <= x <=      150 ; y =      12.0000 +       0.4667 x ; interpolation
     150 <= x <=      180 ; y =     112.0000 +      -0.2000 x ; interpolation
     180 <= x <=      210 ; y =      34.0000 +       0.2333 x ; interpolation
     210 <= x <=      240 ; y =     146.0000 +      -0.3000 x ; interpolation
     240 <= x <=      270 ; y =       2.0000 +       0.3000 x ; interpolation
     270 <= x <=      300 ; y =     137.0000 +      -0.2000 x ; interpolation
```