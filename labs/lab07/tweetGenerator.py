"""TweetGenerator builds a chain of tweets and then creates tweets based on that chain."""
import json
import re
from random import randint

class TweetGenerator:
    """Creates tweets using a corpus of past tweets."""

    def __init__(self, sourceFile=None):
        """Initialize the class."""
        self.rawTweets = []
        self.initialStates = []
        self.markovDictionary = {}
        if sourceFile:
            self.loadTweets(sourceFile)
            self.processTweets()
            self.saveTweetGen(sourceFile + "Markov")

    def loadTweets(self, fileName):
        """Load tweets from a JSON file."""
        self.rawTweets = self.loadJSON(fileName)

    def processTweets(self):
        """Build the tweets into a chain."""
        endingCharacters = ["!", "?", "."]

        priorWord = None
        for tweet in self.rawTweets:
            for word in tweet.split() + [None]:
                if priorWord is None and not word is None:
                    self.initialStates.append(word)
                    priorWord = word
                elif word is None:
                    self.updateDictionary(priorWord, "END_OF_SENTENCE")
                    priorWord = None
                elif word[-1] in endingCharacters:
                    self.updateDictionary(priorWord, word)
                    self.updateDictionary(word, "END_OF_SENTENCE")
                    priorWord = None
                else:
                    self.updateDictionary(priorWord, word)
                    priorWord = word

    def loadTweetGen(self, fileName):
        """Load the tweets and parse the data."""
        allGenData = self.loadJSON(fileName)
        self.initialStates = allGenData['initialStates']
        self.markovDictionary = allGenData['markovDictionary']
        self.rawTweets = allGenData['rawTweets']
        print("{} Loaded".format(fileName))

    def saveTweetGen(self, fileName):
        """Save out the data parsed to a file."""
        allGenData = {'initialStates':self.initialStates,
                      'markovDictionary':self.markovDictionary,
                      'rawTweets':self.rawTweets}
        self.saveJSON(allGenData, fileName)

    def generateTweet(self):
        """Create a tweet using the chain."""
        word = self.initialStates[randint(0, len(self.initialStates) - 1)]
        tweet = [word]
        while word != "END_OF_SENTENCE":
            randomIndex = randint(0, len(self.markovDictionary[word]) - 1)
            word = self.markovDictionary[word][randomIndex]
            if not word == "END_OF_SENTENCE":
                tweet.append(word)
        return " ".join(tweet)

    def loadJSON(self, filename):
        """Read and parse a JSON file."""
        with open(filename, 'r') as fileHandler:
            jsonData = json.load(fileHandler)
        return jsonData

    def saveJSON(self, jsonData, fileName):
        """Write data to a JSON file."""
        with open(fileName, 'w') as fileHandler:
            json.dump(jsonData, fileHandler)
        print("JSON saved as {}.".format(fileName))

    def updateDictionary(self, priorWord, word):
        """Add a word to the chain."""
        if priorWord in self.markovDictionary:
            self.markovDictionary[priorWord].append(word)
        else:
            self.markovDictionary.update({priorWord:[word]})

class TrumpTweetGenerator(TweetGenerator):
    """Generates Trump-specific tweets."""

    def __init__(self, sourceFile=None):
        """Initialize the class."""
        self.theBestHashtags = []
        self.theBestWords = ["GREAT!", "SAD!", "PATHETIC!", "RIDICULOUS!", "BAD!", "UNACCEPTABLE!",
                        "NO!", "ENJOY!", "TERRIFIC!", "TERRIBLE!", "AMAZING!", "HORRIBLE!"]
        if sourceFile:
            TweetGenerator.__init__(self, sourceFile)
        else:
            TweetGenerator.__init__(self)

    def loadTweetGen(self, fileName):
        """Load tweets by Trump."""
        allGenData = self.loadJSON(fileName)
        self.initialStates = allGenData['initialStates']
        self.rawTweets = allGenData['rawTweets']
        self.markovDictionary = allGenData['markovDictionary']
        self.theBestHashtags = allGenData['theBestHashtags']
        print("{} Loaded".format(fileName))

    def saveTweetGen(self, fileName):
        """Save a corpus of Trump tweets."""
        allGenData = {'initialStates':self.initialStates,
                        'rawTweets':self.rawTweets,
                        'markovDictionary':self.markovDictionary,
                        'theBestHashtags':self.theBestHashtags}
        self.saveJSON(allGenData, fileName)

    def collectHashtags(self):
        """Search through the corpus to find all hashtags."""
        if self.rawTweets:
            hashtags = []
            hashtagRegex = r'#\w+[?.!]?'
            for tweet in self.rawTweets:
                matches = re.findall(hashtagRegex, tweet)
                for match in matches:
                    hashtags.append(match)
            self.theBestHashtags = hashtags
        else:
            print("Please load Tweet Data Before Collecting Hashtags.")

    def loadTweets(self, fileName):
        """Load all Trump tweets and parse them."""
        TweetGenerator.loadTweets(self, fileName)
        self.collectHashtags()

    def generateTrumpTweet(self):
        """Generate a Trump-specific tweet."""
        finalTweet = []
        while finalTweet == [] or len(finalTweet) > 144 or len(finalTweet) < 35:
            finalTweet = []
            for _ in range(randint(1, 3)):
                finalTweet.append(self.generateTweet())
            if randint(0, 1):
                finalTweet.append(self.theBestWords[randint(0, len(self.theBestWords) - 1)])
            if randint(0, 1):
                finalTweet.append(self.theBestHashtags[randint(0, len(self.theBestHashtags) - 1)])
            finalTweet = " ".join(finalTweet)
        return finalTweet
