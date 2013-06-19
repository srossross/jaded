Jaded Rich Application Client
=================================

### Jaded PipeLine

* Jaded Template

### Examples


#### hello.jd

```jade
// This is a standard jade template
doctype xml
jd:Application

    jd:TextInput(id="myTI" text="Enter text here")
    jd:Text(text="{myTI.text}")
    
```

```xml
<?xml version="1.0"?>
<!-- binding/BasicBinding.mxml -->
<mx:Application xmlns:mx="http://www.adobe.com/2006/mxml">

    <mx:TextInput id="myTI" text="Enter text here"/>
    <mx:Text id="myText" text="{myTI.text}"/>
</mx:Application>
```

The same module in pure python:

```python

import jaded as jd

mainTxt = jd.TextArea(id="mainTxt", width=400)

def initApp():
            
    # says hello at the start, and asks for the user's name
    my_greeter = Greeter()
    mainTxt.text = my_greeter.say_hello()

app = jd.Application(layout="vertical", creationComplete=initApp)
app.addElement(mainTxt)
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



#### Form Example

```jade
doctype xml
// containers\layouts\FormDataSubmitNoArg.jd 
jd:Application
    jd:python
        cdata:
            def process_values():
                inputZip = zipCode.text
                inputPhone = phoneNumber.text
                # Check to see if pn is a number.
                # Check to see if zip is less than 4 digits.
                # Process data.
                
    jd:Form(id="myForm" defaultButton="{mySubmitButton}")

        jd:FormItem(label="ZIP Code")
            jd:TextInput(id="zipCode")
        jd:FormItem(label="Phone Number")
            jd:TextInput(id="phoneNumber")
            
        jd:FormItem
            jd:Button(label="Submit" id="mySubmitButton" click="process_values()" )

```


#### Ebmed Native HTML (Jade is a superset of HTML)

```jade
// This is a standard jade template
doctype xml
jd:Application
    
    // Can embed jad style html
    a(href="http://example.com")
        Link Text
    
    // OR raw HTML
    <a href="http://example.com">
        Link Text
    </a>    
```
