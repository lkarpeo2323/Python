import metadata_parser

url = 'https://portfolio-karpel-website.netlify.app/index.html'
page = metadata_parser.MetadataParser(url)


print(page.metadata) #All the data

print('Title:' ,page.get_metadatas('title')) #title

print('Meta Description:', page.get_metadatas('description')) #description

print('Image:', page.get_metadatas('image')) #image
