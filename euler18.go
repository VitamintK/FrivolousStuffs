package main

import "fmt"
import "strings"
import "strconv"

const MinInt :=  -(int(^uint(0) >> 1) - 1)

func main(){
	triangle := `75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23`
	trinodes := triToNodes(triangle)
	fmt.Println(trinodes)
	for  _,i := range trinodes[len(trinodes)-1]{
		for _,j := range i.parents{
			fmt.Println(j.value)
		}
		fmt.Println(i.value)
	}
}

func intmax(a, b int) int {
   if a < b {
      return b
   }
   return a
}

type node struct { //should capitalize node?
	value int
	parents []*node
	children []*node
}

func (n *node) addChild(childnodes []*node) (){
	n.children = append(n.children,childnodes...)
}

func triToNodes(tri string) (nodes [][]node){
	for rownum,rowslice :=  range strings.Split(tri,"\n"){
		row := []node{}
		for columnnum,value := range strings.Split(rowslice," "){
			var parent1 node
			var parent2 node
			if rownum-1<len(nodes) && rownum-1 >= 0 {
				if columnnum-1<len(nodes[rownum-1]) && columnnum-1 >= 0{
					parent1 = nodes[rownum-1][columnnum-1]
				}
				if columnnum<len(nodes[rownum-1]) && columnnum-1 >= 0{
					parent2 = nodes[rownum-1][columnnum]
				}
			}
			value,err := strconv.Atoi(value)
			fmt.Println(value)
			if err != nil{
				fmt.Println(err)
			}
			newnode := node{value,[]*node{&parent1,&parent2},[]*node{}}
			row = append(row, newnode)
			parent1.addChild([]*node{&newnode}) //is this wrong?  probably
			parent2.addChild([]*node{&newnode})
		}
		nodes = append(nodes,row)
	}
	return
}

func getHighestTotal(topnode node) (nodes []*node){
	if len(node.children) == 0{
		return 0
	} else {
		max := MinInt
		for _,i := node.children{
			max = intmax(getHighestTotal(i),max)
		}
	}
	return
}