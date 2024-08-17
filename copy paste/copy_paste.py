# Pyperclip is a cross-platform Python module for copy and paste clipboard functions.

import pyperclip as pc 
  
text1 = "Apple 🍎"
pc.copy(text1)  
text2 = pc.paste()  
print(text2) 
