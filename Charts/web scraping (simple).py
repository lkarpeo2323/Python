import metadata_parser

url = 'https://portfolio-karpel-website.netlify.app/index.html'
page = metadata_parser.MetadataParser(url)
print(page.metadata)
