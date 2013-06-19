'''
Created on Jun 19, 2013

@author: sean
'''
from jinja2 import Environment, FileSystemLoader
from jinja2.utils import import_string
from argparse import ArgumentParser
from os.path import abspath, curdir
from lxml.etree import fromstring
from PySide import *
from PySide.QtGui import QWidget, QLayout
from PySide.QtGui import QApplication
import re

_biner_re = re.compile('^\{=(.*)\}$')
def isbinder(value):
    m = _biner_re.match(value)
    if m:
        return m.groups()[0]
    return 

def get_signal(qobj, attr):
    if hasattr(qobj, '%sChanged' % attr):
        return getattr(qobj, '%sChanged' % attr)
    return getattr(qobj, attr)


def get_slot(qobj, attr):
    if hasattr(qobj, 'set%s' % attr.title()):
        return getattr(qobj, 'set%s' % attr.title())
    return getattr(qobj, attr)


class AppGenerator(object):
    def __init__(self):
        self.glbls = {}
        self.imports = {}
        self.binders = []
        
    def connect(self):
        for qobj, binders in self.binders:
            for (attr, source) in binders:
                source, source_attr = source.rsplit('.')
                source_obj = eval(source, globals(), self.glbls)
                signal = get_signal(source_obj, source_attr)
                slot = get_slot(qobj, attr)
                signal.connect(slot)
    
    def add_bind(self, obj, bind):
        self.binders.append((obj, bind))
        
    def generic_visit(self, elem, cls, children):
        raise NotImplementedError(elem, cls.mro())
    
    def process_attrib(self, attrib):
        attrs = {key:eval(value) for key, value in attrib.items() if not isbinder(value)}
        data_binders = [(key, isbinder(value)) for key, value in attrib.items() if isbinder(value)]
        return attrs, data_binders 
    
    def instantiate(self, cls, elem):
        kwargs, data_binders = self.process_attrib(elem.attrib)
        widget = cls(**kwargs)
        if data_binders:
            self.add_bind(widget, data_binders)
        return widget
    
    def visit_QWidget(self, elem, cls, children):
        assert len(children) == 0
        widget = self.instantiate(cls, elem)
        return widget
        
    def visit_QLayout(self, elem, cls, children):
        layout = self.instantiate(cls, elem)
        for widget in children:
            assert isinstance(widget, QWidget), widget
            layout.addWidget(widget)
        return layout 
    
    def visit_QCoreApplication(self, elem, cls, children):
        instance = cls.instance()
        widget = None
        for child in children:
            if isinstance(child, QLayout):
                widget = QWidget()
                widget.setLayout(child)
            else:
                raise NotImplementedError(child)
        
        return widget
        
    def visit(self, elem):
        
        children = [self.visit(child) for child in elem.iterchildren()]
        
        cls_name = elem.xpath('local-name()')
        ns = elem.nsmap[elem.prefix]
        if ns not in self.imports:
            self.imports[ns] = import_string(ns)
        module = self.imports[ns]
        cls = getattr(module, cls_name)
        
        wid = elem.attrib.pop('id', None)

        for scls in cls.mro():
            method_name = 'visit_{0}'.format(scls.__name__)
            method = getattr(self, method_name, None) 
            if method: 
                result = method(elem, cls, children)
                break
        else:
            result = self.generic_visit(elem, cls, children)
            
        if wid:
            self.glbls[wid] = result
        return result

def generate_app(elem):
    appgen = AppGenerator()
    qobj = appgen.visit(elem)
    appgen.connect()
    return qobj


def main():
    
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('inputs', nargs=1)
    
    args = parser.parse_args()
    
    loader = FileSystemLoader(abspath(curdir))
    jinja_env = Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'],
                            loader=loader)

    template = jinja_env.get_or_select_template(args.inputs[0])
    elem = fromstring(template.render().encode('utf-8'))
    
    app = QApplication([])
    widget = generate_app(elem)
    
    widget.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
