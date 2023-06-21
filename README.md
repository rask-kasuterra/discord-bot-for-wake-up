# discord-bot-for-wake-up

# discord bot の入力を受け付けるための EC2 の準備

## 必要なパッケージのインストール
sudo apt update
sudo apt install -y python3-pip
sudo pip3 install python-dotenv
sudo pip3 install discord.py

## ソースコードの取得と設定ファイルの作成
git clone https://github.com/rask-kasuterra/discord-bot-for-wake-up.git
cd discord-bot-for-wake-up
cp configs/.env_org configs/.env
vi configs/.env

## Systemctl へのサービスとしての設定と自動起動設定の追加
sudo vi /etc/systemd/system/mc-server-controller.service

```
[Unit]
Description=MC Server Controller
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/discord-bot-for-wake-up/
ExecStart=/usr/bin/python3 /home/ubuntu/discord-bot-for-wake-up/src/discord_bot.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
sudo systemctl daemon-reload
sudo systemctl enable mc-server-controller
sudo systemctl start mc-server-controller
sudo systemctl status mc-server-controller

## ログ確認方法
sudo journalctl -u mc-server-controller -f