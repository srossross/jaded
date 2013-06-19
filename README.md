
Hello.jade
```jade

!!! xml

QtGui:QApplication(xmlns:QtGui="PySide.QtGui", xmlns:jd="jaded.utils")
    QtGui:QVBoxLayout
        
        QtGui:QLCDNumber(id="lcd", numDigits=2, display="{=slider.value}")
        QtGui:QSlider(id="slider", orientation="QtCore.Qt.Horizontal")
        

```


### Data Binding

Data binding is the process of tying the data in one object to another object. 
It provides a convenient way to pass data between the different layers of the application.
Data binding requires a source property, a destination property, 
and a triggering event that indicates when to copy the data from the source 
to the destination. An object dispatches the triggering event when the source property changes.

Jaded provides specifies data binding with the curly braces `{= }` as in the above example `{=slider.value}` 


```


```bash

# Run as a qt application
jaded hello.jade

```
