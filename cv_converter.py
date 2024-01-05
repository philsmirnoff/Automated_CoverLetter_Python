from docxtpl import DocxTemplate
import datetime

# Get Inputs from User
today_date = datetime.datetime.today().strftime('%B %d, %Y').replace(" 0", " ")

company_name = input("Enter name of the Company: ")
position_name = input("Enter name of the Position: ")
specific_goal = input("Enter specific goal the Company is committed to that aligns with your values: ")
specific_aspect = input("Enter specific aspect of the Company that shares your passion for: ")

context = {
    'today_date': today_date,
    'company_name': company_name,
    'position_name': position_name,
    'specific_goal': specific_goal,
    'specific_aspect': specific_aspect
}

# Opening our template file
doc = DocxTemplate("CV_Template.docx")

# Load this document object into the docx
doc.render(context)

# Save the document
doc.save('CV_'+company_name+'_'+position_name+'.docx')
