Pelican plugin: Advance Embed Tweet
===================================

Embedding tweets into your Pelican blog posts. This repo is an advance
version of the plugin from
`lqez <https://github.com/lqez/pelican-embed-tweet>`__ which hasn't the
config for the style.

| Author \| Fundor333 \|
| :----: \| \|:-----------------------------: \|
|   Email \| f333@fundor333.com \|
| Homepage \| https://www.fundor333.com \|
|  Github \| https://github.com/fundor333 \|
|  Twitter \| https://twitter.com/fundor333 \|

# How to use it
---------------

1. Install the plugin with ``pip install pelican_advance_embed_tweet``
2. Put ``pelican_advance_embed_tweet`` into plugin list of settings.

   -  ``PLUGINS = ['pelican_advance_embed_tweet']``

3. Add your config into the ``pelicanconf.py``

Config
------

The config implement the `Twitter
Api <https://dev.twitter.com/web/embedded-tweets/parameters>`__.

+----------+-----------------------------------------------------------------+
| **Config | **Description**                                                 |
| Label**  |                                                                 |
+==========+=================================================================+
| TWITTER\ | When set to ``hidden``, links in a Tweet are not expanded to    |
| _CARDS   | photo, video, or link previews.                                 |
+----------+-----------------------------------------------------------------+
| TWITTER\ | When set to ``none``, only the cited Tweet will be displayed    |
| _THEME   | even if it is in reply to another Tweet.                        |
+----------+-----------------------------------------------------------------+
| TWITTER\ | When set to ``dark``, displays Tweet with light text over a     |
| _CONVERS | dark background.                                                |
| ATION    |                                                                 |
+----------+-----------------------------------------------------------------+
| TWITTER\ | Adjust the color of Tweet links with a hexadecimal color value. |
| _LINK\_C |                                                                 |
| OLOR     |                                                                 |
+----------+-----------------------------------------------------------------+
| TWITTER\ | The maximum width of the rendered Tweet in whole pixels. This   |
| _WIDTH   | value should be between 250 and 550 pixels.                     |
+----------+-----------------------------------------------------------------+
| TWITTER\ | Float the Tweet ``left``, ``right``, or ``center`` relative to  |
| _ALIGN   | its container. Typically set to allow text or other content to  |
|          | wrap around the Tweet.                                          |
+----------+-----------------------------------------------------------------+
| TWITTER\ | A supported Twitter language code. Loads text components in the |
| _LANG    | specified language. Note: does not affect the text of the cited |
|          | Tweet.                                                          |
+----------+-----------------------------------------------------------------+
| TWITTER\ | When set to true, the Tweet and its embedded page on your site  |
| _DNT     | are not used for purposes that include personalized suggestions |
|          | and personalized ads.                                           |
+----------+-----------------------------------------------------------------+
