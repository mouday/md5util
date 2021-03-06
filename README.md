# md5util
Pyhton3下的实用工具集合

[![PyPI](https://img.shields.io/pypi/v/md5util.svg)](https://pypi.org/project/chinesename/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/md5util.svg)

# 安装
```
pip3 install md5util
```

# 快速开始
```python
>>> from md5util import Md5Util


# 1、获取字符串的md5
>>> Md5Util.get_md5("hello world")
'5eb63bbbe01eeed093cb22bb8f5acdc3'


# 2、获取字典值的md5
>>> data = {
        "name": "Tom", 
        "age": 23, 
        "city": "beijing"
    }
>>> Md5Util.get_data_md5(data, ['name', 'age'])
'55d61ba470dcf2241af55b734a283991'

# 相当于：
>>> Md5Util.get_md5("Tom" + str(23))
'55d61ba470dcf2241af55b734a283991'
```

mac自带的md5生成工具来检测生成的结果
```bash
$ md5 -s 'hello world'
MD5 ("hello world") = 5eb63bbbe01eeed093cb22bb8f5acdc3
```

```
 *------------------------------------------------------------*
 |  有趣的小插件，快试试吧 ！                                     |
 *------------------------------------------------------------*
          o
           o   ^__^
            o  (oo)\_______
               (__)\       )\/\
                   ||----w |
                   ||     ||
```
