> probably have a lot of bugs...
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
$ sudo go build main.go -o pgo && cp pgo /usr/bin 


```
