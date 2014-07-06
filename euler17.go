package main

import "fmt"

func main(){
	fmt.Println(euler())
}

func euler() (endamount int){
	tests := [...]int{1,5,20,21,30,35,100,150,171,1000}
	for _,value := range tests{
		fmt.Println(numtostr(value))
	}
	endamount = 0
	return
}

func numtostr(num int) (str string){
	ones := [...]string{"","one","two","three","four","five","six","seven","eight","nine"}
	tens := [...]string{"","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"}
	teens := [...]string{"ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"}
	//hundred = 7, and = 3
	if num>1000{
		str = ""
	} else {
		var lengthof int
		one,ten,hundred,thousand := num%10, (num%100)/10, (num%1000)/100, num/1000
		fmt.Println(one,ten,hundred,thousand)
		str = ones[hundred] + "hundredand" + tens[ten] + ones[one]
		fmt.Println(str,len(str))
		if thousand>0{
			lengthof = 11
		}else{
			lengthof = len(ones[hundred]) + len(tens[ten]) + len(ones[one]) //+conditional length of "hundred and" if hundred exists
			if hundred>0{
				lengthof+=10 //hundredand
			}
		}
		str = ""
		fmt.Println(lengthof)
	}
	return

}