# PNG_Height_Steganography
**CTF**的**MISC**中根据**CRC**计算**PNG**隐写的图片高度。
## Versions
**Python 3.10.0**
## Usage
```
usage: main.py [-h] [--source_path SOURCE_PATH] [--target_path TARGET_PATH]

PNG_Height_Steganography

options:
  -h, --help            show this help message and exit
  --source_path SOURCE_PATH, -s SOURCE_PATH
                        图片输入路径，默认为source文件夹
  --target_path TARGET_PATH, -t TARGET_PATH
                        图片输出路径，默认为target文件夹
```
## Examples
```
# 图片放进source文件夹，输出路径指向target文件夹
python main.py

# 指定图片输入路径，输出路径指向target文件夹
python main.py -s source/example.png

# 图片放进source文件夹，指定图片输出路径
python main.py -t target/

# 指定图片输入、输出路径
python main.py -s source/example.png -t target/
```