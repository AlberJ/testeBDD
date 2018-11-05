from faker import Faker
from blog.models import Post

fake = Faker()

def seed(loop=30, overide=False):
    if overide:
        Post.objects.all().delete()
    
    for i in range(loop):
        ftitle = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        ftext = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        fcreated = fake.date_object(end_datetime=None)
        fpublished = fake.date_object(end_datetime=None)

        Post.objects.create(
            title = ftitle,
            text = ftext,
            created_date = fcreated,
            published_date = fpublished
        )
