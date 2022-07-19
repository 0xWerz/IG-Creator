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
## Starting 

- run `python botAccountCreate.py --chrome` for chrome

- run `python botAccountCreate.py --firefox` for firefox 

## Future updates
- [x] http request for the security code 
- [ ] http requests version.
- [ ] advanced proxy rotating service
