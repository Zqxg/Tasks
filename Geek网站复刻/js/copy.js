function copy1(){
	var u1=document.getElementById("qqgroup");
	u1.select();// 选择对象
	document.execCommand("Copy");// 执行浏览器复制命令
	alert("小锅温馨提示：QQ群号复制到剪贴板了哦 Y^-^Y");
}

function copy2(){
	var u2=document.getElementById("Email");
	u2.select();
	document.execCommand("Copy");// 执行浏览器复制命令
	alert("小锅温馨提示：邮箱复制到剪贴板了哦 Y^-^Y");
}