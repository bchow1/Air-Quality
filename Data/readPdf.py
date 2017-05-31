# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:30:49 2017

@author: sid
"""
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


# Main Program
if __name__ == '__main__':
  os.chdir('d:\\SCIPUFF\\runs\\PortonDown\\Docs')
  print os.getcwd()
  pdfFile = 'picknett_1981_dense_gas_dispersion_slopes.pdf'
  
  dirName = pdfFile.replace('.pdf','')
  if not os.path.exists(dirName):
      os.makedirs(dirName)
  
  in_file_pdf = PdfFileReader(file(pdfFile, "rb"))
  print in_file_pdf.numPages
  
  for i in xrange(in_file_pdf.numPages):
      output = PdfFileWriter()
      output.addPage(in_file_pdf.getPage(i))
      out_file_pdf = "P" + str(i) + ".pdf" 
      out_file = os.path.join(dirName,out_file_pdf)
      print("Saving " + out_file)
      outputStream = file(out_file, "wb")
      output.write(outputStream)
      outputStream.close()