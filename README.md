Jaded Rich Application Client
=================================

### Jaded PipeLine

* Jaded Template

### Hello world example

#### hello.jd

```jade
// This is a standard jade template
doctype xml
jd:Application

    jd:TextInput(id="myTI" text="Enter text here")
    jd:Text(text="{myTI.text}")
    
```

The same module can be written in pure python:

```python

import jaded as jd
import traty as ty

myTI = jd.TextInput(text="Enter text here")
myText = jd.TextArea(text="")

ty.events(myTI).text.on('change', lambda value: setattr(myText,'text', value))

app = jd.Application()
app.addElement(myTI)
app.addElement(myText)

```


### Data Binding

Data binding is the process of tying the data in one object to another object. 
It provides a convenient way to pass data between the different layers of the application.
Data binding requires a source property, a destination property, 
and a triggering event that indicates when to copy the data from the source 
to the destination. An object dispatches the triggering event when the source property changes.

Jaded provides specifies data binding with the curly braces `{ }` as in the above example `{myTI.text}` 

### Running A Jaded Application

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
