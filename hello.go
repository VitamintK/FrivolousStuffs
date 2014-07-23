package main

import "fmt"

func main() {
    fmt.Printf("hello, world\n")
    practice()
}

func practice(){
	//following learnxinyminutes.com and tour.golang.org
	//and freewheeling some

	//two line variable declaration and value assignment
	var x int //declaration
	x =3 //assignment

	//"short" declarations use := to infer type, declare, and assign
	y := 4
	sum, prod := addAndMult(x,y)
	fmt.Println("sum:", sum, "prod:", prod)
	learnTypes()
	arraytestres := arraytest([][]int{[]int{1,2},[]int{3,4}})
	fmt.Println(arraytestres)
}

func addAndMult(x, y int) (sum, prod int){
	return x + y, x * y
}

func learnTypes(){
	s := "Learn Go!"
	s2 := `a "raw" string literal
	can include line breaks.`

	f := 3.14159
	c := 3 + 4i

	//var syntax with initializers.
	var u uint = 7
	var pi float32 = 22. / 7

	n := byte('\n')

	//arrays have size fixed at compile time.
	var a4 [4]int
	a3 := [...]int{3, 1, 5}
	asdf,_,_,_,_,_,_,_,_ := s,s2,f,c,u,pi,n,a4,a3
	fmt.Println(asdf)
}

func arraytest(inputs [][]int)(ends [][]int){
	ends = inputs
	for _,y := range ends{
		y = append(y,3)
		fmt.Println(y)
	}
	return
}