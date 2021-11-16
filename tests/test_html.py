import pyweb


# Initializing HTML object
html = pyweb.HTML(title="PyWeb Test")
body = html.content

nav = body.inside() # Creating an element withon body
nav.text("This is the navigation bar\n", heading=3) # Adding <h3> text inside the element

buttons = []
for i in range(6):
    buttons.append(nav.inside(type='button')) # Creating buttons inside previously created element
buttons[1].text("Button 2") # Adding text inside 2nd button

body = body.inside() # Creating another element within body
body.text("\n") # Inserting <br>
para1 = body.inside(type='span') # Adding some <span> tags for text
para2 = body.inside(type='span')
para1.text("Blah blah this is para 1") # Adding texts
para2.text("Blah blah this is para 2")

html.render_to_file("test.html") # Rendering generated HTML to a file