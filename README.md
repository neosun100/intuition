Intuition
=========

> Quantitative trading kit, for hackers


<!--![Dashboard](https://raw.github.com/hivetech/hivetech.github.io/master/images/QuantDashboard.png)-->
![Dashboard](http://intuition.io/img/flat-showoff.png)

> The intuitive mind is a sacred gift and the rational mind is a faithful
> servant. We have created a society that honors the servant and has forgotten
> the gift.

<i align=right>Albert Einstein</i>


Overview
--------

**Intuition** is an engine, some building bricks and a set of tools meant to
let you efficiently and intuitively make your own **automated quantitative trading
system**. It is designed to let traders, developers and scientists explore,
improve and deploy market technical hacks.

While the project is still at an early stage, you can already write, use, combine
**signal detection algorithms, portfolio allocation strategies, data sources
and contexts configurators**. Just plug your strategies and analyze
**backtests** or monitor **live trading sessions**.

In addition I work on facilities to build a distributed system and
21st century application (big data, fat computations, d3.js and other html5
stuff), tools to mix languages like Python, node.js and R and a financial
library. You will find some goodies like machine learning forecast, markowitz
portfolio optimization, genetic optimization, sentiment analysis from twitter, ...


Features
--------

* Highly configurable trading environment, powered by [zipline][9]
* From instant kickstart to full control
* Made to let you tweak algorithms, portfolio manager, data sources, contexts and plugins
* [Plugin friendly][8]. Enjoy mail or mobile notifications.
* Already includes [many][2]
* Experimental live trading on different markets (Nyse, Nasdaq, CAC40 and Forex for now)
* Experimental R integration in your algorithms
* Results analyser
* Financial library, with common used trading functions, data fetchers, ... used for example to solve Coursera econometrics assignments
* Easy to use data management, powered by [rethinkdb][6]
* [Docker](docker.io) support for development workflow and deployment
* Kind of a CI showcase as I am testing [travis](https://travis-ci.org), [wercker](wercker.com), [shippable](shippable.com), [drone.io](shippable.com), [coveralls](coveralls.io) and [landscape](landscape.io)


Status
------

[![Latest Version](https://pypip.in/v/intuition/badge.png)](https://pypi.python.org/pypi/intuition/)
<!--[![wercker status](https://app.wercker.com/status/f39a4be40502a31b3dcb94875c787b56/m "wercker status")](https://app.wercker.com/project/bykey/f39a4be40502a31b3dcb94875c787b56)-->
<!--[![wercker status](https://app.wercker.com/status/f39a4be40502a31b3dcb94875c787b56 "wercker status")](https://app.wercker.com/project/bykey/f39a4be40502a31b3dcb94875c787b56)-->
[![Build Status](https://drone.io/github.com/hackliff/intuition/status.png)](https://drone.io/github.com/hackliff/intuition/latest)
<!--[![Build Status](https://travis-ci.org/hackliff/intuition.png?branch=master)](https://travis-ci.org/hackliff/intuition)-->
[![Coverage Status](https://coveralls.io/repos/hackliff/intuition/badge.png)](https://coveralls.io/r/hackliff/intuition)
[![Code Health](https://landscape.io/github/hackliff/intuition/master/landscape.png)](https://landscape.io/github/hackliff/intuition/master)
[![Requirements Status](https://requires.io/github/hackliff/intuition/requirements.png?branch=master)](https://requires.io/github/hackliff/intuition/requirements/?branch=master)
[![License](https://pypip.in/license/intuition/badge.png)](https://pypi.python.org/pypi/intuition/)


Getting started
---------------

Learn more and find the (in progress) documentation at http://doc.intuition.io.

You can follow the development on this [trello board][1] and chat about the
project on [Gitter][3].

A webapp built on top of Intuition is also in development, get your early
ticket at http://intuition.io !


Contributing
------------

Contributors are happily welcome, [here is the place to start][10].


License
-------

Copyright 2014 Xavier Bruhiere.

Intuition is available under the [Apache License, Version 2.0][5].


[1]: https://trello.com/b/WvJDlynt/intuition
[2]: https://github.com/intuition-io/insights
[3]: https://gitter.im/intuition-io
[5]: http://www.apache.org/licenses/LICENSE-2.0.html
[6]: rethinkdb.com
[8]: https://github.com/intuition-io/insights/tree/develop/insights/plugins
[9]: https://github.com/quantopian/zipline
[10]: http://doc.intuition.io/articles/contributors.html
