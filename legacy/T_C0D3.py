##### T_C0D3 V1.0.1
var2 = '''
████████╗      ██████╗ ██████╗ ██████╗ ██████╗ 
╚══██╔══╝     ██╔════╝██╔═████╗██╔══██╗╚════██╗
   ██║        ██║     ██║██╔██║██║  ██║ █████╔╝
   ██║        ██║     ████╔╝██║██║  ██║ ╚═══██╗
   ██║███████╗╚██████╗╚██████╔╝██████╔╝██████╔╝
  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ 
                                -----T_C0D3 [V1.0.1]
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|               [ ₮_₵0Đ3 ]              |
	| Version : 1.0.1                       |
	| Creator : D4RK-C0D3                   |
	| Name    : Dipan Nama                  |
	| Github  : https://github.com/D4RK-C0D3|
	| Gmail   : Dipannama468@gmail.com      |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#####################################################
'''
var1 = "\033[1;32;40m" #### this is for colouring the programe 
print ( var1 + var2 )

### main code area ###
import os
sdcard = "/sdcard/"
os.chdir(sdcard)
print ("Enter folder name : ", end= "")
folder = input()
os.mkdir(folder)
dir_path = sdcard + folder
os.chdir(dir_path)
f = open("index.html","w")
file = '''<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="description" content="my contect">
		<meta name="keywords" content="HTML,CSS,XML,JavaScript">
		<meta name="author" content="Dipan Nama">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<title>My Site</title>
	</head>
	<body>
	
	<h1> Hello World </h1>

	<script src="js/main.js"></script>
	</body>
</html>
'''
f.write(file)
f.close()
os.chdir(dir_path)
os.mkdir('css')
path1 = dir_path + "/css"
os.chdir(path1)
f = open("style.css","w")
f.write("")
f.close()
os.chdir(dir_path)
os.mkdir('js')
path2 = path1 = dir_path + "/js"
os.chdir(path2)
f = open("main.js","w")
f.write("")
f.close()
var3 = "\033[0m"
print (var3)

### github : www.github.com/D4RK-C0D3
### contect : dipannama468@gmail.com
##### please don't remove this footer credit area
