#

import turtle as tt

def h1():
   tt.forward(30)

def h2():
   tt.left(45)

def h3():
   tt.right(45)

def h4():
    tt.bye()                      

tt.onkey(h1, "Up")
tt.onkey(h2, "Left")
tt.onkey(h3, "Right")
tt.onkey(h4, "q")

tt.listen()
tt.mainloop()