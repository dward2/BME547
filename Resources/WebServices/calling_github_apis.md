# Calling GitHub APIs

GitHub API can be found at <https://developer.github.com/v3/>.

#### Example:  Get list of branches
<https://developer.github.com/v3/repos/branches/>

<https://developer.github.com/v3/repos/branches/#list-branches>

```python
import requests

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
answer = r.json()
print(answer)
for branch in answer:
    print(branch["name"])
```

