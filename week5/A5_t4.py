def askDimension(PPrompt) -> float:
   Feed = input("Insert {pprompt}: ")
   return Feed

#Width = askNumber("width")
#Height = askNumber("height")

def calcRectangleArea(PWidth, PHeight) -> float:
   print("")
   Area = PWidth * PHeight
   return float(Area) 
 #  PWidth = Area * PHeight
 #  return Sum





def main() -> None:
   print("program starting")
   Width = askDimension("width")
   Height = askDimension("height")
   Area = calcRectangleArea(Width,Height)
   print(f"Area is {Area}²")
   print("program ending.")

main()
