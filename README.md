# Un sistema que ilustra modularidad de un sistema sw

## howto1

Utilizamos wrappers de operadores aritméticos de pyton, en forma funcional:

- de `+` y `-` : `suma()` y `resta()` 
- de `*` y `//` : `multiplica()` y `divide()` 

## howto2

Repartimos mas o menos los objetos en mas o menos modulos

- Sin reparticion: (**monolito**, rama _main_)
- En 3 módulos (rama _ternary_, los modulos **`principal`**, **`sumres`** y **`muldiv`**)
- En 2 módulos (rama _binary_, **`principal`** y **`aritmetic`**)  
  
## target

Realizar el mismo sistema **en C** 
