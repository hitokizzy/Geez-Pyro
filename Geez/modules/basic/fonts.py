"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""


from geezlibs.geez import geez
from Geez.modules.basic.broadcast import get_arg
from Geez import cmds
from Geez.modules.basic import add_command_help


_font = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_font1 = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
_font2 = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
_font3 = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
_font4 = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
_font5 = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
_font6 = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
_font7 = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
_font8 = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ¹²³⁴⁵⁶⁷⁸⁹⁰\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font9 = "ᗩᗷᑕᗞᗴᖴᏀᕼᏆᒍᏦᏞᗰᑎᝪᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᏃᗩᗷᑕᗞᗴᖴᏀᕼᏆᒍᏦᏞᗰᑎᝪᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᏃ1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font10 = "ₐBCDₑFGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥWₓYZₐᵦ𝒸𝒹ₑ𝒻𝓰ₕᵢⱼₖₗₘₙₒₚᵩᵣₛₜᵤᵥ𝓌ₓᵧ𝓏₁₂₃₄₅₆₇₈₉₀\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font11 = "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font12 = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font13 = "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font14 = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
_font15 = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ０１２３４５６７８９！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［\\］＾＿‘｛｜｝～"


def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _font:
            new = new_font[_font.index(q)]
            text = text.replace(q, new)
    return text


@geez(["font"], cmds)
async def font_ubot(client, message):
    if not message.reply_to_message and not get_arg(message):
        return await message.reply("Balas Teks Dan Isi Nama Font!!!")
    font = get_arg(message)
    text = message.reply_to_message.text
    if not font:
        return await message.reply(f"<code>{font} Tidak ada dalam daftar font...</code>")
    if font == "1":
        meira = gen_font(text, _font1)
    elif font == "2":
        meira = gen_font(text, _font2)
    elif font == "3":
        meira = gen_font(text, _font3)
    elif font == "4":
        meira = gen_font(text, _font4)
    elif font == "5":
        meira = gen_font(text, _font5)
    elif font == "6":
        meira = gen_font(text, _font6)
    elif font == "7":
        meira = gen_font(text, _font7)
    elif font == "8":
        meira = gen_font(text, _font8)
    elif font == "9":
        meira = gen_font(text, _font9)
    elif font == "10":
        meira = gen_font(text, _font10)
    elif font == "11":
        meira = gen_font(text, _font11)
    elif font == "12":
        meira = gen_font(text, _font12)
    elif font == "13":
        meira = gen_font(text, _font13)
    elif font == "14":
        meira = gen_font(text, _font14)
    elif font == "15":
        meira = gen_font(text, _font15)
    await message.reply(meira)


@geez(["lf", "listfont"], cmds)
async def fonts_list(client, message):
    await message.reply(
        "<b>Daftar Fonts :</b>\n\n"
        "<b>• 1 -> ᴀʙᴄᴅ</b>\n"
        "<b>• 2 -> 𝚊𝚋𝚌𝚍</b>\n"
        "<b>• 3 -> 𝕒𝕓𝕔𝕕</b>\n"
        "<b>• 4 -> 🅐🅑🅒🅓</b>\n"
        "<b>• 5 -> ⓐⓑⓒⓓ</b>\n"
        "<b>• 6 -> 𝗮𝗯𝗰𝗱</b>\n"
        "<b>• 7 -> 𝙖𝙗𝙘𝙙</b>\n"
        "<b>• 8 -> ᴬᴮᶜᴰ</b>\n"
        "<b>• 9 -> ᗩᗷᑕᗞ</b>\n"
        "<b>• 10 -> ₐBCD</b>\n"
        "<b>• 11 -> 𝔄𝔅ℭ𝔇</b>\n"
        "<b>• 12 -> 𝕬𝕭𝕮𝕯</b>\n"
        "<b>• 13 -> 𝒜𝐵𝒞𝒟</b>\n"
        "<b>• 14 -> 𝓐𝓑𝓒𝓓</b>\n"
        "<b>• 15 -> ＡＢＣＤ</b>\n",
    )

add_command_help(
    "font",
    [
        [f"{cmds}font <reply ke pesan>", "merubah font pesan"],
        [f"{cmds}lf/{cmds}listfont", "melihat list font yg tersedia"],
    ],
)