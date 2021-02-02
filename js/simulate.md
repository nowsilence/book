function simulateClick(){
	//点击位置为屏幕中间
	var sx= window.innerWidth/2,sy= window.innerHeight/2,cx= sx,cy=sy;
	var eventDown = document.createEvent("MouseEvents");
	eventDown.initMouseEvent("mousedown",true,true,window,0,
		sx,sy,cx,cy,false,false,false,false,0,null);
	var eventUp = document.createEvent("MouseEvents");
	eventUp.initMouseEvent("mouseup",true,true,window,0,
		sx,sy,cx,cy,false,false,false,false,0,null);
	$("#container")[0].dispatchEvent(eventDown);
	$("#container")[0].dispatchEvent(eventUp);
}