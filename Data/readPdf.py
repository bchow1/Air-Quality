# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:30:49 2017
@author: bchow1
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


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

      
      pageObj = in_file_pdf.getPage(i)
      
      # Write each page to a separate pdf file
      pdfOut = PdfFileWriter()
      pdfOut.addPage(pageObj)
      out_file_pdf = os.path.join(outDir,"P"+str(i)+".pdf")
      #print("Page %d"%i)
      outputStream = file(out_file_pdf, "wb")
      pdfOut.write(outputStream)
      outputStream.close()
      
      # txtOut
      txtOut = open(os.path.join(outDir,"P"+str(i)+".txt"),"w")
      pageTxt = pageObj.extractText()
      txtOut.write(pageTxt)
      txtOut.close()
     