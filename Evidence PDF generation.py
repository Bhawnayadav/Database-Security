# -*- coding: utf-8 -*-
from reportlab.platypus import SimpleDocTemplate 
#from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, Spacer
from reportlab.platypus import Image
from reportlab.platypus import PageBreak
from reportlab.lib.units import mm, inch, cm
from  reportlab.platypus import TableStyle
from reportlab.lib import colors
import datetime
import csv
#from reportlab.lib import pdfencrypt
#enc=pdfencrypt.StandardEncryption("encryptionkey",canPrint=0)

pagesize = (440 * mm, 460* mm)
my_doc = SimpleDocTemplate(
    "Log_Report.pdf",
    pagesize=pagesize,
    showBoundary=1,
    topMargin=0.5*inch,
    leftMargin=0.5*cm,
    rightMargin=0.5*cm,
    bottomMargin=0.5*inch,
    pagecolor = 'Black'
)  

sample_style_sheet = getSampleStyleSheet()  
flowables = [] 
title_style = sample_style_sheet ['Heading1']
title_style.alignment = 1
title_style.fontsize=40
title_style.firstLineIndent = 24 
im = Image("alert.jpg")
im.hAlign = 'CENTER' 
flowables.append(im)
#title_style.listAttrs()
styles = getSampleStyleSheet()
styleNormal = styles['Heading3']
styleNormal.fontsize=25 
paragraph_1 = Paragraph("<I><U>Details</U></I>", title_style )
flowables.append(Spacer(inch, .50 * inch))
flowables.append(paragraph_1)
flowables.append(Spacer(inch, .25 * inch)) 
flowables.append(Spacer(inch, .15 * inch)) 

line1 = '<font color=white>........</font>-------------------------------------------------------------------------------------------------------------------'
line2 = '<font color=white>........</font><font size=15><font color="red">* An unauthorised attempt to access data has been recorded at timestamp</font></font>: {}'.format(datetime.datetime.now().strftime("%d-%m-%y"))
line3 = '<font color=white>........</font><font size =15><font color="red">* More deatils of the session are recorded with the report.</font></font>'
line4 = '<font color=white>........</font>-------------------------------------------------------------------------------------------------------------------'
 
flowables.append(Paragraph(line1, styleNormal))
flowables.append(Paragraph(line2, styleNormal))
flowables.append(Paragraph(line3, styleNormal))
flowables.append(Paragraph(line4, styleNormal))
 


flowables.append(Spacer(inch, .75 * inch))
paragraph_2 = Paragraph("<b><i><U><font color='blue'>Log details are shown below:</font></U></i></b>", title_style )
flowables.append(paragraph_2) 
flowables.append(Spacer(inch, .50 * inch))

list1=[] 
with open('Result.csv', mode='r') as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',') 
    for row in csv_reader1: 
        list1.append(row)

all_cells = [(0, 0), (-1, -1)]
header = [(0, 0), (-1, 0)]
column0 = [(0, 0), (0, -1)]
column1 = [(1, 0), (1, -1)]

table_style = TableStyle([
    ('VALIGN', all_cells[0], all_cells[1], 'TOP'),
    ('LINEBELOW', header[0], header[1], 1, colors.black),
    ('TEXTCOLOR',header[0], header[1],colors.blue),
    ('VALIGN',header[0], header[1], 'MIDDLE'),
    ('FONTSIZE',header[0], header[1], 13),
    ('ALIGN', column0[0], column0[1], 'LEFT'),
    ('FONTSIZE',column0[0], column0[1], 12),
    ('ALIGN', column1[0], column1[1], 'LEFT'),
    ('FONTSIZE',column1[0], column1[1], 12),
]) 
table_style.fontsize=70

# PDF Table - Column Widths
colWidths = [
    20 * cm,  # Column 0
    10 * cm,  # Column 1
] 

t3 = Table(list1, colWidths=colWidths)
t3.setStyle(table_style) 
flowables.append(t3)   

flowables.append(PageBreak())
flowables.append(Spacer(inch, .75 * inch)) 

my_doc.build(flowables) 
print('\n')
print("--------PDF GENERATED--------")
print('\n')

