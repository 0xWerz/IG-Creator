> probably it have a lot of bugs...
## Configurations
  - run `pip install -r requirements.txt`
<br>
Download the browserdriver:

- for chrome [chromedriver](https://chromedriver.chromium.org/downloads)
- for firefox [geckodriver](https://github.com/mozilla/geckodriver/releases) <br>
### Set the driver in path  
  - open main.py 
```python
42       driver = webdriver.Chrome('Chrome driver path here')
50       driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"Gecko driver path here")

```
## ⬇️ Installation

```ruby
$ git clone https://github.com/0xWerz/IG-Creator.git
$ cd IG-Creator
$ python3 -m pip install -r requirements.txt
```
## 📈 Usage

```ruby
$ python3 main.py --help
 usage: main.py [-h] (--firefox | --chrome)

 options:
  -h, --help  show this help message and exit
  --firefox   Use Firefox - geckodriver
  --chrome    Use Chrome - chromedriver
```

## 🖊️ Example

```ruby
$ python3 main.py --chrome
```
