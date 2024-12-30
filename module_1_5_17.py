immutable_var = 1,2.3,'ab','cd',True
print(immutable_var)
#immutable_var[0]=4 # При попытке внести в кортеж изменения выдает ошибку
#TypeError: 'tuple' object does not support item assignment
#это происходит потому, что кортеж относится к неизменяемым объектам
mutable_list = [1,2.3,'ab','cd',True]
print(mutable_list)
mutable_list[0] = 4
print(mutable_list)
