package main
import "fmt"
func answer(x int) int {
  var y int;
  fmt.Scanf("%d", &y); // inputy
  var temp int;
  temp = 0
  if (y >= 0) {// accept not negative integer only
    temp = y*y;
  }
  if (x > 0) {// when x is still larger than 0
    temp += answer(x-1);
  }
  return temp;
}
func challenge (n int) {
  var x int;
  fmt.Scanf("%d", &x);
  fmt.Println(answer(x-1));
  if (n != 0) {
    challenge(n-1);
  }
}
func main() {
  var n int;
  fmt.Scanf("%d", &n);
  challenge(n-1);
}