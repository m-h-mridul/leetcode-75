# using go lang to solve this problems
# import (
#     "fmt"
# )
# func pairSum(head *ListNode) int {
#     var value []int
#     var ans int=0
#     var i int =0
#     for head!=nil{
#       value = append(value, head.Val)
#       i++
#       head=head.Next
#     }
#     end:=i-1
#     for start:=0;start<i/2;start++{
#         addvalue:=value[end]+value[start]
#         ans=max(ans,addvalue)
#         end--
#         //fmt.Println("ans ",ans)
#     }
     
# return ans
# } 

# func max(a, b int) int {
#     if a > b {
#         return a
#     }
#     return b