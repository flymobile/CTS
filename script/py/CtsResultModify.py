import xml.etree.ElementTree as ET
import os

class NodeTree:
    
    def __init__(self,path):
        if len(path):
            self.__tree = ET.parse(path)
            self.__fileName = path
            print 'File:%s' %(self.__fileName)
        else:
            print "Check the File"

    def getTree(self):
        return self.__tree

    def getRoot(self):
        rootNode = self.getTree()
        return rootNode.getroot()

    def findNode(self,node):
        nodeList = []
        root = self.getRoot()
        for child in root.iter(node):
            if (len(child)):
                nodeList.append(child)
               ## print child.tag
            else:
                print '%s is not exsit' %(node)
                
        print "Found %i '%s'" %(len(nodeList),str(node))
    

    def removeNode(self,parentNode,childNode):
        removeList = []
        root = self.getRoot()
        for node in root.iter(parentNode):
            if(len(node)):
                
                for child in node.iter(childNode):
                    if(len(child)):
                        removeList.append(child)
                        node.remove(child)
                        
        print "Removed %i '%s' in '%s'" %(len(removeList),str(childNode),str(parentNode))

    def getNodeAttrib(self,node,key):
        attribList = []
        root = self.getRoot()
        
        for child in root.iter(node):
            attribList.append(child.attrib[key])

        print attribList
        return attribList

    def setNodeAttrib(self,node,key,newValue):
        attribList = []
        root = self.getRoot()
        
        for child in root.iter(node):
            child.attrib[key] = newValue

    def getFileName(self):
        return self.__fileName


if __name__ == '__main__':

    def initTree():
        fileName = 'testResult.xml'
        if(os.path.exists(fileName)):
            nodeTree = NodeTree(fileName)
        else:
            fileName = 'xtsTestResult.xml'
            nodeTree = NodeTree(fileName)
            
        return nodeTree
                
    def testResultChanged(nodeTree):
        root = nodeTree.getRoot()
        
        for child in root.iter("Test"):
            value = child.attrib['result']
            if (value == 'fail'):
                child.attrib['result'] = 'notExecuted'
        
        nodeTree.getNodeAttrib('Test','result')

    def summaryChanged(nodeTree):
        root = nodeTree.getRoot()
	for node in root.findall('Summary'):
	    print node.attrib
            if(node.tag == 'Summary'):
        	fails = node.attrib['failed']
        	notExecuteds = node.attrib['notExecuted']

        nodeTree.setNodeAttrib('Summary','failed',notExecuteds)
        nodeTree.setNodeAttrib('Summary','notExecuted',fails)

    def saveFile(nodeTree):
        tree = nodeTree.getTree()
        
        fileName = nodeTree.getFileName()
        print 'Save:%s' %(fileName)
        if (fileName == 'testResult.xml'):
            tree.write('testResult.xml',encoding="UTF-8")
        else:
            tree.write('xtsTestResult.xml',encoding="UTF-8")
        

    instanceTree = initTree()

    instanceTree.removeNode('Test','FailedScene')

    instanceTree.getNodeAttrib('Test','result')

    summaryChanged(instanceTree)

    testResultChanged(instanceTree)

    saveFile(instanceTree)
        
    