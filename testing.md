# Cbench Test

- Single ONOS Docker Instance 

- Multi ONOS Docker Instances

# Single Controller 


## Latency 

### 12 Switches 

#### Command 

```bash
cbench -c 172.17.0.2 -s 12
```

#### Results 

```text
Total Count: responses/requests =  616263/616107
Total Average: responses/requests = 38516.44/38506.69
RESULT: 12 switches 15 tests min/max/avg/stdev = 22308.98/57404.62/40743.42/10297.04 responses/s
```

### 24 switches

#### Command

```bash
cbench -c 172.17.0.2 -s 24
```

### Results 

```text
Total Count: responses/requests =  779545/782437
Total Average: responses/requests = 48721.56/48902.31
RESULT: 24 switches 15 tests min/max/avg/stdev = 25026.97/67288.93/51749.88/14104.78 responses/s
```

### 36 switches

#### Command

```bash
cbench -c 172.17.0.2 -s 36
```

### Results 

```text
Total Count: responses/requests =  659171/658453
Total Average: responses/requests = 41198.19/41153.31
RESULT: 36 switches 15 tests min/max/avg/stdev = 12034.86/60430.52/43906.51/12511.20 responses/s
```

### 48 switches

#### Command

```bash
cbench -c 172.17.0.2 -s 48
```

### Results 

```text
Total Count: responses/requests =  473446/512716
Total Average: responses/requests = 29590.38/32044.75
RESULT: 48 switches 15 tests min/max/avg/stdev = 6121.08/53320.75/31558.11/11924.03 responses/s
```

### 60 switches

#### Command

```bash
cbench -c 172.17.0.2 -s 60
```

### Results 

```text
Total Count: responses/requests =  616564/646815
Total Average: responses/requests = 38535.25/40425.94
RESULT: 60 switches 15 tests min/max/avg/stdev = 7971.89/69233.97/41098.89/17646.26 responses/s
```

## Throughput 

### 12 Switches 

#### Command 

```bash
cbench -c 172.17.0.2 -s 12 -t
```

### Results

```text
Total Count: responses/requests =  1251646/5317721
Total Average: responses/requests = 78227.88/332357.56
RESULT: 12 switches 15 tests min/max/avg/stdev = 1347.42/176465.18/72528.68/70663.31 responses/s
```

### 24 Switches 

#### Command 

```bash
cbench -c 172.17.0.2 -s 24 -t
```

### Results

```text
Total Count: responses/requests =  1178732/9268569
Total Average: responses/requests = 73670.75/579285.56
RESULT: 24 switches 15 tests min/max/avg/stdev = 0.00/216673.12/69677.32/75191.75 responses/s
```

### 36 Switches 

#### Command 

```bash
cbench -c 172.17.0.2 -s 36 -t
```

### Results

```text
Total Count: responses/requests =  961791/7379056
Total Average: responses/requests = 60111.94/461191.00
RESULT: 36 switches 15 tests min/max/avg/stdev = 0.00/163774.13/58659.16/62525.30 responses/s
```

### 48 Switches 

#### Command 

```bash
cbench -c 172.17.0.2 -s 48 -t
```

### Results

```text
Total Count: responses/requests =  986264/10000751
Total Average: responses/requests = 61641.50/625046.94
RESULT: 48 switches 15 tests min/max/avg/stdev = 0.00/282422.12/57453.79/90536.96 responses/s
```

### 60 Switches 

#### Command 

```bash
cbench -c 172.17.0.2 -s 60 -t
```

### Results

```text
Total Count: responses/requests =  1049344/11417781
Total Average: responses/requests = 65584.00/713611.31
RESULT: 60 switches 15 tests min/max/avg/stdev = 0.00/234006.29/67435.50/82054.22 responses/s
```



---
---
---




## Latency for Multi controller

### 12 Switches 

#### Command 

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 12
```

### Results

```text
Total Count: responses/requests =  103194/102722					
Total Average: responses/requests = 6449.62/6420.12					
RESULT: 12 switches 15 tests min/max/avg/stdev = 2326.99/10915.29/6822.52/2182.57 responses/s		
```

### 24 switches

#### Command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 24
```

### Results 

```text
Total Count: responses/requests =  102950/102087					
Total Average: responses/requests = 6434.38/6380.44					
RESULT: 24 switches 15 tests min/max/avg/stdev = 812.00/13063.99/6854.68/3446.89 responses/s
```

### 36 switches

#### Command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 36
```

### Results 

```text
Total Count: responses/requests =  93405/92254					
Total Average: responses/requests = 5837.81/5765.88					
RESULT: 36 switches 15 tests min/max/avg/stdev = 904.00/8884.96/6224.28/2364.39 responses/s
```

### 48 switches

#### Command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 48
```

### Results 

```text
Total Count: responses/requests =  126337/124884					
Total Average: responses/requests = 7896.06/7805.25					
RESULT: 48 switches 15 tests min/max/avg/stdev = 1688.99/11715.82/8420.20/2622.93 responses/s
```

### 60 switches

#### Command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 60
```

### Results 

```text
Total Count: responses/requests =  136636/134981					
Total Average: responses/requests = 8539.75/8436.31					
RESULT: 60 switches 15 tests min/max/avg/stdev = 2642.99/12721.95/9107.22/2384.14 responses/s
```



---

## Throughput for Multi controller

### 12 switches

#### command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 12 -t
```

### Results

```text
Total Count: responses/requests =  950969/4378319
Total Average: responses/requests = 59435.56/273644.94
RESULT: 12 switches 15 tests min/max/avg/stdev = 5185.60/101349.13/63088.94/26432.29 responses/s
```

### 24 switches

#### command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 24 -t
```

### Results

```text
Total Count: responses/requests =  861896/6941286
Total Average: responses/requests = 53868.50/433830.38
RESULT: 24 switches 15 tests min/max/avg/stdev = 0.00/95253.59/57276.57/27479.59 responses/s
```


### 36 switches

#### command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 36 -t
```

### Results

```text
Total Count: responses/requests =  755593/7361608
Total Average: responses/requests = 47224.56/460100.50
RESULT: 36 switches 15 tests min/max/avg/stdev = 52.95/81577.51/50202.99/23202.95 responses/s
```


### 48 switches

#### command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 48 -t
```

### Results

```text
Total Count: responses/requests =  577805/11959769
Total Average: responses/requests = 36112.81/747485.56
RESULT: 48 switches 15 tests min/max/avg/stdev = 0.00/75825.57/38341.68/26631.47 responses/s
```

### 60 switches

#### command

```bash
cbench -c 172.17.0.6,172.17.0.7,172.17.0.8,172.17.0.9 -s 60 -t
```

### Results

```text
Total Count: responses/requests =  769698/12989210
Total Average: responses/requests = 48106.12/811825.62
RESULT: 60 switches 15 tests min/max/avg/stdev = 0.00/113468.65/51185.94/30202.06 responses/s
```
