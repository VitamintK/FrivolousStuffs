package main

import "fmt"

func main(){
	fmt.Println(euler())
}

func euler() (endamount int){
	fmt.Println(numtostr(443))
	endamount = 0
	return
}

func numtostr(num int) (str string){
	ones := [...]string{"","one","two","three","four","five","six","seven","eight","nine"}
	tens := [...]string{"","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"}
	//hundred = 7, and = 3
	if num>1000{
		str = ""
	} else {
		one,ten,hundred,thousand := num%10, (num%100)/10, (num%1000)/100, num/1000
		fmt.Println(one,ten,hundred,thousand)
		str = ones[hundred] + "hundredand" + tens[ten] + ones[one]
		fmt.Println(str)
		if thousand>0{
			lengthof = 11
		}else{
		lengthof = len(ones[hundred]) + len(tens[ten]) + len(ones[one]) //+conditional length of "hundred and" if hundred exists
		if hundred>0{
			lengthof+=10 //hundredand
		}
		}
		str = ""
	}
	return

}