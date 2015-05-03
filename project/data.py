""" setup movie instances 
  author: H. Kin Fung
  dates: 20140406,0504
"""
import media

movies = []
titles = [
    # Ref: http://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture 
    # 2014
    "Birdman: Or (The Unexpected Virtue of Ignorance)", 
    "American Sniper", 
    "Boyhood", 
    "The Grand Budapest Hotel", 
    "The Imitation Game", 
    "Selma", 
    "The Theory of Everything", 
    "Whiplash", 

   # 2013
   "12 Years a Slave",  
   "American Hustle",
   "Captain Phillips", 
   "Dallas Buyers Club", 
   "Gravity", 
   "Her", 
   "Nebraska", 
   "Philomena",
   "The Wolf of Wall Street", 

   # 2012
   "Argo", 
   "Amour", 
   "Beasts of the Southern Wild", 
   "Django Unchained", 
   "Les Miserables", 
   "Life of Pi", 
   "Lincoln", 
   "Silver Linings Playbook", 
   "Zero Dark Thirty", 

   # 2011
   "The Artist", 
   "The Descendants", 
   "Extremely Loud & Incredibly Close", 
   "The Help", 
   "Hugo", 
   "Midnight in Paris", 
   "Moneyball", 
   "The Tree of Life", 
   "War Horse", 
   
   # 2010
   "The King's Speech",
   "127 Hours", 
   "Black Swan", 
   "The Fighter", 
   "Inception", 
   "The Kids Are All Right", 
   "The Social Network", 
   "Toy Story 3", 
   "True Grit", 
   "Winter's Bone"

   #"12 Years a Slave",  
   #"Forrest Gump", 
   #"Interstellar", 
    #"Citizenfour"
]

for title in titles: 
    movie = media.Movie( title )
    movies.append( movie )
