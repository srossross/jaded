Jaded Rich Application Client
=================================

### Examples

#### hello.jd

```jade
// This is a standard jade template
doctype xml
jd:Application(layout="vertical", creationComplete="self.initApp()")
    jd:python 
      :cdata
        def initApp(self):
            # says hello at the start, and asks for the user's name
            
            self.my_greeter = Greeter()
            self.mainTxt.text = self.my_greeter.say_hello()

    jd:TextArea(id="mainTxt", width=400)
```

The same module in pure python:

```python

import jaded as jd

class App(jd.Application):

    def __init__(layout="vertical"):
        self.creationComplete(self.initApp)
        self.mainTxt = MainTxt(width=400)
    
    def initApp(self):
        
        self.mainTxt = jd.TextArea(width=400)
        self.add_child(self.mainTxt)
        
        # says hello at the start, and asks for the user's name
        self.my_greeter = Greeter()
        self.mainTxt.text = self.my_greeter.say_hello()


```

#### command line

```bash
# Serve as a web application
jaded serve hello.jd --port 8080

# Run as a qt application
jaded run hello.jd

# Build Bundle for sharing (probably using conda)
jaded bundle hello.jd

```

