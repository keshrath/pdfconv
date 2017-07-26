# -*- coding: utf-8 -*-

######################################################################################
# 
#    Copyright (C) 2017 Mathias Markl
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#######################################################################################

import os
import unittest
import pdfconv

from contextlib import closing
 
current_directory = os.path.dirname(__file__) 

class TestConverter(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_convert_docx(self):
        input_path = os.path.join(current_directory, 'data/input_docx.docx')
        with closing(open(input_path, 'rb')) as file:
            self.assertTrue(pdfconv.converter.convert_binary2pdf(file.read(), None, "input_docx.docx"))
            
    def test_convert_pptx(self):
        input_path = os.path.join(current_directory, 'data/input_pptx.pptx')
        with closing(open(input_path, 'rb')) as file:
            self.assertTrue(pdfconv.converter.convert_binary2pdf(file.read(), None, "input_pptx.pptx"))    
            
    def test_convert_xlsx(self):
        input_path = os.path.join(current_directory, 'data/input_xlsx.xlsx')
        with closing(open(input_path, 'rb')) as file:
            self.assertTrue(pdfconv.converter.convert_binary2pdf(file.read(), None, "input_xlsx.xlsx"))  
        
    def test_convert_document2pdf_odt(self):
        input_path = os.path.join(current_directory, 'data/input_odt.odt')
        output_path = os.path.join(current_directory, 'data/input_odt.pdf')
        pdfconv.converter.convert_document2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
    
    def test_convert_document2pdf_doc(self):
        input_path = os.path.join(current_directory, 'data/input_doc.doc')
        output_path = os.path.join(current_directory, 'data/input_doc.pdf')
        pdfconv.converter.convert_document2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)

    def test_convert_document2pdf_docx(self):
        input_path = os.path.join(current_directory, 'data/input_docx.docx')
        output_path = os.path.join(current_directory, 'data/input_docx.pdf')
        pdfconv.converter.convert_document2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
        
    def test_convert_presentation2pdf_odp(self):
        input_path = os.path.join(current_directory, 'data/input_odp.odp')
        output_path = os.path.join(current_directory, 'data/input_odp.pdf')
        pdfconv.converter.convert_presentation2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
    
    def test_convert_presentation2pdf_ppt(self):
        input_path = os.path.join(current_directory, 'data/input_ppt.ppt')
        output_path = os.path.join(current_directory, 'data/input_ppt.pdf')
        pdfconv.converter.convert_presentation2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)

    def test_convert_presentation2pdf_pptx(self):
        input_path = os.path.join(current_directory, 'data/input_pptx.pptx')
        output_path = os.path.join(current_directory, 'data/input_pptx.pdf')
        pdfconv.converter.convert_presentation2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
       
    def test_convert_presentation2pdf_ods(self):
        input_path = os.path.join(current_directory, 'data/input_ods.ods')
        output_path = os.path.join(current_directory, 'data/input_ods.pdf')
        pdfconv.converter.convert_spreadsheet2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
    
    def test_convert_presentation2pdf_xls(self):
        input_path = os.path.join(current_directory, 'data/input_xls.xls')
        output_path = os.path.join(current_directory, 'data/input_xls.pdf')
        pdfconv.converter.convert_spreadsheet2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)

    def test_convert_presentation2pdf_xlsx(self):
        input_path = os.path.join(current_directory, 'data/input_xlsx.xlsx')
        output_path = os.path.join(current_directory, 'data/input_xlsx.pdf')
        pdfconv.converter.convert_spreadsheet2pdf(input_path, output_path)
        self.assertTrue(os.path.isfile(output_path))
        os.remove(output_path)
 
if __name__ == '__main__':
    unittest.main()