// You can edit this code!
// Click here and start typing.
// http://hdechallenge.appspot.com/challenge?email=b7615199%40hotmail.com&key=9160760b19bc9fe7dd746d2d53e23e86640f1d71
package main

import "fmt"

func sum(n int) int {
	if n == 0 {
	    return 0
	}
	var x int
	fmt.Scanf("%d", &x)
	if x < 0 {
	    return sum(n - 1)
	} else {
	    return sum(n - 1) + x * x
	}
} 
func process(testcase int) {
	if testcase == 0 {
	    return
	}
	var n int
	fmt.Scanf("%d", &n)
	fmt.Printf("%d\n", sum(n))
	process(testcase-1)
}
func main() {
	var testcase int
	fmt.Scanf("%d", &testcase)
	process(testcase)
}