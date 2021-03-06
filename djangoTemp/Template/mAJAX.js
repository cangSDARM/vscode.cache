/*
    Asynchronous Javascript And XML(异步JS和XML)
    优点_使用js与服务器进行异步交互, 传输XML格式数据, 且交互时局部刷新网页
    缺点_需要处理浏览器兼容问题, 发送请求增多增加服务器压力
*/

/**
 *  -------------------------------局部刷新模拟
 * 
 * window.onload = function(){  //当文档加载完毕时执行
 *     var form = document.getElementById("form1")  //获取表单
 *     form.onsubmit = function(){  //监听表单提交
 *         var user = form.username.value;  //获取表单元素
 *         if(!user){
 *             var userSpan = document.getElementById('userSpan')   //获取span元素
 *             userSpan.innerText = '用户名不能为空';
 *             return false;    //标示拦截表单提交
 *         }
 *         return true;
 *     }
 * }
 */

// --------------------------------四步操作__JS
//1. 创建核心对象(XMLHTTPRequest)
function creatXMLHttpRequest(){
    var xmlHead;
    try{
        xmlHead = new XMLHttpRequest();
    }catch(e){
        //适用于IE6
        try{
            xmlHead = new ActiveXObject("Msxm12.XMLHTTP");
        }catch(e){
            //适用于IE更早版本
            xmlHead = new ActiveXObject("Microsoft.XMLHTTP");
        }
    }
    return xmlHead;
}
var xmlHttpRequest = creatXMLHttpRequest();
//2. 使用核心对象打开与服务器链接
xmlHttpRequest.open("POST", "/index", true);    //open(请求方式, URL, 是否异步)
//3. 发送请求
xmlHttpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");   //POST必须设置请求头
xmlHttpRequest.send(null);      //send(请求体:"str=value")[-Get请求:send(null)-]
//4. 注册监听, 监听服务器响应
xmlHttpRequest.onreadystatechange = function(){ // 指定监听函数, 在对象状态发生变化时调用,执行4次!
    //readyState[查看对象状态, 4标示监听响应结束]
    //status[服务器响应状态码, 服务器响应结束后才有]
    if(xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200){
        var date = xmlHttpRequest.responseText;     //获取服务器响应体, 后端的httpresponse
    }
};

//---------------------------------基于jQuary
//-------------$.ajax()
// -1 --------------------
token = $('[name = "csrfmiddlewaretocken"]').val()
$.ajax({
    url:"/index",
    type:"POST",
    headers:{'X-CSRFToken':token},  //csrf
    data:{
        'a':1,
        'b':"name",
        'csrfmiddlewaretocken':token,       //csrf
        //'csrfmiddlewaretocken':"{{csrf_token}}"   //csrf
    },
    traditional:true,   //数据若是复杂结构, 需要加
    processData:true,  //是否对数据预处理
    contentType:text,
    dataType:"json",      //要求后端传输数据类型
    beforeSend:function(XMLHttpRequest){},    //发送数据前调用. 用于修改请求头, 返回false可以取消发送请求
    success:function(data){     //返回成功后调用
        console.log(typeof data);
    },
    error:function(data){},     //返回错误时调用
    complate:function(XMLHttpRequest){},    //传输步骤完成调用
    statusCode:{        //根据状态码调用
        "404":function(){},
        "403":function(){}
    }
});
// -2 ---------------------
$.ajax(
    url("/index"),
    type("POST"),
    data($("#form1").seralize()),    //form表单(id=form1), 自动序列化所有form内容为json数据发送
    traditional(true)               //seralize要加
);
//-------------简单方式
$.post("/index", {name:"alex"}, function(data, statusTest, jqh){     //post(url, [data], [callback], [type:text/html/json/script])
    alert(data);    //data是后端返回数据
    dates = JSON.parse(data);   //将后端json字符串转为json对象
    datas = JSON.stringify(dates);  //将json对象转为json字符串
    alert(statusTest);  //状态文本, 只有"success"和"error"
    alert(jqh);     //核心对象
});
$.get();    //get(url, [data], [callback], [type])
$.getJSON();    //type=Json的get
$.getscript();  //getscript(scriptURL, callback) 在callback中调用外部js文件的function

// ------------------- AJAX不能直接传递文件, 需借助FormData
var formdata = new FormData();
formdata.append("key", "value");    //FormData本质是一个字典
formdata.append("file", document.getElementById("file").Files[0]);  //添加文件对象
xmlHttpRequest.send(formdata);  //AJAX-JS传递
$.post("/index", {data:formdata},   //AJAX-JQ传递
    processData=false, //tell jquary not to process the data
    contentType=false);  //tell jquary not to set contentType