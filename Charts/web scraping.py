import metadata_parser

url = 'https://portfolio-karpel-website.netlify.app/academics'
page = metadata_parser.MetadataParser(url)
print(page.metadata)


print(page.get_metadatas('title')) #get the title
