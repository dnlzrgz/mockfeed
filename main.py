from random import randint
from fastapi import FastAPI, Response
from faker import Faker
from fastapi.responses import HTMLResponse

fake = Faker()
app = FastAPI()


def generate_random_feed(site: str, num_posts=5):
    feed = f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>{fake.company()}</title>
        <link>{site}</link>
        <description>{fake.catch_phrase()}</description>
        <atom:link href="{site}/rss/" rel="self"/>
        <lastBuildDate>{fake.date_time_this_year().strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>
    """

    for _ in range(num_posts):
        slug = fake.slug()
        pub_date = fake.date_time_this_year()
        feed += f"""
        <item>
            <title>{fake.sentence(nb_words=6)}</title>
            <link>http://localhost:8000/{site}/blog/{slug}</link>
            <description><![CDATA[{fake.paragraph(nb_sentences=2)}]]></description>
            <pubDate>{pub_date}</pubDate>
            <guid>/{site}/blog/{slug}</guid>
        </item>
        """

    feed += """
    </channel>
</rss>
    """

    return feed


@app.get("/{site}/rss/")
def get_rss_feed(site: str):
    rss_feed = generate_random_feed(site, randint(3, 9))
    return Response(content=rss_feed, media_type="application/xml")


@app.get("/{site}/blog/{slug}", response_class=HTMLResponse)
def get_blog_post(site: str, slug: str):
    html_content = "<p></p>".join(fake.paragraphs(nb=randint(5, 9)))

    return f"""<html>
        <head>
            <title>{fake.sentence(nb_words=5)} - {site}</title>
            <meta charset="utf-8">
        </head>
        <body>
        <h1>{fake.catch_phrase()}</h1>
        <div>{html_content}</div>
        </body>
    </html>
    """
