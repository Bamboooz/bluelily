<p align="center">
<img alt="bluelily logo" width="200"
src="https://github.com/Bamboooz/bluelily/blob/master/art/icon.png?raw=true" />
</p>

<p align="center">
'bluelily is an efficient library to manage GitHub data from python 🌸
<br/>
It allows for such actions as getting GitHub's repository or user information, but also pushing code to it etc.
</p>

<div align="center">

-----------------

[**Home**](https://github.com/Bamboooz/bluelily)⠀
[**Install**](https://github.com/Bamboooz/bluelily#installation)⠀
[**Documentation**](https://github.com/Bamboooz/bluelily/wiki)⠀
[**Contributing**](https://github.com/Bamboooz/bluelily/blob/master/CONTRIBUTING.md)⠀
[**Download**](https://pypi.org/project/bluelily#files)⠀
[**Security**](https://github.com/Bamboooz/bluelily/blob/master/SECURITY.md)⠀
[**License**](https://github.com/Bamboooz/bluelily/blob/master/LICENSE)

-----------------

<div align="left">

## What is bluelily?
[![](https://www.aschey.tech/tokei/github/Bamboooz/bluelily?style=flat-square)](https://github.com/Bamboooz/bluelily)

bluelily is an advanced python library to manage GitHub repositories. It allows retrieving, user, repository information.
It also gives access to commiting, fetching, cloning, creating pull requests to your, and other users repositories.
(of course when interacting with other users repositories, you will need reviews as normal etc.)

## Installation
### You can install bluelily using pip:
```bash
pip install bluelily
```

## Usage
### Retrieving GitHub repository information

```python
import bluelily as bl

bl.log_actions = True  # log user interactions with GitHub

repo1 = bl.Repository("Bamboooz", "bluelily")

print (repo1.url)
# => https://github.com/Bamboooz/bluelily
print(repo1.stars)
# => 38 or something idk
print(repo1.branches)
# => [class Branch bla bla bla, ...]
print(repo1.branches[0].name)
# => "main"
```

### And many more!
These were just random examples of bluelily usage, but there's a lot more to explore, visit [bluelily docs](https://github.com/Bamboooz/bluelily/wiki) to learn about everything you can create with bluelily.

## Documentation

 * [Documentation](https://github.com/Bamboooz/bluelily/wiki)
 * [PyPi page](https://pypi.org/project/bluelily/)

## Support bluelily
You can buy me a coffee if you enjoy my work [Buy me a coffee ☕](https://www.buymeacoffee.com/Bamboooz)

## License

This project is licensed under the [BSD-3 Clause License](https://opensource.org/license/bsd-3-clause/).