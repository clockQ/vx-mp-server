import mt_msg.reply as mrp


def test_process_text_msg():
    to_user_name = 'to_user_name'
    from_user_name = 'from_user_name'
    content = 'content'

    text_msg = mrp.TextMsg(to_user_name, from_user_name, content).send()
    assert text_msg != "success"


def test_process_image_msg():
    to_user_name = 'to_user_name'
    from_user_name = 'from_user_name'
    media_id = 'media_id'

    image_msg = mrp.ImageMsg(to_user_name, from_user_name, media_id).send()
    assert image_msg != "success"


def test_process_news_msg():
    news_msg = mrp.NewsMsg('to_user_name', 'from_user_name', [
        {
            'title': 'title',
            'desc': 'desc',
            'pic_url': 'pic_url',
            'url': 'url',
        },
        {
            'title': 'title2',
            'desc': 'desc2',
            'pic_url': 'pic_url2',
            'url': 'url2',
        },
    ]).send()
    assert news_msg != "success"
