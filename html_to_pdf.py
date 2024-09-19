import pdfkit

path_to_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

input_html = 'index.html'
output_pdf = 'Koorosh_Komeili_Zadeh_CV.pdf'

options = {
    'page-size': 'A4',
    'margin-top': '10mm',
    'margin-right': '10mm',
    'margin-bottom': '10mm',
    'margin-left': '10mm',
    'encoding': 'UTF-8',
    'enable-local-file-access': None,
    'no-outline': None,
    'print-media-type': None
}

pdfkit.from_file(input_html, output_pdf, configuration=config, options=options)

print(f'PDF generated: {output_pdf}')