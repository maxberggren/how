Ask ChatGPT API how to do something in the Linux terminal 

# Install
* `make install`

# Usage
* `how find the most common words in a txt file`
  - -> `cat file.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | head`
* `how to completely brick the computer`
  - -> `I'm sorry, I cannot provide a command that would intentionally brick a computer. It goes against ethical and responsible use of technology.`
* `how query the wikipedia article for Michael Jackson for its text`
  - -> `curl "https://en.wikipedia.org/w/api.php?action=query&titles=Michael+Jackson&prop=extracts&format=json"`
* `how to scrape dn.se for all its links`
  - -> `curl -s https://www.dn.se/ | grep -o 'http[^"]*'`