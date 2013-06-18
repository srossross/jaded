jaded
=====

#### hello.jd

```jade
// This is a standard jade
doctype jaded_app
jd:Application(layout="vertical", creationComplete="self.initApp()")
  jd:Python 
    :cdata
      def initApp(self):
          # says hello at the start, and asks for the user's name
          import 
          self.my_greeter = Greeter()
          mainTxt.text = myGreeter.say_hello()

  jd:TextArea(id="mainTxt", width=400)
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

