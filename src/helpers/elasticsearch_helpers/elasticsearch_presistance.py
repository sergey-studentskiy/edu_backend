from datetime import datetime
from elasticsearch_dsl import connections, analyzer

connections.create_connection(hosts=['https://elastic:8VTylqWydBtHw9RmVEIZ52B6@i-o-optimized-deployment-75162b.es.eastus2.azure.elastic-cloud.com:9243'], timeout=20)


from elasticsearch_dsl import Document, Date, Nested, Boolean, \
    InnerDoc, Completion, Keyword, Text




class Post(Document):
    title = Text()
    title_suggest = Completion()
    created_at = Date()
    published = Boolean()



    class Index:
        name = 'blog'



    def save(self, **kwargs):
        self.created_at = datetime.now()
        return super().save(**kwargs)


Post(title='dafsd').save()

s = Post.search()

s = s.query('match', title='dafsd')


results = s.execute()


t = 2
