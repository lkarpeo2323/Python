import metadata_parser

url = 'https://portfolio-karpel-website.netlify.app/academics'
page = metadata_parser.MetadataParser(url)
print(page.metadata)
