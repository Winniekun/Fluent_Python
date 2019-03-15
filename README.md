# 涉及内容

-------



* [x] [易错的Python语法问题](https://github.com/KongWiKi/Fluent_Python/tree/master/Arithmetic)
* [x] [Effective Python](https://github.com/KongWiKi/Fluent_Python/tree/master/EffectivePython)
* [x] [Fluent Pythoh](https://github.com/KongWiKi/Fluent_Python/tree/master/FluentPython)
* [x] [LeetCode](https://github.com/KongWiKi/Fluent_Python/tree/master/LeetCode)
* [x] [大杂烩](https://github.com/KongWiKi/Fluent_Python/tree/master/Basis)
* [x] [Python常用包使用](https://github.com/KongWiKi/Fluent_Python/tree/master/Basis/package)
* [x] [Python做的有趣的东西](https://github.com/KongWiKi/Fluent_Python/tree/master/DivertivePython)



# 基础内容

---



## 函数：

#### 1. 关键字参数和位置参数

* 最常用的方式为**`位置参数`**，即按顺序第一个形参绑定到第一个实参，第二个形参绑定到第二个实参，以此类推。

  ```python
  def printName(firstName, lastName, reverse):
  	if reverse:
  		print(lastName + ', ' + firstName)
  	else:
  		print(firstName, lastName)
  ```

​       以下每行代码都是对 printName 的等价调用

​	printName('Olga', 'Puchmajerova', False)
​	printName('Olga', 'Puchmajerova', reverse = False)	

* **关键字参数**：形参根据名称绑定到实参。

  例如：

  ```python
  printName(lastName = 'Puchmajerova', firstName = ' Olga',
  reverse = False)
  ```

  但是尽管关键字参数可以在实参列表中以任意顺序出现，但将关键字参数放在非关键字参数后面是不合法的

  ```python
  printName('Olga', lastName = 'Puchmajerova', False)
  ```


* 待更

