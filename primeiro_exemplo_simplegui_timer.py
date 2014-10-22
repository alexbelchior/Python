# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
  #Função responsável por incrementar a variável counter
def increment():
    global counter
    counter = counter + 1
    
# Define event handler functions
  #Função responsável por incrementar a variável counter de acordo com o tempo estabelecido
def tick():
    increment()
    print counter
    
  #Função responsável por zerar a variável counter
def buttonpress():
    global counter
    counter = 0
    
# Create a frame
frame = simplegui.create_frame("SimpleGUI Frame Teste", 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Clique aqui", buttonpress)

# Start frame and timers
frame.start()
timer.start()
