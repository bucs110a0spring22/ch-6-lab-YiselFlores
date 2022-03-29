import turtle 
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count
                      # the last print is 1

def drawgraph(upperbound):
  bonnie = turtle.Turtle()
  clyde = turtle.Turtle()
  window = turtle.Screen()

  window.setworldcoordinates (0,0,10, 10)

  max_so_far = 0
  bonnie.up()
  bonnie.goto(0,10)
  
  for i in range(1,upperbound+110):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far = result
    bonnie.goto(0,max_so_far)
    maximum = 'maximum', i,result
    bonnie.clear()
    bonnie.write(maximum)

    window.setworldcoordinates (0,0,i+10, max_so_far+10)

    clyde.down()
    clyde.goto(i,result)
  
  window.exitonclick()
  
  
def main():
  upperbound = int(input("Input a positive number:"))
  if upperbound <= 0:
     exit()
  start = range(1, upperbound)
  for i in start:
    print("Initial Number: " + str(i))
    print(seq3np1(i))

  drawgraph(upperbound)  
  print(seq3np1(3))
main()

