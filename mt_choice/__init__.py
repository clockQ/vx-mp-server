from fuzzywuzzy import process
import mt_msg.receive as mrc
from mt_choice.purpose import all_purpose, unknow_purpose, permission_denied_purpose


def __get_purpose_by_text(identity, text):
    # 获得所有功能中最接近的一个
    extract_result = process.extractOne(text, list(all_purpose.keys()))
    # 如果字符匹配结果小于 %50，则放弃找到的可能行为
    if extract_result[1] < 50:
        return unknow_purpose

    extract_purpose = all_purpose[extract_result[0]]
    purpose_obj = extract_purpose[0]
    purpose_level_lst = extract_purpose[1]

    # TODO 可以改成 set 的 issubset() 或 issuperset() 检查权限
    purpose_require_level = max([role.value for role in purpose_level_lst])
    fans_level = max([role.value for role in identity.groups])
    if fans_level < purpose_require_level:
        return permission_denied_purpose

    return purpose_obj


def __get_purpose_by_image(identity, pic_url, media_id):
    return unknow_purpose


def get_purpose_by_msg(identity, msg: mrc.Msg):
    if msg.MsgType == 'text':
        purpose_func = __get_purpose_by_text(identity, msg.Content)
    elif msg.MsgType == 'voice':
        purpose_func = __get_purpose_by_text(identity, msg.Recognition)
    elif msg.MsgType == 'image':
        purpose_func = __get_purpose_by_image(identity, msg.PicUrl, msg.MediaId)
    else:
        purpose_func = unknow_purpose

    return purpose_func
