import turtle

def draw_tree(branchLen,t):
    """
    Figure out the tree pattern, then display the recursion tree.
    You may have to play/tune with angles/lengths to draw a pretty tree.

    :param branchLen: Int -- Length of this branch. Should reduce every recursion. Starting length is 100.
    :param t: turtle.Turtle -- Instance of turtle module. We can call turtle functions on this parameter.

    :return: Nothing to return
    """
    if branchLen < 60:
        return
    else:
        t.forward(branchLen)
        t.left(20)
        draw_tree(branchLen-10,t)
        t.right(40)
        draw_tree(branchLen-10,t)
        t.left(20)
        t.backward(branchLen)
        
        
        
        
    

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.backward(100)
    t.color("green")
    draw_tree(100,t)    # Drawing tree with branchLen = 100
    myWin.exitonclick()

main()
