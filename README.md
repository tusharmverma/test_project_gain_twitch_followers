# test_project_gain_twitch_followers
 Creating a bot to gain followers

As starting to stream its like an inferior complex to not hae followers just to learn how those bots for followers are built.
I ended writing a bot to get to followers.

CONTRIBUTE: Contributions are always welcome!

---

## Requirements

* **python** version >= **3.7.0** installed

## Installation

```bash
git clone https://github.com/MD3XTER/Twitch-Farmer.git

cd Twitch-Farmer

pip3 install selenium pandas

python3 twitch_farmer.py
```

## Usage

In order for the bot to run, you need to add at least one account to the accounts.csv file located in the _data_ folder.

You only need to specify the **username** and **password**, the **following_channel** and **used_proxy** columns are filled by the bot for _log_ purposes.

|**username**|**password**|**following_channel**|**used_proxy**|
|---|---|---|---|
|_root_|_toor_|||

---

Besides accounts.csv file you also need too specify the proxies in the  proxies.csv file located in the _data_ folder.

You only need to specify the **proxy**. The **status** column is filled by the bot for _log_ purposes.

|proxy|status|
|---|---|
|_192.168.0.1:3000_||

## Maintaining this project

Now and then Twich changes it's elements ids, classes, etc. In order for the bot to work even after this changes,
 you need to change the value of a specific object in the _page_elements.json_ file.

Example:

```json
"username_input": {
  "type": "xPath",
  "value": "//div[contains(@data-a-target,'login-username-input')]/input"
},
```