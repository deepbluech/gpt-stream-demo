# gpt-stream-demo
极简版本 gpt api 调用，前端流式展示，只需会 python 即可。

## 依赖
python 3.8（其他版本应该也都行）
只要 pip 安装以下几个包即可
openai
pysocks
flask

## 需要进行的设置
### 科学上网
从 ShadowsocksX-NG -> 高级设置 -> 本地 socks5 监听地址、端口 获取
获取后填入 proxies = {'http': 'socks5h://127.0.0.1:1086', 'https': 'socks5h://127.0.0.1:1086'}

### openai key
获取后填入 openai.api_key = ''
-
最后就可以看到一个一个字显示在浏览器中
reference：https://betterprogramming.pub/openai-sse-sever-side-events-streaming-api-733b8ec32897
