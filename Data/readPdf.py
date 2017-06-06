# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:30:49 2017
@author: bchow1
"""

import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
#from wand.image import Image
import PythonMagick
from PythonMagick import Image

os.environ['MAGICK_HOME'] = "C:\Program Files\ImageMagick-7.0.5-Q16"

img = Image()
img.density('300')
bg_colour = "#ffffff"

# Main Program
if __name__ == '__main__':
    os.chdir('d:\\SCIPUFF\\runs\\PortonDown\\Docs')
    print os.getcwd()
      
    pdfFile = 'picknett_1981_dense_gas_dispersion_slopes.pdf'
     
    outDir = pdfFile.replace('.pdf','')
    if not os.path.exists(outDir):
        os.makedirs(outDir)
      
    in_file_pdf = PdfFileReader(file(pdfFile, "rb"))
    print in_file_pdf.numPages
  
    # Loop through the pages in the pdf file
    for i in xrange(in_file_pdf.numPages):

        out_file_pdf = os.path.join(outDir,"P"+str(i)+".pdf")
        out_file_jpg = out_file_pdf.replace(".pdf", ".jpg")
        
        if not os.path.exists(out_file_pdf):
            
            # Read page i from pdfFile
            pageObj = in_file_pdf.getPage(i)
            pdfOut = PdfFileWriter()
            pdfOut.addPage(pageObj)
            print("Page %d"%i)
            
            # Write page i to a separate pdf file
            outputStream = file(out_file_pdf, "wb")
            pdfOut.write(outputStream)
            outputStream.close()
     
        if not os.path.exists(out_file_jpg):
            
            
            img.read(out_file_pdf)
            size = "%sx%s" % (img.columns(), img.rows())
            
            output_img = Image(size, bg_colour)
            output_img.type = img.type
            output_img.composite(img, 0, 0, PythonMagick.CompositeOperator.SrcOverCompositeOp)
            output_img.resize(str(img.rows()))
            output_img.magick('JPG')
            output_img.quality(75)
            output_img.write(out_file_jpg)
            print("Save page %d to %s"%(i,out_file_jpg))

