import os
import mt_choice.zhihu.spider as zh_spider


def test_get_all_columns():
    result = zh_spider.get_all_columns()
    assert len(result) != 0


def test_get_pic_QA_from_article():
    article_url = 'https://zhuanlan.zhihu.com/p/158527476'
    first_png_url, qa_dict = zh_spider.get_pic_QA_from_article(article_url)
    assert first_png_url != ''
    assert qa_dict != {}


def test_get_all_articles():
    articles, qas = zh_spider.get_all_articles()
    for r in articles:
        print(r)

    for r in qas:
        print(r)


def test_flush_db():
    zh_spider.flush_db()
    assert os.path.exists(zh_spider.COLUMNS_FILE)
    assert os.path.exists(zh_spider.ARTICLES_FILE)
    assert os.path.exists(zh_spider.QAS_FILE)


def test_load_db():
    all_columns, all_articles, all_qas = zh_spider.load_db()
    assert len(all_columns) != 0
    assert len(all_articles) != 0
    assert len(all_qas) != 0

