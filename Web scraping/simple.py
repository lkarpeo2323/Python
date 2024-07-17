import metadata_parser

url = 'https://portfolio-karpel-website.netlify.app/index.html'
page = metadata_parser.MetadataParser(url)


print('Title:' ,page.get_metadatas('title'))

print('Meta Description:', page.get_metadatas('description'))
