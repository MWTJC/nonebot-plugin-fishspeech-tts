<div align="center">

# nonebot-plugin-fishspeech-tts

<a href="https://v2.nonebot.dev/store"><img src="https://count.getloli.com/get/@nonebot-plugin-fishspeech-tts?theme=asoul"></a>

_⭐基于Nonebot2的调用在线[fish-audio](https://fish.audio/zh-CN/)或离线[fish-speech](https://github.com/fishaudio/fish-speech) api⭐_
_⭐文本生成语音`tts`插件⭐_


</div>

<div align="center">
<a href="https://www.python.org/downloads/release/python-390/"><img src="https://img.shields.io/badge/python-3.10+-blue"></a>  <a href=""><img src="https://img.shields.io/badge/QQ-1141538825-yellow"></a> <a href="https://github.com/Cvandia/nonebot-plugin-game-torrent/blob/main/LICENCE"><img src="https://img.shields.io/badge/license-MIT-blue"></a> <a href="https://v2.nonebot.dev/"><img src="https://img.shields.io/badge/Nonebot2-2.2.0+-red"></a>
</div>


## ⭐ 介绍

仅需一条5秒语音素材，就可~~完美~~优秀克隆素材本音呐

## 📜 免责声明

> [!note]
> 本插件仅供**学习**和**研究**使用，使用者需自行承担使用插件的风险。作者不对插件的使用造成的任何损失或问题负责。请合理使用插件，**遵守相关法律法规。**
使用**本插件即表示您已阅读并同意遵守以上免责声明**。如果您不同意或无法遵守以上声明，请不要使用本插件。


## 💿 安装

<details>
<summary>安装</summary>

`pipx` 安装

```
pipx install nonebot-plugin-fishspeech-tts -U
```
> [!note] 在nonebot的pyproject.toml中的plugins = ["xxx"]添加此插件

`nb-cli`安装
```
nb plugin install nonebot-plugin-fishspeech-tts -U
```

`git clone`安装(不推荐)

- 命令窗口`cmd`下运行
```bash
git clone https://github.com/Cvandia/nonebot-plugin-fishspeech-tts
```
- 在窗口运行处
将文件夹`nonebot-plugin-fishspeech-tts`复制到bot根目录下的`src/plugins`(或创建bot时的其他名称`xxx/plugins`)

 
 </details>
 
 <details>
 <summary>注意</summary>
 
 推荐镜像站下载
  
 清华源```https://pypi.tuna.tsinghua.edu.cn/simple```
 
 阿里源```https://mirrors.aliyun.com/pypi/simple/```

</details>

## ⚙️ 配置

**在env.中添加以下配置**

| 配置 | 类型 |必填项| 默认值 | 说明 |
|:-----:|:----:|:----:|:---:|:----:|
|tts_is_online|bool|是|True|是否使用云端api|
|tts_is_to_me|bool|是|True|是否需要at触发(防止误触)|
|online_authorization|str|看需求|None|fish-audio 后端api，详见[链接](https://fish.audio/zh-CN/go-api/api-keys/)||
|tts_api_url|str|看需求|"http://127.0.0.1:8080"|离线或自定义api地址
|tts_audio_path|str|看需求|"./data/参考音频"|合成角色语音路劲|

## ⭐ 使用

> [!note]
> 请注意你的 `COMMAND_START` 以及上述配置项。

### 指令：

| 指令 | 需要@ | 范围 | 说明 |权限|
|:---:|:---:|:---:|:---:|:---:|
|xxx说xxx|根据配置|all|tts语音生成|all|
|语音列表|否|all|获取所有角色列表|all|
|语音余额|否|all|查询api余额|all|

## 🌙 未来
 - 暂无规划

<center>喜欢记得点个star⭐</center>

## 💝 特别鸣谢

- [x] [nonebot2](https://github.com/nonebot/nonebot2): 本项目的基础，非常好用的聊天机器人框架。
- [x] [fish-speech](https://github.com/fishaudio/fish-speech):零样本 & 小样本 TTS：输入 10 到 30 秒的声音样本即可生成高质量的 TTS 输出