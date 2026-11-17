import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}Welcome to Sentiment chickens🐔{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
  user_name = "Mystery Chicken"
conversation_history = []
print(f"\n{Fore.CYAN}Hello, Chicken {user_name}!")
print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. ")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, "
f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:
  sentence=input(f"{Fore.BLUE}Please enter your sentence so we can investigate buk buk: {Style.RESET_ALL}").strip().lower()
  if sentence=="exit":
    print(f"{Fore.CYAN}exiting the sentiment chicken algorithim see you Baaawk{Style.RESET_ALL}")
    break
  elif sentence=="reset":
    if not conversation_history:
      print(f"{Fore.CYAN}No history to clear{Style.RESET_ALL}")
    else:
      print(f"{Fore.CYAN}Deleting all sentiment history{Style.RESET_ALL}")
      conversation_history.clear()
    continue
  elif sentence=="history":
    if not conversation_history:
      print(f"{Fore.CYAN}No conversation history to display{Style.RESET_ALL}")
    else:
      print(f"{Fore.CYAN}Conversation history will be displayed{Style.RESET_ALL}")
      for i,(text,polarity,sentiment) in enumerate(conversation_history):
        if sentiment=="positive":
          color=Fore.GREEN
          emoji="🐔"
        elif sentiment=="negative":
          color=Fore.RED
          emoji="🍗"
        else:
          color=Fore.YELLOW
          emoji="😐"
        print(f"{i}. {color}{emoji} {text} "f"Polarity: {polarity:.2f}, {sentiment}{Style.RESET_ALL}")
    continue
  polarity=TextBlob(sentence).sentiment.polarity
  if polarity>0:
    sentiment="positive"
    color=Fore.GREEN
    emoji="🐔"     
  elif polarity<0:
    color=Fore.RED
    emoji="🍗"  
    sentiment="negative"
  else:
    color=Fore.YELLOW
    emoji="😐"
    sentiment="neutral"
  conversation_history.append((sentence, polarity, sentiment))
  print(f"{color}{emoji} {sentiment} sentiment detected Bawk bucawk! "f"Polarity: {polarity:.2f}")
