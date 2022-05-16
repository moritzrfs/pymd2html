import markdown
import sys
import os

def validate_args():
    args = sys.argv[1:]
    if len(args):
        if os.path.basename(args[0]).endswith('.md'):
            return True
    else:
        return False

def to_html(filename):
    if validate_args(): 
        path = os.path.basename(filename)
        with open(path, 'r') as md_file:
            text = md_file.read()
            html = markdown.markdown(text)
        with open ('out.html', 'w') as html_file:            
            with open('template.html', 'r') as template:
                content = template.read()
                content = content.replace('content', html)
            html_file.write(content)
            with open ('log.log', 'w') as log_file:
                log_file.write('Success')        
    else:
        with open ('log.log', 'w') as file:
            logs = sys.argv[1:]
            file.write('Error while reading args')
            for l in logs:
                file.write(l+'\n')

to_html(sys.argv[1])