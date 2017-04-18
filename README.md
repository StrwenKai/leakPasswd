# leakPasswd

> 这是一款用来查询密码泄露的 **`Python`** 模块

## 安装
### 安装方式一
```
pip install leakPasswd
```

### 安装方式二
**下载源码，进入源码目录**
```
python setup.py install
```

## 使用
 测试是否安装成功

```
import leakPasswd
```

### 查看所有泄露厂商的信息

```
import leakPasswd
leakPasswd.queryBreachs()
```

### 查看某个泄露厂商的信息

```
import leakPasswd
leakPasswd.findBreach('taobao')
```

### 查看泄露密码的账号

```
import leakPasswd
leakPasswd.findAccount('test@qq.com')
```

## 查询测试

![enter image description here](http://ww1.sinaimg.cn/large/005Bpb8ily1feqtmlem15g30hr0caagh.gif)

## 联系

> Author ：天才小三斤
>
> E-mail ：lauixData@gmail.com