package main

import "fmt"

func main(){
	fmt.Println(euler(1,1000))
}

func euler(firstnum, lastnum int) (endamount int){
	for i := firstnum; i <= lastnum; i++ {
		endamount += numtolen(i)
	}
	return
}

func numtolen(num int) (lengthof int){
	//just realized this could be written decently recursively
	ones := [...]string{"","one","two","three","four","five","six","seven","eight","nine"}
	tens := [...]string{"","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"}
	teens := [...]string{"ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"}
	if num>1000 || num<1{
		lengthof = 0
	} else {
		one,ten,hundred,thousand := num%10, (num%100)/10, (num%1000)/100, num/1000
		//fmt.Println(one,ten,hundred,thousand)
		if thousand>0{
			lengthof = 11
		}else{
			if ten == 1{
				lengthof = len(ones[hundred]) + len(teens[one])
			} else{
				lengthof = len(ones[hundred]) + len(tens[ten]) + len(ones[one])
			}
			if hundred>0{
				if one != 0 || ten != 0{
					lengthof+=10 //len(hundredand) == 10
				} else {
					lengthof += 7
				}
			}
		}
		//fmt.Println(lengthof)
	}
	return

}