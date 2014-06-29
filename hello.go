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

}

func addAndMult(x, y int) (sum, prod int){
	return x + y, x * y
}