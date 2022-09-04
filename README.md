# Script: polybar-vk
A python script that shows count of unread vk messages. And opens tab with messanger after left-click

It uses VKAPI. So you should get your access token (preferably offline token) from [here](https://dev.vk.com/api/access-token/getting-started#%D0%9A%D0%BB%D1%8E%D1%87%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F).

![image](/screenshots/Screenshot_2022-09-04_18-51-50.png)
## Installation
`git clone https://github.com/AsKreY/polybar-vk.git ~/.config/polybar/vk/`

__Nota bene__ Maybe your path to polybar folder is different than mine so you need to put it instead.
## Configuration
After installation you should open `vk_messages.py` and paste your access tokent into access_token variable
## Module
```ini
[module/vk]
type = custom/script
exec = ~/.config/polybar/vk/vk_messages.py
interval = 10
format-padding = 1
format = <label>
format-prefix = " "
format-prefix-foreground = #1E90FF
click-left = xdg-open https://vk.com/im
```