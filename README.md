# Entrada e Saída de Dados
----
Entrada:
```
S "GO" "Programa um" 05:00 06:00
S "BR" "Programa dois" 05:00 06:00
Q "GO" 05:30
Q "SP" 05:28
```
Saída:
```
A "GO" 05:30 "GO" "Programa um"
A "SP" 05:28 "BR" "Programa Dois"
```
----
Entrada:
```
S "DF" "Bom dia Um" 06:01 07:29
S "RJ" "Bom dia Dois" 06:01 07:29
S "SP" "Bom dia Três" 06:01 07:29
Q "RJ" 07:00
Q "GO" 06:50
```
Saída:
```
A "RJ" 07:00 "RJ" "Bom dia Dois"
A "GO" 06:50 noise
```