var arr=["a","3","e","w","o","n","s","r","t","1","z","f","7","k","m",'d','h']; 
var wellplayed=""; 
for(i=1;i<13;i++) {
 	if(i % 4 == 0){
  		wellplayed += arr[i-2]
   	}
   	else {
   		wellplayed += arr[i+2]
   	}
}
console.log(wellplayed)
