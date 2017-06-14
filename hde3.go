// Package main fulfulls the requirement by HDE challenge 003.
// * Calculate squred sum of data from standard input.
// * No `for` statement is allowed.
package main

import "fmt"

// isValidVal test the input value for specified condition, in
// this case, only values that are greater then 0 are valid.
func isValidVal(val int) bool {
    return (val > 0)
}

// readInt is a wrapper function for the fmt.Scanf input,
// which contains error checking and validate the acquired
// input from user.
func readInt() (bool, int) {
    var i int
    _, err := fmt.Scanf("%d", &i)
    if err != nil {
        fmt.Println(err)
        return false, 0
    } else {
        return isValidVal(i), i
    }
}

// calcSqures is the core function, using recursive to eliminate
// the need of `for` statement.
func calcSquares(n int) int {
    if n > 0 {
        valid, i := readInt()
        if !valid {
            i = 0
        }
        return calcSquares(n-1) + i*i
    }
    return 0
}

// runCases is the parent function that called calcSquares, due
// to the fact that there might me multiple cases at hand.
// Recursive style is used as well, since `for` statement isn't
// allowed here.
func runCases(n int) {
    if (n > 0) {
        _, cnt := readInt()
        result := calcSquares(cnt)
        fmt.Println(result)
        runCases(n-1)
    }
}

// main calls runCases to perform the task. Invalid input won't
// be dealt with here.
func main() {
    _, cases := readInt()
    runCases(cases)
}