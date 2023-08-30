#!/usr/bin/env python
import collections
import pprint

#emojis = pprint.pprint

##Author:Scott Weaver Date:May,2021 https://github.com/sweaver2112/Regex-combined-emojis/blob/master/compactRegex.js
emoji_pattern = [
     "🧑🏻‍❤️‍💋‍🧑🏼",
     "🧑🏻‍❤️‍💋‍🧑🏽",
     "🧑🏻‍❤️‍💋‍🧑🏾",
     "🧑🏻‍❤️‍💋‍🧑🏿",
     "🧑🏼‍❤️‍💋‍🧑🏻",
     "🧑🏼‍❤️‍💋‍🧑🏽","🧑🏼‍❤️‍💋‍🧑🏾","🧑🏼‍❤️‍💋‍🧑🏿","🧑🏽‍❤️‍💋‍🧑🏻","🧑🏽‍❤️‍💋‍🧑🏼","🧑🏽‍❤️‍💋‍🧑🏾","🧑🏽‍❤️‍💋‍🧑🏿","🧑🏾‍❤️‍💋‍🧑🏻","🧑🏾‍❤️‍💋‍🧑🏼","🧑🏾‍❤️‍💋‍🧑🏽","🧑🏾‍❤️‍💋‍🧑🏿","🧑🏿‍❤️‍💋‍🧑🏻","🧑🏿‍❤️‍💋‍🧑🏼","🧑🏿‍❤️‍💋‍🧑🏽","🧑🏿‍❤️‍💋‍🧑🏾","👩🏻‍❤️‍💋‍👨🏻","👩🏻‍❤️‍💋‍👨🏼","👩🏻‍❤️‍💋‍👨🏽","👩🏻‍❤️‍💋‍👨🏾","👩🏻‍❤️‍💋‍👨🏿","👩🏼‍❤️‍💋‍👨🏻","👩🏼‍❤️‍💋‍👨🏼","👩🏼‍❤️‍💋‍👨🏽","👩🏼‍❤️‍💋‍👨🏾","👩🏼‍❤️‍💋‍👨🏿","👩🏽‍❤️‍💋‍👨🏻","👩🏽‍❤️‍💋‍👨🏼","👩🏽‍❤️‍💋‍👨🏽","👩🏽‍❤️‍💋‍👨🏾","👩🏽‍❤️‍💋‍👨🏿","👩🏾‍❤️‍💋‍👨🏻","👩🏾‍❤️‍💋‍👨🏼","👩🏾‍❤️‍💋‍👨🏽","👩🏾‍❤️‍💋‍👨🏾","👩🏾‍❤️‍💋‍👨🏿","👩🏿‍❤️‍💋‍👨🏻","👩🏿‍❤️‍💋‍👨🏼","👩🏿‍❤️‍💋‍👨🏽","👩🏿‍❤️‍💋‍👨🏾","👩🏿‍❤️‍💋‍👨🏿","👨🏻‍❤️‍💋‍👨🏻","👨🏻‍❤️‍💋‍👨🏼","👨🏻‍❤️‍💋‍👨🏽","👨🏻‍❤️‍💋‍👨🏾","👨🏻‍❤️‍💋‍👨🏿","👨🏼‍❤️‍💋‍👨🏻","👨🏼‍❤️‍💋‍👨🏼","👨🏼‍❤️‍💋‍👨🏽","👨🏼‍❤️‍💋‍👨🏾","👨🏼‍❤️‍💋‍👨🏿","👨🏽‍❤️‍💋‍👨🏻","👨🏽‍❤️‍💋‍👨🏼","👨🏽‍❤️‍💋‍👨🏽","👨🏽‍❤️‍💋‍👨🏾","👨🏽‍❤️‍💋‍👨🏿","👨🏾‍❤️‍💋‍👨🏻","👨🏾‍❤️‍💋‍👨🏼","👨🏾‍❤️‍💋‍👨🏽","👨🏾‍❤️‍💋‍👨🏾","👨🏾‍❤️‍💋‍👨🏿","👨🏿‍❤️‍💋‍👨🏻","👨🏿‍❤️‍💋‍👨🏼","👨🏿‍❤️‍💋‍👨🏽","👨🏿‍❤️‍💋‍👨🏾","👨🏿‍❤️‍💋‍👨🏿","👩🏻‍❤️‍💋‍👩🏻","👩🏻‍❤️‍💋‍👩🏼","👩🏻‍❤️‍💋‍👩🏽","👩🏻‍❤️‍💋‍👩🏾","👩🏻‍❤️‍💋‍👩🏿","👩🏼‍❤️‍💋‍👩🏻","👩🏼‍❤️‍💋‍👩🏼","👩🏼‍❤️‍💋‍👩🏽","👩🏼‍❤️‍💋‍👩🏾","👩🏼‍❤️‍💋‍👩🏿","👩🏽‍❤️‍💋‍👩🏻","👩🏽‍❤️‍💋‍👩🏼","👩🏽‍❤️‍💋‍👩🏽","👩🏽‍❤️‍💋‍👩🏾","👩🏽‍❤️‍💋‍👩🏿","👩🏾‍❤️‍💋‍👩🏻","👩🏾‍❤️‍💋‍👩🏼","👩🏾‍❤️‍💋‍👩🏽","👩🏾‍❤️‍💋‍👩🏾","👩🏾‍❤️‍💋‍👩🏿","👩🏿‍❤️‍💋‍👩🏻","👩🏿‍❤️‍💋‍👩🏼","👩🏿‍❤️‍💋‍👩🏽","👩🏿‍❤️‍💋‍👩🏾","👩🏿‍❤️‍💋‍👩🏿","🏴󠁧󠁢󠁥󠁮󠁧󠁿","🏴󠁧󠁢󠁳󠁣󠁴󠁿","🏴󠁧󠁢󠁷󠁬󠁳󠁿","🧑🏻‍🤝‍🧑🏻","🧑🏻‍🤝‍🧑🏼","🧑🏻‍🤝‍🧑🏽","🧑🏻‍🤝‍🧑🏾","🧑🏻‍🤝‍🧑🏿","🧑🏼‍🤝‍🧑🏻","🧑🏼‍🤝‍🧑🏼","🧑🏼‍🤝‍🧑🏽","🧑🏼‍🤝‍🧑🏾","🧑🏼‍🤝‍🧑🏿","🧑🏽‍🤝‍🧑🏻","🧑🏽‍🤝‍🧑🏼","🧑🏽‍🤝‍🧑🏽","🧑🏽‍🤝‍🧑🏾","🧑🏽‍🤝‍🧑🏿","🧑🏾‍🤝‍🧑🏻","🧑🏾‍🤝‍🧑🏼","🧑🏾‍🤝‍🧑🏽","🧑🏾‍🤝‍🧑🏾","🧑🏾‍🤝‍🧑🏿","🧑🏿‍🤝‍🧑🏻","🧑🏿‍🤝‍🧑🏼","🧑🏿‍🤝‍🧑🏽","🧑🏿‍🤝‍🧑🏾","🧑🏿‍🤝‍🧑🏿","👩🏻‍🤝‍👩🏼","👩🏻‍🤝‍👩🏽","👩🏻‍🤝‍👩🏾","👩🏻‍🤝‍👩🏿","👩🏼‍🤝‍👩🏻","👩🏼‍🤝‍👩🏽","👩🏼‍🤝‍👩🏾","👩🏼‍🤝‍👩🏿","👩🏽‍🤝‍👩🏻","👩🏽‍🤝‍👩🏼","👩🏽‍🤝‍👩🏾","👩🏽‍🤝‍👩🏿","👩🏾‍🤝‍👩🏻","👩🏾‍🤝‍👩🏼","👩🏾‍🤝‍👩🏽","👩🏾‍🤝‍👩🏿","👩🏿‍🤝‍👩🏻","👩🏿‍🤝‍👩🏼","👩🏿‍🤝‍👩🏽","👩🏿‍🤝‍👩🏾","👩🏻‍🤝‍👨🏼","👩🏻‍🤝‍👨🏽","👩🏻‍🤝‍👨🏾","👩🏻‍🤝‍👨🏿","👩🏼‍🤝‍👨🏻","👩🏼‍🤝‍👨🏽","👩🏼‍🤝‍👨🏾","👩🏼‍🤝‍👨🏿","👩🏽‍🤝‍👨🏻","👩🏽‍🤝‍👨🏼","👩🏽‍🤝‍👨🏾","👩🏽‍🤝‍👨🏿","👩🏾‍🤝‍👨🏻","👩🏾‍🤝‍👨🏼","👩🏾‍🤝‍👨🏽","👩🏾‍🤝‍👨🏿","👩🏿‍🤝‍👨🏻","👩🏿‍🤝‍👨🏼","👩🏿‍🤝‍👨🏽","👩🏿‍🤝‍👨🏾","👨🏻‍🤝‍👨🏼","👨🏻‍🤝‍👨🏽","👨🏻‍🤝‍👨🏾","👨🏻‍🤝‍👨🏿","👨🏼‍🤝‍👨🏻","👨🏼‍🤝‍👨🏽","👨🏼‍🤝‍👨🏾","👨🏼‍🤝‍👨🏿","👨🏽‍🤝‍👨🏻","👨🏽‍🤝‍👨🏼",
     "👨🏽‍🤝‍👨🏾👨🏽‍🤝‍👨🏿",
     "👨🏾‍🤝‍👨🏻","👨🏾‍🤝‍👨🏼","👨🏾‍🤝‍👨🏽","👨🏾‍🤝‍👨🏿","👨🏿‍🤝‍👨🏻","👨🏿‍🤝‍👨🏼","👨🏿‍🤝‍👨🏽","👨🏿‍🤝‍👨🏾","🧑🏻‍❤️‍🧑🏼","🧑🏻‍❤️‍🧑🏽","🧑🏻‍❤️‍🧑🏾","🧑🏻‍❤️‍🧑🏿","🧑🏼‍❤️‍🧑🏻","🧑🏼‍❤️‍🧑🏽","🧑🏼‍❤️‍🧑🏾","🧑🏼‍❤️‍🧑🏿","🧑🏽‍❤️‍🧑🏻","🧑🏽‍❤️‍🧑🏼","🧑🏽‍❤️‍🧑🏾","🧑🏽‍❤️‍🧑🏿","🧑🏾‍❤️‍🧑🏻","🧑🏾‍❤️‍🧑🏼","🧑🏾‍❤️‍🧑🏽","🧑🏾‍❤️‍🧑🏿","🧑🏿‍❤️‍🧑🏻","🧑🏿‍❤️‍🧑🏼","🧑🏿‍❤️‍🧑🏽","🧑🏿‍❤️‍🧑🏾","👩🏻‍❤️‍👨🏻","👩🏻‍❤️‍👨🏼","👩🏻‍❤️‍👨🏽","👩🏻‍❤️‍👨🏾","👩🏻‍❤️‍👨🏿","👩🏼‍❤️‍👨🏻","👩🏼‍❤️‍👨🏼","👩🏼‍❤️‍👨🏽","👩🏼‍❤️‍👨🏾","👩🏼‍❤️‍👨🏿","👩🏽‍❤️‍👨🏻","👩🏽‍❤️‍👨🏼","👩🏽‍❤️‍👨🏽","👩🏽‍❤️‍👨🏾","👩🏽‍❤️‍👨🏿","👩🏾‍❤️‍👨🏻","👩🏾‍❤️‍👨🏼","👩🏾‍❤️‍👨🏽","👩🏾‍❤️‍👨🏾","👩🏾‍❤️‍👨🏿","👩🏿‍❤️‍👨🏻","👩🏿‍❤️‍👨🏼","👩🏿‍❤️‍👨🏽","👩🏿‍❤️‍👨🏾","👩🏿‍❤️‍👨🏿","👨🏻‍❤️‍👨🏻","👨🏻‍❤️‍👨🏼","👨🏻‍❤️‍👨🏽","👨🏻‍❤️‍👨🏾","👨🏻‍❤️‍👨🏿","👨🏼‍❤️‍👨🏻","👨🏼‍❤️‍👨🏼","👨🏼‍❤️‍👨🏽","👨🏼‍❤️‍👨🏾","👨🏼‍❤️‍👨🏿","👨🏽‍❤️‍👨🏻","👨🏽‍❤️‍👨🏼","👨🏽‍❤️‍👨🏽","👨🏽‍❤️‍👨🏾","👨🏽‍❤️‍👨🏿","👨🏾‍❤️‍👨🏻","👨🏾‍❤️‍👨🏼","👨🏾‍❤️‍👨🏽","👨🏾‍❤️‍👨🏾","👨🏾‍❤️‍👨🏿","👨🏿‍❤️‍👨🏻","👨🏿‍❤️‍👨🏼","👨🏿‍❤️‍👨🏽","👨🏿‍❤️‍👨🏾","👨🏿‍❤️‍👨🏿","👩🏻‍❤️‍👩🏻","👩🏻‍❤️‍👩🏼","👩🏻‍❤️‍👩🏽","👩🏻‍❤️‍👩🏾","👩🏻‍❤️‍👩🏿","👩🏼‍❤️‍👩🏻","👩🏼‍❤️‍👩🏼","👩🏼‍❤️‍👩🏽","👩🏼‍❤️‍👩🏾","👩🏼‍❤️‍👩🏿","👩🏽‍❤️‍👩🏻","👩🏽‍❤️‍👩🏼","👩🏽‍❤️‍👩🏽","👩🏽‍❤️‍👩🏾","👩🏽‍❤️‍👩🏿","👩🏾‍❤️‍👩🏻","👩🏾‍❤️‍👩🏼","👩🏾‍❤️‍👩🏽","👩🏾‍❤️‍👩🏾","👩🏾‍❤️‍👩🏿","👩🏿‍❤️‍👩🏻","👩🏿‍❤️‍👩🏼","👩🏿‍❤️‍👩🏽","👩🏿‍❤️‍👩🏾","👩🏿‍❤️‍👩🏿","👩‍❤️‍💋‍👨","👨‍❤️‍💋‍👨","👩‍❤️‍💋‍👩","👨‍👩‍👧‍👦","👨‍👩‍👦‍👦","👨‍👩‍👧‍👧","👨‍👨‍👧‍👦","👨‍👨‍👦‍👦","👨‍👨‍👧‍👧","👩‍👩‍👧‍👦","👩‍👩‍👦‍👦","👩‍👩‍👧‍👧","🧑‍🤝‍🧑","👩‍❤️‍👨","👨‍❤️‍👨","👩‍❤️‍👩","👨‍👩‍👦","👨‍👩‍👧","👨‍👨‍👦","👨‍👨‍👧","👩‍👩‍👦","👩‍👩‍👧","👨‍👦‍👦","👨‍👧‍👦","👨‍👧‍👧","👩‍👦‍👦","👩‍👧‍👦","👩‍👧‍👧","👁️‍🗨️","🧔🏻‍♂️","🧔🏼‍♂️","🧔🏽‍♂️","🧔🏾‍♂️","🧔🏿‍♂️","🧔🏻‍♀️","🧔🏼‍♀️","🧔🏽‍♀️","🧔🏾‍♀️","🧔🏿‍♀️","👨🏻‍🦰","👨🏼‍🦰","👨🏽‍🦰","👨🏾‍🦰","👨🏿‍🦰","👨🏻‍🦱","👨🏼‍🦱","👨🏽‍🦱","👨🏾‍🦱","👨🏿‍🦱","👨🏻‍🦳","👨🏼‍🦳","👨🏽‍🦳","👨🏾‍🦳","👨🏿‍🦳","👨🏻‍🦲","👨🏼‍🦲","👨🏽‍🦲","👨🏾‍🦲","👨🏿‍🦲","👩🏻‍🦰","👩🏼‍🦰","👩🏽‍🦰","👩🏾‍🦰","👩🏿‍🦰","🧑🏻‍🦰","🧑🏼‍🦰","🧑🏽‍🦰","🧑🏾‍🦰","🧑🏿‍🦰","👩🏻‍🦱","👩🏼‍🦱","👩🏽‍🦱","👩🏾‍🦱","👩🏿‍🦱","🧑🏻‍🦱","🧑🏼‍🦱","🧑🏽‍🦱","🧑🏾‍🦱","🧑🏿‍🦱","👩🏻‍🦳","👩🏼‍🦳","👩🏽‍🦳","👩🏾‍🦳","👩🏿‍🦳","🧑🏻‍🦳","🧑🏼‍🦳","🧑🏽‍🦳","🧑🏾‍🦳","🧑🏿‍🦳","👩🏻‍🦲","👩🏼‍🦲","👩🏽‍🦲","👩🏾‍🦲","👩🏿‍🦲","🧑🏻‍🦲","🧑🏼‍🦲","🧑🏽‍🦲","🧑🏾‍🦲","🧑🏿‍🦲","👱🏻‍♀️","👱🏼‍♀️","👱🏽‍♀️","👱🏾‍♀️","👱🏿‍♀️","👱🏻‍♂️","👱🏼‍♂️","👱🏽‍♂️","👱🏾‍♂️","👱🏿‍♂️","🙍🏻‍♂️","🙍🏼‍♂️","🙍🏽‍♂️","🙍🏾‍♂️","🙍🏿‍♂️","🙍🏻‍♀️","🙍🏼‍♀️","🙍🏽‍♀️","🙍🏾‍♀️","🙍🏿‍♀️","🙎🏻‍♂️","🙎🏼‍♂️","🙎🏽‍♂️","🙎🏾‍♂️","🙎🏿‍♂️","🙎🏻‍♀️","🙎🏼‍♀️","🙎🏽‍♀️","🙎🏾‍♀️","🙎🏿‍♀️","🙅🏻‍♂️","🙅🏼‍♂️","🙅🏽‍♂️","🙅🏾‍♂️","🙅🏿‍♂️","🙅🏻‍♀️","🙅🏼‍♀️","🙅🏽‍♀️","🙅🏾‍♀️","🙅🏿‍♀️","🙆🏻‍♂️","🙆🏼‍♂️","🙆🏽‍♂️","🙆🏾‍♂️","🙆🏿‍♂️","🙆🏻‍♀️","🙆🏼‍♀️","🙆🏽‍♀️","🙆🏾‍♀️","🙆🏿‍♀️","💁🏻‍♂️","💁🏼‍♂️","💁🏽‍♂️","💁🏾‍♂️","💁🏿‍♂️","💁🏻‍♀️","💁🏼‍♀️","💁🏽‍♀️","💁🏾‍♀️","💁🏿‍♀️","🙋🏻‍♂️","🙋🏼‍♂️","🙋🏽‍♂️","🙋🏾‍♂️","🙋🏿‍♂️","🙋🏻‍♀️","🙋🏼‍♀️","🙋🏽‍♀️","🙋🏾‍♀️","🙋🏿‍♀️","🧏🏻‍♂️","🧏🏼‍♂️","🧏🏽‍♂️","🧏🏾‍♂️","🧏🏿‍♂️","🧏🏻‍♀️","🧏🏼‍♀️","🧏🏽‍♀️","🧏🏾‍♀️","🧏🏿‍♀️","🙇🏻‍♂️","🙇🏼‍♂️","🙇🏽‍♂️","🙇🏾‍♂️","🙇🏿‍♂️","🙇🏻‍♀️","🙇🏼‍♀️","🙇🏽‍♀️","🙇🏾‍♀️","🙇🏿‍♀️","🤦🏻‍♂️","🤦🏼‍♂️","🤦🏽‍♂️","🤦🏾‍♂️","🤦🏿‍♂️","🤦🏻‍♀️","🤦🏼‍♀️","🤦🏽‍♀️","🤦🏾‍♀️","🤦🏿‍♀️","🤷🏻‍♂️","🤷🏼‍♂️","🤷🏽‍♂️","🤷🏾‍♂️","🤷🏿‍♂️","🤷🏻‍♀️","🤷🏼‍♀️","🤷🏽‍♀️","🤷🏾‍♀️","🤷🏿‍♀️","🧑🏻‍⚕️","🧑🏼‍⚕️","🧑🏽‍⚕️","🧑🏾‍⚕️","🧑🏿‍⚕️","👨🏻‍⚕️","👨🏼‍⚕️","👨🏽‍⚕️","👨🏾‍⚕️","👨🏿‍⚕️","👩🏻‍⚕️","👩🏼‍⚕️","👩🏽‍⚕️","👩🏾‍⚕️","👩🏿‍⚕️","🧑🏻‍🎓","🧑🏼‍🎓","🧑🏽‍🎓","🧑🏾‍🎓","🧑🏿‍🎓","👨🏻‍🎓","👨🏼‍🎓","👨🏽‍🎓","👨🏾‍🎓","👨🏿‍🎓","👩🏻‍🎓","👩🏼‍🎓","👩🏽‍🎓","👩🏾‍🎓","👩🏿‍🎓","🧑🏻‍🏫","🧑🏼‍🏫","🧑🏽‍🏫","🧑🏾‍🏫","🧑🏿‍🏫","👨🏻‍🏫","👨🏼‍🏫","👨🏽‍🏫","👨🏾‍🏫","👨🏿‍🏫","👩🏻‍🏫","👩🏼‍🏫","👩🏽‍🏫","👩🏾‍🏫","👩🏿‍🏫","🧑🏻‍⚖️","🧑🏼‍⚖️","🧑🏽‍⚖️","🧑🏾‍⚖️","🧑🏿‍⚖️","👨🏻‍⚖️","👨🏼‍⚖️","👨🏽‍⚖️","👨🏾‍⚖️","👨🏿‍⚖️","👩🏻‍⚖️","👩🏼‍⚖️","👩🏽‍⚖️","👩🏾‍⚖️","👩🏿‍⚖️","🧑🏻‍🌾","🧑🏼‍🌾","🧑🏽‍🌾","🧑🏾‍🌾","🧑🏿‍🌾","👨🏻‍🌾","👨🏼‍🌾","👨🏽‍🌾","👨🏾‍🌾","👨🏿‍🌾","👩🏻‍🌾","👩🏼‍🌾","👩🏽‍🌾","👩🏾‍🌾","👩🏿‍🌾","🧑🏻‍🍳","🧑🏼‍🍳","🧑🏽‍🍳","🧑🏾‍🍳","🧑🏿‍🍳","👨🏻‍🍳","👨🏼‍🍳","👨🏽‍🍳","👨🏾‍🍳","👨🏿‍🍳","👩🏻‍🍳","👩🏼‍🍳","👩🏽‍🍳","👩🏾‍🍳","👩🏿‍🍳","🧑🏻‍🔧","🧑🏼‍🔧","🧑🏽‍🔧","🧑🏾‍🔧","🧑🏿‍🔧","👨🏻‍🔧","👨🏼‍🔧","👨🏽‍🔧","👨🏾‍🔧","👨🏿‍🔧","👩🏻‍🔧","👩🏼‍🔧","👩🏽‍🔧","👩🏾‍🔧","👩🏿‍🔧","🧑🏻‍🏭","🧑🏼‍🏭","🧑🏽‍🏭","🧑🏾‍🏭","🧑🏿‍🏭","👨🏻‍🏭","👨🏼‍🏭","👨🏽‍🏭","👨🏾‍🏭","👨🏿‍🏭","👩🏻‍🏭","👩🏼‍🏭","👩🏽‍🏭","👩🏾‍🏭","👩🏿‍🏭","🧑🏻‍💼","🧑🏼‍💼","🧑🏽‍💼","🧑🏾‍💼","🧑🏿‍💼","👨🏻‍💼","👨🏼‍💼","👨🏽‍💼","👨🏾‍💼","👨🏿‍💼","👩🏻‍💼","👩🏼‍💼","👩🏽‍💼","👩🏾‍💼","👩🏿‍💼","🧑🏻‍🔬","🧑🏼‍🔬","🧑🏽‍🔬","🧑🏾‍🔬","🧑🏿‍🔬","👨🏻‍🔬","👨🏼‍🔬","👨🏽‍🔬","👨🏾‍🔬","👨🏿‍🔬","👩🏻‍🔬","👩🏼‍🔬","👩🏽‍🔬","👩🏾‍🔬","👩🏿‍🔬","🧑🏻‍💻","🧑🏼‍💻","🧑🏽‍💻","🧑🏾‍💻","🧑🏿‍💻","👨🏻‍💻","👨🏼‍💻","👨🏽‍💻","👨🏾‍💻","👨🏿‍💻","👩🏻‍💻","👩🏼‍💻","👩🏽‍💻","👩🏾‍💻","👩🏿‍💻","🧑🏻‍🎤","🧑🏼‍🎤","🧑🏽‍🎤","🧑🏾‍🎤","🧑🏿‍🎤","👨🏻‍🎤","👨🏼‍🎤","👨🏽‍🎤","👨🏾‍🎤","👨🏿‍🎤","👩🏻‍🎤","👩🏼‍🎤","👩🏽‍🎤","👩🏾‍🎤","👩🏿‍🎤","🧑🏻‍🎨","🧑🏼‍🎨","🧑🏽‍🎨","🧑🏾‍🎨","🧑🏿‍🎨","👨🏻‍🎨","👨🏼‍🎨","👨🏽‍🎨","👨🏾‍🎨","👨🏿‍🎨","👩🏻‍🎨","👩🏼‍🎨","👩🏽‍🎨","👩🏾‍🎨","👩🏿‍🎨","🧑🏻‍✈️","🧑🏼‍✈️","🧑🏽‍✈️","🧑🏾‍✈️","🧑🏿‍✈️","👨🏻‍✈️","👨🏼‍✈️","👨🏽‍✈️","👨🏾‍✈️","👨🏿‍✈️","👩🏻‍✈️","👩🏼‍✈️","👩🏽‍✈️","👩🏾‍✈️","👩🏿‍✈️","🧑🏻‍🚀","🧑🏼‍🚀","🧑🏽‍🚀","🧑🏾‍🚀","🧑🏿‍🚀","👨🏻‍🚀","👨🏼‍🚀","👨🏽‍🚀","👨🏾‍🚀","👨🏿‍🚀","👩🏻‍🚀","👩🏼‍🚀","👩🏽‍🚀","👩🏾‍🚀","👩🏿‍🚀","🧑🏻‍🚒","🧑🏼‍🚒","🧑🏽‍🚒","🧑🏾‍🚒","🧑🏿‍🚒","👨🏻‍🚒","👨🏼‍🚒","👨🏽‍🚒","👨🏾‍🚒","👨🏿‍🚒","👩🏻‍🚒","👩🏼‍🚒","👩🏽‍🚒","👩🏾‍🚒","👩🏿‍🚒","👮🏻‍♂️","👮🏼‍♂️","👮🏽‍♂️","👮🏾‍♂️","👮🏿‍♂️","👮🏻‍♀️","👮🏼‍♀️","👮🏽‍♀️","👮🏾‍♀️","👮🏿‍♀️","🕵🏻‍♂️","🕵🏼‍♂️","🕵🏽‍♂️","🕵🏾‍♂️","🕵🏿‍♂️","🕵🏻‍♀️","🕵🏼‍♀️","🕵🏽‍♀️","🕵🏾‍♀️","🕵🏿‍♀️","💂🏻‍♂️","💂🏼‍♂️","💂🏽‍♂️","💂🏾‍♂️","💂🏿‍♂️","💂🏻‍♀️","💂🏼‍♀️","💂🏽‍♀️","💂🏾‍♀️","💂🏿‍♀️","👷🏻‍♂️","👷🏼‍♂️","👷🏽‍♂️","👷🏾‍♂️","👷🏿‍♂️","👷🏻‍♀️","👷🏼‍♀️","👷🏽‍♀️","👷🏾‍♀️","👷🏿‍♀️","👳🏻‍♂️","👳🏼‍♂️","👳🏽‍♂️","👳🏾‍♂️","👳🏿‍♂️","👳🏻‍♀️","👳🏼‍♀️","👳🏽‍♀️","👳🏾‍♀️","👳🏿‍♀️","🤵🏻‍♂️","🤵🏼‍♂️","🤵🏽‍♂️","🤵🏾‍♂️","🤵🏿‍♂️","🤵🏻‍♀️","🤵🏼‍♀️","🤵🏽‍♀️","🤵🏾‍♀️","🤵🏿‍♀️","👰🏻‍♂️","👰🏼‍♂️","👰🏽‍♂️","👰🏾‍♂️","👰🏿‍♂️","👰🏻‍♀️","👰🏼‍♀️","👰🏽‍♀️","👰🏾‍♀️","👰🏿‍♀️","👩🏻‍🍼","👩🏼‍🍼","👩🏽‍🍼","👩🏾‍🍼","👩🏿‍🍼","👨🏻‍🍼","👨🏼‍🍼","👨🏽‍🍼","👨🏾‍🍼","👨🏿‍🍼","🧑🏻‍🍼","🧑🏼‍🍼","🧑🏽‍🍼","🧑🏾‍🍼","🧑🏿‍🍼","🧑🏻‍🎄","🧑🏼‍🎄","🧑🏽‍🎄","🧑🏾‍🎄","🧑🏿‍🎄","🦸🏻‍♂️","🦸🏼‍♂️","🦸🏽‍♂️","🦸🏾‍♂️","🦸🏿‍♂️","🦸🏻‍♀️","🦸🏼‍♀️","🦸🏽‍♀️","🦸🏾‍♀️","🦸🏿‍♀️","🦹🏻‍♂️","🦹🏼‍♂️","🦹🏽‍♂️","🦹🏾‍♂️","🦹🏿‍♂️","🦹🏻‍♀️","🦹🏼‍♀️","🦹🏽‍♀️","🦹🏾‍♀️","🦹🏿‍♀️","🧙🏻‍♂️","🧙🏼‍♂️","🧙🏽‍♂️","🧙🏾‍♂️","🧙🏿‍♂️","🧙🏻‍♀️","🧙🏼‍♀️","🧙🏽‍♀️","🧙🏾‍♀️","🧙🏿‍♀️","🧚🏻‍♂️","🧚🏼‍♂️","🧚🏽‍♂️","🧚🏾‍♂️","🧚🏿‍♂️","🧚🏻‍♀️","🧚🏼‍♀️","🧚🏽‍♀️","🧚🏾‍♀️","🧚🏿‍♀️","🧛🏻‍♂️","🧛🏼‍♂️","🧛🏽‍♂️","🧛🏾‍♂️","🧛🏿‍♂️","🧛🏻‍♀️","🧛🏼‍♀️","🧛🏽‍♀️","🧛🏾‍♀️","🧛🏿‍♀️","🧜🏻‍♂️","🧜🏼‍♂️","🧜🏽‍♂️","🧜🏾‍♂️","🧜🏿‍♂️","🧜🏻‍♀️","🧜🏼‍♀️","🧜🏽‍♀️","🧜🏾‍♀️","🧜🏿‍♀️","🧝🏻‍♂️","🧝🏼‍♂️","🧝🏽‍♂️","🧝🏾‍♂️","🧝🏿‍♂️","🧝🏻‍♀️","🧝🏼‍♀️","🧝🏽‍♀️","🧝🏾‍♀️","🧝🏿‍♀️","💆🏻‍♂️","💆🏼‍♂️","💆🏽‍♂️","💆🏾‍♂️","💆🏿‍♂️","💆🏻‍♀️","💆🏼‍♀️","💆🏽‍♀️","💆🏾‍♀️","💆🏿‍♀️","💇🏻‍♂️","💇🏼‍♂️","💇🏽‍♂️","💇🏾‍♂️","💇🏿‍♂️","💇🏻‍♀️","💇🏼‍♀️","💇🏽‍♀️","💇🏾‍♀️","💇🏿‍♀️","🚶🏻‍♂️","🚶🏼‍♂️","🚶🏽‍♂️","🚶🏾‍♂️","🚶🏿‍♂️","🚶🏻‍♀️","🚶🏼‍♀️","🚶🏽‍♀️","🚶🏾‍♀️","🚶🏿‍♀️","🧍🏻‍♂️","🧍🏼‍♂️","🧍🏽‍♂️","🧍🏾‍♂️","🧍🏿‍♂️","🧍🏻‍♀️","🧍🏼‍♀️","🧍🏽‍♀️","🧍🏾‍♀️","🧍🏿‍♀️","🧎🏻‍♂️","🧎🏼‍♂️","🧎🏽‍♂️","🧎🏾‍♂️","🧎🏿‍♂️","🧎🏻‍♀️","🧎🏼‍♀️","🧎🏽‍♀️","🧎🏾‍♀️","🧎🏿‍♀️","🧑🏻‍🦯","🧑🏼‍🦯","🧑🏽‍🦯","🧑🏾‍🦯","🧑🏿‍🦯","👨🏻‍🦯","👨🏼‍🦯","👨🏽‍🦯","👨🏾‍🦯","👨🏿‍🦯","👩🏻‍🦯","👩🏼‍🦯","👩🏽‍🦯","👩🏾‍🦯","👩🏿‍🦯","🧑🏻‍🦼","🧑🏼‍🦼","🧑🏽‍🦼","🧑🏾‍🦼","🧑🏿‍🦼","👨🏻‍🦼","👨🏼‍🦼","👨🏽‍🦼","👨🏾‍🦼","👨🏿‍🦼","👩🏻‍🦼","👩🏼‍🦼","👩🏽‍🦼","👩🏾‍🦼","👩🏿‍🦼","🧑🏻‍🦽","🧑🏼‍🦽","🧑🏽‍🦽","🧑🏾‍🦽","🧑🏿‍🦽","👨🏻‍🦽","👨🏼‍🦽","👨🏽‍🦽","👨🏾‍🦽","👨🏿‍🦽","👩🏻‍🦽","👩🏼‍🦽","👩🏽‍🦽","👩🏾‍🦽","👩🏿‍🦽","🏃🏻‍♂️","🏃🏼‍♂️","🏃🏽‍♂️","🏃🏾‍♂️","🏃🏿‍♂️","🏃🏻‍♀️","🏃🏼‍♀️","🏃🏽‍♀️","🏃🏾‍♀️","🏃🏿‍♀️","🧖🏻‍♂️","🧖🏼‍♂️","🧖🏽‍♂️","🧖🏾‍♂️","🧖🏿‍♂️","🧖🏻‍♀️","🧖🏼‍♀️","🧖🏽‍♀️","🧖🏾‍♀️","🧖🏿‍♀️","🧗🏻‍♂️","🧗🏼‍♂️","🧗🏽‍♂️","🧗🏾‍♂️","🧗🏿‍♂️","🧗🏻‍♀️","🧗🏼‍♀️","🧗🏽‍♀️","🧗🏾‍♀️","🧗🏿‍♀️","🏌🏻‍♂️","🏌🏼‍♂️","🏌🏽‍♂️","🏌🏾‍♂️","🏌🏿‍♂️","🏌🏻‍♀️","🏌🏼‍♀️","🏌🏽‍♀️","🏌🏾‍♀️","🏌🏿‍♀️","🏄🏻‍♂️","🏄🏼‍♂️","🏄🏽‍♂️","🏄🏾‍♂️","🏄🏿‍♂️","🏄🏻‍♀️","🏄🏼‍♀️","🏄🏽‍♀️","🏄🏾‍♀️","🏄🏿‍♀️","🚣🏻‍♂️","🚣🏼‍♂️","🚣🏽‍♂️","🚣🏾‍♂️","🚣🏿‍♂️","🚣🏻‍♀️","🚣🏼‍♀️","🚣🏽‍♀️","🚣🏾‍♀️","🚣🏿‍♀️","🏊🏻‍♂️","🏊🏼‍♂️","🏊🏽‍♂️","🏊🏾‍♂️","🏊🏿‍♂️","🏊🏻‍♀️","🏊🏼‍♀️","🏊🏽‍♀️","🏊🏾‍♀️","🏊🏿‍♀️","🏋🏻‍♂️","🏋🏼‍♂️","🏋🏽‍♂️","🏋🏾‍♂️","🏋🏿‍♂️","🏋🏻‍♀️","🏋🏼‍♀️","🏋🏽‍♀️","🏋🏾‍♀️","🏋🏿‍♀️","🚴🏻‍♂️","🚴🏼‍♂️","🚴🏽‍♂️","🚴🏾‍♂️","🚴🏿‍♂️","🚴🏻‍♀️","🚴🏼‍♀️","🚴🏽‍♀️","🚴🏾‍♀️","🚴🏿‍♀️","🚵🏻‍♂️","🚵🏼‍♂️","🚵🏽‍♂️","🚵🏾‍♂️","🚵🏿‍♂️","🚵🏻‍♀️","🚵🏼‍♀️","🚵🏽‍♀️","🚵🏾‍♀️","🚵🏿‍♀️","🤸🏻‍♂️","🤸🏼‍♂️","🤸🏽‍♂️","🤸🏾‍♂️","🤸🏿‍♂️","🤸🏻‍♀️","🤸🏼‍♀️","🤸🏽‍♀️","🤸🏾‍♀️","🤸🏿‍♀️","🤽🏻‍♂️","🤽🏼‍♂️","🤽🏽‍♂️","🤽🏾‍♂️","🤽🏿‍♂️","🤽🏻‍♀️","🤽🏼‍♀️","🤽🏽‍♀️","🤽🏾‍♀️","🤽🏿‍♀️","🤾🏻‍♂️","🤾🏼‍♂️","🤾🏽‍♂️","🤾🏾‍♂️","🤾🏿‍♂️","🤾🏻‍♀️","🤾🏼‍♀️","🤾🏽‍♀️","🤾🏾‍♀️","🤾🏿‍♀️","🤹🏻‍♂️","🤹🏼‍♂️","🤹🏽‍♂️","🤹🏾‍♂️","🤹🏿‍♂️","🤹🏻‍♀️","🤹🏼‍♀️","🤹🏽‍♀️","🤹🏾‍♀️","🤹🏿‍♀️","🧘🏻‍♂️","🧘🏼‍♂️","🧘🏽‍♂️","🧘🏾‍♂️","🧘🏿‍♂️","🧘🏻‍♀️","🧘🏼‍♀️","🧘🏽‍♀️","🧘🏾‍♀️","🧘🏿‍♀️","😶‍🌫️","🕵️‍♂️","🕵️‍♀️","🏌️‍♂️","🏌️‍♀️","🏋️‍♂️","🏋️‍♀️","🏳️‍🌈","🏳️‍⚧️","⛹🏻‍♂️","⛹🏼‍♂️","⛹🏽‍♂️","⛹🏾‍♂️","⛹🏿‍♂️","⛹🏻‍♀️","⛹🏼‍♀️","⛹🏽‍♀️","⛹🏾‍♀️","⛹🏿‍♀️","😮‍💨","😵‍💫","❤️‍🔥","❤️‍🩹","🧔‍♂️","🧔‍♀️","👨‍🦰","👨‍🦱","👨‍🦳","👨‍🦲","👩‍🦰","🧑‍🦰","👩‍🦱","🧑‍🦱","👩‍🦳","🧑‍🦳","👩‍🦲","🧑‍🦲","👱‍♀️","👱‍♂️","🙍‍♂️","🙍‍♀️","🙎‍♂️","🙎‍♀️","🙅‍♂️","🙅‍♀️","🙆‍♂️","🙆‍♀️","💁‍♂️","💁‍♀️","🙋‍♂️","🙋‍♀️","🧏‍♂️","🧏‍♀️","🙇‍♂️","🙇‍♀️","🤦‍♂️","🤦‍♀️","🤷‍♂️","🤷‍♀️","🧑‍⚕️","👨‍⚕️","👩‍⚕️","🧑‍🎓","👨‍🎓","👩‍🎓","🧑‍🏫","👨‍🏫","👩‍🏫","🧑‍⚖️","👨‍⚖️","👩‍⚖️","🧑‍🌾","👨‍🌾","👩‍🌾","🧑‍🍳","👨‍🍳","👩‍🍳","🧑‍🔧","👨‍🔧","👩‍🔧","🧑‍🏭","👨‍🏭","👩‍🏭","🧑‍💼","👨‍💼","👩‍💼","🧑‍🔬","👨‍🔬","👩‍🔬","🧑‍💻","👨‍💻","👩‍💻","🧑‍🎤","👨‍🎤","👩‍🎤","🧑‍🎨","👨‍🎨","👩‍🎨","🧑‍✈️","👨‍✈️","👩‍✈️","🧑‍🚀","👨‍🚀","👩‍🚀","🧑‍🚒","👨‍🚒","👩‍🚒","👮‍♂️","👮‍♀️","💂‍♂️","💂‍♀️","👷‍♂️","👷‍♀️","👳‍♂️","👳‍♀️","🤵‍♂️","🤵‍♀️","👰‍♂️","👰‍♀️","👩‍🍼","👨‍🍼","🧑‍🍼","🧑‍🎄","🦸‍♂️","🦸‍♀️","🦹‍♂️","🦹‍♀️","🧙‍♂️","🧙‍♀️","🧚‍♂️","🧚‍♀️","🧛‍♂️","🧛‍♀️","🧜‍♂️","🧜‍♀️","🧝‍♂️","🧝‍♀️","🧞‍♂️","🧞‍♀️","🧟‍♂️","🧟‍♀️","💆‍♂️","💆‍♀️","💇‍♂️","💇‍♀️","🚶‍♂️","🚶‍♀️","🧍‍♂️","🧍‍♀️","🧎‍♂️","🧎‍♀️","🧑‍🦯","👨‍🦯","👩‍🦯","🧑‍🦼","👨‍🦼","👩‍🦼","🧑‍🦽","👨‍🦽","👩‍🦽","🏃‍♂️","🏃‍♀️","👯‍♂️","👯‍♀️","🧖‍♂️","🧖‍♀️","🧗‍♂️","🧗‍♀️","🏄‍♂️","🏄‍♀️","🚣‍♂️","🚣‍♀️","🏊‍♂️","🏊‍♀️","⛹️‍♂️","⛹️‍♀️","🚴‍♂️","🚴‍♀️","🚵‍♂️","🚵‍♀️","🤸‍♂️","🤸‍♀️","🤼‍♂️","🤼‍♀️","🤽‍♂️","🤽‍♀️","🤾‍♂️","🤾‍♀️","🤹‍♂️","🤹‍♀️","🧘‍♂️","🧘‍♀️","👨‍👦","👨‍👧","👩‍👦","👩‍👧","🐕‍🦺","🐻‍❄️","🏴‍☠️","🐈‍⬛","🇦🇨","🇦🇩","🇦🇪","🇦🇫","🇦🇬","🇦🇮","🇦🇱","🇦🇲","🇦🇴","🇦🇶","🇦🇷","🇦🇸","🇦🇹","🇦🇺","🇦🇼","🇦🇽","🇦🇿","🇧🇦","🇧🇧","🇧🇩","🇧🇪","🇧🇫","🇧🇬","🇧🇭","🇧🇮","🇧🇯","🇧🇱","🇧🇲","🇧🇳","🇧🇴","🇧🇶","🇧🇷","🇧🇸","🇧🇹","🇧🇻","🇧🇼","🇧🇾","🇧🇿","🇨🇦","🇨🇨","🇨🇩","🇨🇫","🇨🇬","🇨🇭","🇨🇮","🇨🇰","🇨🇱","🇨🇲","🇨🇳","🇨🇴","🇨🇵","🇨🇷","🇨🇺","🇨🇻","🇨🇼","🇨🇽","🇨🇾","🇨🇿","🇩🇪","🇩🇬","🇩🇯","🇩🇰","🇩🇲","🇩🇴","🇩🇿","🇪🇦","🇪🇨","🇪🇪","🇪🇬","🇪🇭","🇪🇷","🇪🇸","🇪🇹","🇪🇺","🇫🇮","🇫🇯","🇫🇰","🇫🇲","🇫🇴","🇫🇷","🇬🇦","🇬🇧","🇬🇩","🇬🇪","🇬🇫","🇬🇬","🇬🇭","🇬🇮","🇬🇱","🇬🇲","🇬🇳","🇬🇵","🇬🇶","🇬🇷","🇬🇸","🇬🇹","🇬🇺","🇬🇼","🇬🇾","🇭🇰","🇭🇲","🇭🇳","🇭🇷","🇭🇹","🇭🇺","🇮🇨","🇮🇩","🇮🇪","🇮🇱","🇮🇲","🇮🇳","🇮🇴","🇮🇶","🇮🇷","🇮🇸","🇮🇹","🇯🇪","🇯🇲","🇯🇴","🇯🇵","🇰🇪","🇰🇬","🇰🇭","🇰🇮","🇰🇲","🇰🇳","🇰🇵","🇰🇷","🇰🇼","🇰🇾","🇰🇿","🇱🇦","🇱🇧","🇱🇨","🇱🇮","🇱🇰","🇱🇷","🇱🇸","🇱🇹","🇱🇺","🇱🇻","🇱🇾","🇲🇦","🇲🇨","🇲🇩","🇲🇪","🇲🇫","🇲🇬","🇲🇭","🇲🇰","🇲🇱","🇲🇲","🇲🇳","🇲🇴","🇲🇵","🇲🇶","🇲🇷","🇲🇸","🇲🇹","🇲🇺","🇲🇻","🇲🇼","🇲🇽","🇲🇾","🇲🇿","🇳🇦","🇳🇨","🇳🇪","🇳🇫","🇳🇬","🇳🇮","🇳🇱","🇳🇴","🇳🇵","🇳🇷","🇳🇺","🇳🇿","🇴🇲","🇵🇦","🇵🇪","🇵🇫","🇵🇬","🇵🇭","🇵🇰","🇵🇱","🇵🇲","🇵🇳","🇵🇷","🇵🇸","🇵🇹","🇵🇼","🇵🇾","🇶🇦","🇷🇪","🇷🇴","🇷🇸","🇷🇺","🇷🇼","🇸🇦","🇸🇧","🇸🇨","🇸🇩","🇸🇪","🇸🇬","🇸🇭","🇸🇮","🇸🇯","🇸🇰","🇸🇱","🇸🇲","🇸🇳","🇸🇴","🇸🇷","🇸🇸","🇸🇹","🇸🇻","🇸🇽","🇸🇾","🇸🇿","🇹🇦","🇹🇨","🇹🇩","🇹🇫","🇹🇬","🇹🇭","🇹🇯","🇹🇰","🇹🇱","🇹🇲","🇹🇳","🇹🇴","🇹🇷","🇹🇹","🇹🇻","🇹🇼","🇹🇿","🇺🇦","🇺🇬","🇺🇲","🇺🇳","🇺🇸","🇺🇾","🇺🇿","🇻🇦","🇻🇨","🇻🇪","🇻🇬","🇻🇮","🇻🇳","🇻🇺","🇼🇫","🇼🇸","🇽🇰","🇾🇪","🇾🇹","🇿🇦","🇿🇲","🇿🇼","👋🏻","👋🏼","👋🏽","👋🏾","👋🏿","🤚🏻","🤚🏼","🤚🏽","🤚🏾","🤚🏿","🖐🏻","🖐🏼","🖐🏽","🖐🏾","🖐🏿","🖖🏻","🖖🏼","🖖🏽","🖖🏾","🖖🏿","👌🏻","👌🏼","👌🏽","👌🏾","👌🏿","🤌🏻","🤌🏼","🤌🏽","🤌🏾","🤌🏿","🤏🏻","🤏🏼","🤏🏽","🤏🏾","🤏🏿","🤞🏻","🤞🏼","🤞🏽","🤞🏾","🤞🏿","🤟🏻","🤟🏼","🤟🏽","🤟🏾","🤟🏿","🤘🏻","🤘🏼","🤘🏽","🤘🏾","🤘🏿","🤙🏻","🤙🏼","🤙🏽","🤙🏾","🤙🏿","👈🏻","👈🏼","👈🏽","👈🏾","👈🏿","👉🏻","👉🏼","👉🏽","👉🏾","👉🏿","👆🏻","👆🏼","👆🏽","👆🏾","👆🏿","🖕🏻","🖕🏼","🖕🏽","🖕🏾","🖕🏿","👇🏻","👇🏼","👇🏽","👇🏾","👇🏿","👍🏻","👍🏼","👍🏽","👍🏾","👍🏿","👎🏻","👎🏼","👎🏽","👎🏾","👎🏿","👊🏻","👊🏼","👊🏽","👊🏾","👊🏿","🤛🏻","🤛🏼","🤛🏽","🤛🏾","🤛🏿","🤜🏻","🤜🏼","🤜🏽","🤜🏾","🤜🏿","👏🏻","👏🏼","👏🏽","👏🏾","👏🏿","🙌🏻","🙌🏼","🙌🏽","🙌🏾","🙌🏿","👐🏻","👐🏼","👐🏽","👐🏾","👐🏿","🤲🏻","🤲🏼","🤲🏽","🤲🏾","🤲🏿","🙏🏻","🙏🏼","🙏🏽","🙏🏾","🙏🏿","💅🏻","💅🏼","💅🏽","💅🏾","💅🏿","🤳🏻","🤳🏼","🤳🏽","🤳🏾","🤳🏿","💪🏻","💪🏼","💪🏽","💪🏾","💪🏿","🦵🏻","🦵🏼","🦵🏽","🦵🏾","🦵🏿","🦶🏻","🦶🏼","🦶🏽","🦶🏾","🦶🏿","👂🏻","👂🏼","👂🏽","👂🏾","👂🏿","🦻🏻","🦻🏼","🦻🏽","🦻🏾","🦻🏿","👃🏻","👃🏼","👃🏽","👃🏾","👃🏿","👶🏻","👶🏼","👶🏽","👶🏾","👶🏿","🧒🏻","🧒🏼","🧒🏽","🧒🏾","🧒🏿","👦🏻","👦🏼","👦🏽","👦🏾","👦🏿","👧🏻","👧🏼","👧🏽","👧🏾","👧🏿","🧑🏻","🧑🏼","🧑🏽","🧑🏾","🧑🏿","👱🏻","👱🏼","👱🏽","👱🏾","👱🏿","👨🏻","👨🏼","👨🏽","👨🏾","👨🏿","🧔🏻","🧔🏼","🧔🏽","🧔🏾","🧔🏿","👩🏻","👩🏼","👩🏽","👩🏾","👩🏿","🧓🏻","🧓🏼","🧓🏽","🧓🏾","🧓🏿","👴🏻","👴🏼","👴🏽","👴🏾","👴🏿","👵🏻","👵🏼","👵🏽","👵🏾","👵🏿","🙍🏻","🙍🏼","🙍🏽","🙍🏾","🙍🏿","🙎🏻","🙎🏼","🙎🏽","🙎🏾","🙎🏿","🙅🏻","🙅🏼","🙅🏽","🙅🏾","🙅🏿","🙆🏻","🙆🏼","🙆🏽","🙆🏾","🙆🏿","💁🏻","💁🏼","💁🏽","💁🏾","💁🏿","🙋🏻","🙋🏼","🙋🏽","🙋🏾","🙋🏿","🧏🏻","🧏🏼","🧏🏽","🧏🏾","🧏🏿","🙇🏻","🙇🏼","🙇🏽","🙇🏾","🙇🏿","🤦🏻","🤦🏼","🤦🏽","🤦🏾","🤦🏿","🤷🏻","🤷🏼","🤷🏽","🤷🏾","🤷🏿","👮🏻","👮🏼","👮🏽","👮🏾","👮🏿","🕵🏻","🕵🏼","🕵🏽","🕵🏾","🕵🏿","💂🏻","💂🏼","💂🏽","💂🏾","💂🏿","🥷🏻","🥷🏼","🥷🏽","🥷🏾","🥷🏿","👷🏻","👷🏼","👷🏽","👷🏾","👷🏿","🤴🏻","🤴🏼","🤴🏽","🤴🏾","🤴🏿","👸🏻","👸🏼","👸🏽","👸🏾","👸🏿","👳🏻","👳🏼","👳🏽","👳🏾","👳🏿","👲🏻","👲🏼","👲🏽","👲🏾","👲🏿","🧕🏻","🧕🏼","🧕🏽","🧕🏾","🧕🏿","🤵🏻","🤵🏼","🤵🏽","🤵🏾","🤵🏿","👰🏻","👰🏼","👰🏽","👰🏾","👰🏿","🤰🏻","🤰🏼","🤰🏽","🤰🏾","🤰🏿","🤱🏻","🤱🏼","🤱🏽","🤱🏾","🤱🏿","👼🏻","👼🏼","👼🏽","👼🏾","👼🏿","🎅🏻","🎅🏼","🎅🏽","🎅🏾","🎅🏿","🤶🏻","🤶🏼","🤶🏽","🤶🏾","🤶🏿","🦸🏻","🦸🏼","🦸🏽","🦸🏾","🦸🏿","🦹🏻","🦹🏼","🦹🏽","🦹🏾","🦹🏿","🧙🏻","🧙🏼","🧙🏽","🧙🏾","🧙🏿","🧚🏻","🧚🏼","🧚🏽","🧚🏾","🧚🏿","🧛🏻","🧛🏼","🧛🏽","🧛🏾","🧛🏿","🧜🏻","🧜🏼","🧜🏽","🧜🏾","🧜🏿","🧝🏻","🧝🏼","🧝🏽","🧝🏾","🧝🏿","💆🏻","💆🏼","💆🏽","💆🏾","💆🏿","💇🏻","💇🏼","💇🏽","💇🏾","💇🏿","🚶🏻","🚶🏼","🚶🏽","🚶🏾","🚶🏿","🧍🏻","🧍🏼","🧍🏽","🧍🏾","🧍🏿","🧎🏻","🧎🏼","🧎🏽","🧎🏾","🧎🏿","🏃🏻","🏃🏼","🏃🏽","🏃🏾","🏃🏿","💃🏻","💃🏼","💃🏽","💃🏾","💃🏿","🕺🏻","🕺🏼","🕺🏽","🕺🏾","🕺🏿","🕴🏻","🕴🏼","🕴🏽","🕴🏾","🕴🏿","🧖🏻","🧖🏼","🧖🏽","🧖🏾","🧖🏿","🧗🏻","🧗🏼","🧗🏽","🧗🏾","🧗🏿","🏇🏻","🏇🏼","🏇🏽","🏇🏾","🏇🏿","🏂🏻","🏂🏼","🏂🏽","🏂🏾","🏂🏿","🏌🏻","🏌🏼","🏌🏽","🏌🏾","🏌🏿","🏄🏻","🏄🏼","🏄🏽","🏄🏾","🏄🏿","🚣🏻","🚣🏼","🚣🏽","🚣🏾","🚣🏿","🏊🏻","🏊🏼","🏊🏽","🏊🏾","🏊🏿","🏋🏻","🏋🏼","🏋🏽","🏋🏾","🏋🏿","🚴🏻","🚴🏼","🚴🏽","🚴🏾","🚴🏿","🚵🏻","🚵🏼","🚵🏽","🚵🏾","🚵🏿","🤸🏻","🤸🏼","🤸🏽","🤸🏾","🤸🏿","🤽🏻","🤽🏼","🤽🏽","🤽🏾","🤽🏿","🤾🏻","🤾🏼","🤾🏽","🤾🏾","🤾🏿","🤹🏻","🤹🏼","🤹🏽","🤹🏾","🤹🏿","🧘🏻","🧘🏼","🧘🏽","🧘🏾","🧘🏿","🛀🏻","🛀🏼","🛀🏽","🛀🏾","🛀🏿","🛌🏻","🛌🏼","🛌🏽","🛌🏾","🛌🏿","👭🏻","👭🏼","👭🏽","👭🏾","👭🏿","👫🏻","👫🏼","👫🏽","👫🏾","👫🏿","👬🏻","👬🏼","👬🏽","👬🏾","👬🏿","💏🏻","💏🏼","💏🏽","💏🏾","💏🏿","💑🏻","💑🏼","💑🏽","💑🏾","💑🏿","#️⃣","0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","✋🏻","✋🏼","✋🏽","✋🏾","✋🏿","✌🏻","✌🏼","✌🏽","✌🏾","✌🏿","☝🏻","☝🏼","☝🏽","☝🏾","☝🏿","✊🏻","✊🏼","✊🏽","✊🏾","✊🏿","✍🏻","✍🏼","✍🏽","✍🏾","✍🏿","⛹🏻","⛹🏼","⛹🏽","⛹🏾","⛹🏿","😀","😃","😄","😁","😆","😅","🤣","😂","🙂","🙃","😉","😊","😇","🥰","😍","🤩","😘","😗","😚","😙","🥲","😋","😛","😜","🤪","😝","🤑","🤗","🤭","🤫","🤔","🤐","🤨","😐","😑","😶","😏","😒","🙄","😬","🤥","😌","😔","😪","🤤","😴","😷","🤒","🤕","🤢","🤮","🤧","🥵","🥶","🥴","😵","🤯","🤠","🥳","🥸","😎","🤓","🧐","😕","😟","🙁","😮","😯","😲","😳","🥺","😦","😧","😨","😰","😥","😢","😭","😱","😖","😣","😞","😓","😩","😫","🥱","😤","😡","😠","🤬","😈","👿","💀","💩","🤡","👹","👺","👻","👽","👾","🤖","😺","😸","😹","😻","😼","😽","🙀","😿","😾","🙈","🙉","🙊","💋","💌","💘","💝","💖","💗","💓","💞","💕","💟","💔","🧡","💛","💚","💙","💜","🤎","🖤","🤍","💯","💢","💥","💫","💦","💨","🕳","💣","💬","🗨","🗯","💭","💤","👋","🤚","🖐","🖖","👌","🤌","🤏","🤞","🤟","🤘","🤙","👈","👉","👆","🖕","👇","👍","👎","👊","🤛","🤜","👏","🙌","👐","🤲","🤝","🙏","💅","🤳","💪","🦾","🦿","🦵","🦶","👂","🦻","👃","🧠","🫀","🫁","🦷","🦴","👀","👁","👅","👄","👶","🧒","👦","👧","🧑","👱","👨","🧔","👩","🧓","👴","👵","🙍","🙎","🙅","🙆","💁","🙋","🧏","🙇","🤦","🤷","👮","🕵","💂","🥷","👷","🤴","👸","👳","👲","🧕","🤵","👰","🤰","🤱","👼","🎅","🤶","🦸","🦹","🧙","🧚","🧛","🧜","🧝","🧞","🧟","💆","💇","🚶","🧍","🧎","🏃","💃","🕺","🕴","👯","🧖","🧗","🤺","🏇","🏂","🏌","🏄","🚣","🏊","🏋","🚴","🚵","🤸","🤼","🤽","🤾","🤹","🧘","🛀","🛌","👭","👫","👬","💏","💑","👪","🗣","👤","👥","🫂","👣","🦰","🦱","🦳","🦲","🐵","🐒","🦍","🦧","🐶","🐕","🦮","🐩","🐺","🦊","🦝","🐱","🐈","🦁","🐯","🐅","🐆","🐴","🐎","🦄","🦓","🦌","🦬","🐮","🐂","🐃","🐄","🐷","🐖","🐗","🐽","🐏","🐑","🐐","🐪","🐫","🦙","🦒","🐘","🦣","🦏","🦛","🐭","🐁","🐀","🐹","🐰","🐇","🐿","🦫","🦔","🦇","🐻","🐨","🐼","🦥","🦦","🦨","🦘","🦡","🐾","🦃","🐔","🐓","🐣","🐤","🐥","🐦","🐧","🕊","🦅","🦆","🦢","🦉","🦤","🪶","🦩","🦚","🦜","🐸","🐊","🐢","🦎","🐍","🐲","🐉","🦕","🦖","🐳","🐋","🐬","🦭","🐟","🐠","🐡","🦈","🐙","🐚","🐌","🦋","🐛","🐜","🐝","🪲","🐞","🦗","🪳","🕷","🕸","🦂","🦟","🪰","🪱","🦠","💐","🌸","💮","🏵","🌹","🥀","🌺","🌻","🌼","🌷","🌱","🪴","🌲","🌳","🌴","🌵","🌾","🌿","🍀","🍁","🍂","🍃","🍇","🍈","🍉","🍊","🍋","🍌","🍍","🥭","🍎","🍏","🍐","🍑","🍒","🍓","🫐","🥝","🍅","🫒","🥥","🥑","🍆","🥔","🥕","🌽","🌶","🫑","🥒","🥬","🥦","🧄","🧅","🍄","🥜","🌰","🍞","🥐","🥖","🫓","🥨","🥯","🥞","🧇","🧀","🍖","🍗","🥩","🥓","🍔","🍟","🍕","🌭","🥪","🌮","🌯","🫔","🥙","🧆","🥚","🍳","🥘","🍲","🫕","🥣","🥗","🍿","🧈","🧂","🥫","🍱","🍘","🍙","🍚","🍛","🍜","🍝","🍠","🍢","🍣","🍤","🍥","🥮","🍡","🥟","🥠","🥡","🦀","🦞","🦐","🦑","🦪","🍦","🍧","🍨","🍩","🍪","🎂","🍰","🧁","🥧","🍫","🍬","🍭","🍮","🍯","🍼","🥛","🫖","🍵","🍶","🍾","🍷","🍸","🍹","🍺","🍻","🥂","🥃","🥤","🧋","🧃","🧉","🧊","🥢","🍽","🍴","🥄","🔪","🏺","🌍","🌎","🌏","🌐","🗺","🗾","🧭","🏔","🌋","🗻","🏕","🏖","🏜","🏝","🏞","🏟","🏛","🏗","🧱","🪨","🪵","🛖","🏘","🏚","🏠","🏡","🏢","🏣","🏤","🏥","🏦","🏨","🏩","🏪","🏫","🏬","🏭","🏯","🏰","💒","🗼","🗽","🕌","🛕","🕍","🕋","🌁","🌃","🏙","🌄","🌅","🌆","🌇","🌉","🎠","🎡","🎢","💈","🎪","🚂","🚃","🚄","🚅","🚆","🚇","🚈","🚉","🚊","🚝","🚞","🚋","🚌","🚍","🚎","🚐","🚑","🚒","🚓","🚔","🚕","🚖","🚗","🚘","🚙","🛻","🚚","🚛","🚜","🏎","🏍","🛵","🦽","🦼","🛺","🚲","🛴","🛹","🛼","🚏","🛣","🛤","🛢","🚨","🚥","🚦","🛑","🚧","🛶","🚤","🛳","🛥","🚢","🛩","🛫","🛬","🪂","💺","🚁","🚟","🚠","🚡","🛰","🚀","🛸","🛎","🧳","🕰","🕛","🕧","🕐","🕜","🕑","🕝","🕒","🕞","🕓","🕟","🕔","🕠","🕕","🕡","🕖","🕢","🕗","🕣","🕘","🕤","🕙","🕥","🕚","🕦","🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘","🌙","🌚","🌛","🌜","🌡","🌝","🌞","🪐","🌟","🌠","🌌","🌤","🌥","🌦","🌧","🌨","🌩","🌪","🌫","🌬","🌀","🌈","🌂","🔥","💧","🌊","🎃","🎄","🎆","🎇","🧨","🎈","🎉","🎊","🎋","🎍","🎎","🎏","🎐","🎑","🧧","🎀","🎁","🎗","🎟","🎫","🎖","🏆","🏅","🥇","🥈","🥉","🥎","🏀","🏐","🏈","🏉","🎾","🥏","🎳","🏏","🏑","🏒","🥍","🏓","🏸","🥊","🥋","🥅","🎣","🤿","🎽","🎿","🛷","🥌","🎯","🪀","🪁","🎱","🔮","🪄","🧿","🎮","🕹","🎰","🎲","🧩","🧸","🪅","🪆","🃏","🀄","🎴","🎭","🖼","🎨","🧵","🪡","🧶","🪢","👓","🕶","🥽","🥼","🦺","👔","👕","👖","🧣","🧤","🧥","🧦","👗","👘","🥻","🩱","🩲","🩳","👙","👚","👛","👜","👝","🛍","🎒","🩴","👞","👟","🥾","🥿","👠","👡","🩰","👢","👑","👒","🎩","🎓","🧢","🪖","📿","💄","💍","💎","🔇","🔈","🔉","🔊","📢","📣","📯","🔔","🔕","🎼","🎵","🎶","🎙","🎚","🎛","🎤","🎧","📻","🎷","🪗","🎸","🎹","🎺","🎻","🪕","🥁","🪘","📱","📲","📞","📟","📠","🔋","🔌","💻","🖥","🖨","🖱","🖲","💽","💾","💿","📀","🧮","🎥","🎞","📽","🎬","📺","📷","📸","📹","📼","🔍","🔎","🕯","💡","🔦","🏮","🪔","📔","📕","📖","📗","📘","📙","📚","📓","📒","📃","📜","📄","📰","🗞","📑","🔖","🏷","💰","🪙","💴","💵","💶","💷","💸","💳","🧾","💹","📧","📨","📩","📤","📥","📦","📫","📪","📬","📭","📮","🗳","🖋","🖊","🖌","🖍","📝","💼","📁","📂","🗂","📅","📆","🗒","🗓","📇","📈","📉","📊","📋","📌","📍","📎","🖇","📏","📐","🗃","🗄","🗑","🔒","🔓","🔏","🔐","🔑","🗝","🔨","🪓","🛠","🗡","🔫","🪃","🏹","🛡","🪚","🔧","🪛","🔩","🗜","🦯","🔗","🪝","🧰","🧲","🪜","🧪","🧫","🧬","🔬","🔭","📡","💉","🩸","💊","🩹","🩺","🚪","🛗","🪞","🪟","🛏","🛋","🪑","🚽","🪠","🚿","🛁","🪤","🪒","🧴","🧷","🧹","🧺","🧻","🪣","🧼","🪥","🧽","🧯","🛒","🚬","🪦","🗿","🪧","🏧","🚮","🚰","🚹","🚺","🚻","🚼","🚾","🛂","🛃","🛄","🛅","🚸","🚫","🚳","🚭","🚯","🚱","🚷","📵","🔞","🔃","🔄","🔙","🔚","🔛","🔜","🔝","🛐","🕉","🕎","🔯","🔀","🔁","🔂","🔼","🔽","🎦","🔅","🔆","📶","📳","📴","💱","💲","🔱","📛","🔰","🔟","🔠","🔡","🔢","🔣","🔤","🅰","🆎","🅱","🆑","🆒","🆓","🆔","🆕","🆖","🅾","🆗","🅿","🆘","🆙","🆚","🈁","🈂","🈷","🈶","🈯","🉐","🈹","🈚","🈲","🉑","🈸","🈴","🈳","🈺","🈵","🔴","🟠","🟡","🟢","🔵","🟣","🟤","🟥","🟧","🟨","🟩","🟦","🟪","🟫","🔶","🔷","🔸","🔹","🔺","🔻","💠","🔘","🔳","🔲","🏁","🚩","🎌","🏴","🏳","🏻","🏼","🏽","🏾","🏿","☺","☹","☠","❣","❤","✋","✌","☝","✊","✍","⛷","⛹","☘","☕","⛰","⛪","⛩","⛲","⛺","♨","⛽","⚓","⛵","⛴","✈","⌛","⏳","⌚","⏰","⏱","⏲","☀","⭐","☁","⛅","⛈","☂","☔","⛱","⚡","❄","☃","⛄","☄","✨","⚽","⚾","⛳","⛸","♠","♥","♦","♣","♟","⛑","☎","⌨","✉","✏","✒","✂","⛏","⚒","⚔","⚙","⚖","⛓","⚗","⚰","⚱","♿","⚠","⛔","☢","☣","⬆","↗","➡","↘","⬇","↙","⬅","↖","↕","↔","↩","↪","⤴","⤵","⚛","✡","☸","☯","✝","☦","☪","☮","♈","♉","♊","♋","♌","♍","♎","♏","♐","♑","♒","♓","⛎","▶","⏩","⏭","⏯","◀","⏪","⏮","⏫","⏬","⏸","⏹","⏺","⏏","♀","♂","⚧","✖","➕","➖","➗","♾","‼","⁉","❓","❔","❕","❗","〰","⚕","♻","⚜","⭕","✅","☑","✔","❌","❎","➰","➿","〽","✳","✴","❇","©","®","™","ℹ","Ⓜ","㊗","㊙","⚫","⚪","⬛","⬜","◼","◻","◾","◽","▪","▫"]

"""
This is the entry point for the command-line interface (CLI) application.

It can be used as a handy facility for running the task from a command line.

.. note::

    To learn more about Click visit the
    `project website <http://click.pocoo.org/5/>`_.  There is also a very
    helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.

    To learn more about running Luigi, visit the Luigi project's
    `Read-The-Docs <http://luigi.readthedocs.io/en/stable/>`_ page.

.. currentmodule:: emojintrospector.cli
.. moduleauthor:: jmikedupont2 <jmikedupont2@gmail.com>
"""
import logging
import click
from .__init__ import __version__

LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


class Info(object):
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0


# pass_info is a decorator for functions that pass 'Info' objects.
#: pylint: disable=invalid-name
pass_info = click.make_pass_decorator(Info, ensure=True)


# Change the options to below to suit the actual options for your task (or
# tasks).

@click.group()
@click.option("--verbose", "-v", count=True, help="Enable verbose output.")
@pass_info
def cli(info: Info, verbose: int):
    """Run emojintrospector."""
    # Use the verbosity count to determine the logging level...
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS[verbose]
            if verbose in LOGGING_LEVELS
            else logging.DEBUG
        )
        click.echo(
            click.style(
                f"Verbose logging is enabled. "
                f"(LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    info.verbose = verbose


@cli.command()
@click.option("--input", "-i", help="Input file.")
@pass_info
def read(_: Info, input):
    """Say 'hello' to the nice people."""
    with open(input) as fi:
        dd = collections.Counter()
        lines = []
        for l in fi:
            for w in l.split(" "):
                dd[w]+= 1
                lines.append(w)

        #now we assign an emoji
        tokens = [w[0] for w in dd.most_common()]

        multiplied = int((len(tokens) / len(emoji_pattern) ) + 1)
        
        book = []
        for x in range(multiplied):
            book.extend(emoji_pattern)
        
        lookup = dict(zip(tokens,reversed(book) ))

        line = ""
        for x in lines:
            
            c1 = lookup[x]
            line = line + c1

            if len(line)> 40:
                print(line) #newline
                line = ""


@cli.command()
def version():
    """Get the library version."""
    click.echo(click.style(f"{__version__}", bold=True))
