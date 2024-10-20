from nonebot.plugin import on_regex, on_command
from nonebot.params import RegexGroup
from nonebot.adapters import Event, Message
from nonebot.rule import to_me, Rule

from nonebot import require

require("nonebot_plugin_alconna")

from nonebot_plugin_alconna import UniMessage, Reply, UniMsg, Text
from .fish_audio_api import fish_audio_api, ChunkLength
from .fish_speech_api import fish_speech_api
from .exception import APIException
from .config import config, Config
import contextlib


is_online = config.tts_is_online

chunk_length_map = {
    "normal": ChunkLength.NORMAL,
    "short": ChunkLength.SHORT,
    "long": ChunkLength.LONG
}

chunk_length = chunk_length_map.get(config.tts_chunk_length, ChunkLength.NORMAL)


with contextlib.suppress(Exception):
    from nonebot.plugin import PluginMetadata, inherit_supported_adapters

    __plugin_meta__ = PluginMetadata(
        name="FishSpeechTTS",
        description="一个插件,通过调用在线或本地api发送TTS语音",
        usage="发送:[发音人]说[文本]即可发送TTS语音",
        homepage="https://github.com/Cvandia/nonebot-plugin-game-torrent",
        config=Config,
        type="application",
        supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
        extra={"author": "Cvandia", "email": "1141538825@qq.com"},
    )


def check_is_to_me() -> Rule | None:
    if config.tts_is_to_me:
        return to_me()
    else:
        return None


tts_handler = on_regex(r"(.+)说([\s\S]*)", rule=check_is_to_me(), block=False)
speaker_list = on_command("语音列表", block=False)
balance = on_command("语音余额", block=False)


@tts_handler.handle()
async def tts_handle(message: UniMsg, match: tuple = RegexGroup()):
    if message.has(Reply):
        front_reply = message[Reply, 0].msg
        if isinstance(front_reply, Message):
            text = front_reply.extract_plain_text()
        elif isinstance(front_reply, str):
            text = front_reply
        else:
            text = str(front_reply)
        reply_msg = message[Text, 0].text
        speaker = reply_msg.split("说", 1)[0]
    else:
        if not match[1]:
            await tts_handler.finish()
        text = match[1]
        speaker = match[0]

    try:
        if is_online:
            await tts_handler.send("正在通过在线api合成语音, 请稍等")
            audio = await fish_audio_api.generate_tts(text, speaker, chunk_length)
            await UniMessage.voice(raw=audio).finish()
        else:
            await tts_handler.send("正在通过本地api合成语音, 请稍等")
            request = await fish_speech_api.generate_servettsrequest(
                text, speaker, chunk_length
            )
            audio = await fish_speech_api.generate_tts(request)
            await UniMessage.voice(raw=audio).finish()
    except (APIException, FileNotFoundError, ValueError, NotADirectoryError) as e:
        await tts_handler.finish(str(e))


@speaker_list.handle()
async def speaker_list_handle(event: Event):
    try:
        if is_online:
            await speaker_list.send("具体见官网:https://fish.audio/zh-CN/")
        else:
            await speaker_list.send("正在获取本地发音人列表, 请稍等")
            speakers = fish_speech_api.get_speaker_list()
            await speaker_list.send("发音人列表: " + ", ".join(speakers))
    except APIException as e:
        await speaker_list.finish(str(e))


@balance.handle()
async def balance_handle(event: Event):
    try:
        if is_online:
            await balance.send("正在获取在线语音余额, 请稍等")
            balance_float = await fish_audio_api.get_balance()
            await balance.finish(f"语音余额为: {balance_float}")
        else:
            await balance.finish("本地api无法获取余额")
    except APIException as e:
        await balance.finish(str(e))
