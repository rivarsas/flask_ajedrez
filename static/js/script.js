function changeColor(){
    console.log("color",color)
    console.log("color2",color2);
    var elements = document.getElementsByClassName('bg-light');
	for(var i = 0; i < elements.length; i++){
		elements[i].style.backgroundColor = color;
    }  
    var elements = document.getElementsByClassName('bg-dark');
	for(var i = 0; i < elements.length; i++){
		elements[i].style.backgroundColor = color2;
    }
}
changeColor();