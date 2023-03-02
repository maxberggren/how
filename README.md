# Install
* `make install`

# Usage
* `how find the most common words in a txt file`
  - -> `cat file.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | head`