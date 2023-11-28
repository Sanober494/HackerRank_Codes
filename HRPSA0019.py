#Solution for "Designer PDF Viewer" 
#Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure


def designerPdfViewer(h, word):
    index=0
    NewHeight=0
    for l in word:
        index=ord(l)-ord("a")
            
        if h[index] > NewHeight: 
            NewHeight=h[index]
            
    print(NewHeight*len(word))    

height=input()
Height=list(map(int,height.split()))
letter=input()
designerPdfViewer(Height,letter)
