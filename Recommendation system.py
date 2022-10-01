import sys

# Welcome to the recommendation system program made by Clovis H.//
# This program works for any dataset prototype of the one that is below.//

# Below is a dataset in which usernames, movies, and ratings werer stored in form of a dictionary.//

UserMovieRatings = {
'Amy': {'Family Plot':10, 'Rebecca':5, 'Spellbound':9, 'Star Trek':6},
'Bill': {'Apocalypto':8, 'Braveheart':3, 'Rebecca':10, 'Spellbound':5, 'Star Trek':7},
'Cathy': {'Spaceballs':7, 'The Ice Storm':4, 'Family Plot':5, 'Rebecca':9, 'Spellbound':1},
'Dave': {'Braveheart':5, 'Rebecca':7, 'Spellbound':4},
'Ernie': {'Apocalypto':3, 'Braveheart':8, 'Rebecca':1, 'Star Trek':7},
'Fiona': {'The Ice Storm':3, 'Family Plot':10, 'Rebecca':6, 'Spellbound':10}
}

# I structured my code in chunks of functions (methods) and put all of the functions in a class file "User"./

class User():

# Initiating the first method/function that displays the welcome information
    def __init__(self):
        
        print ("This program is a movie recommendation system based on movie ratings.\n") 
        print('The person to whom you want to make movie recommendations has')
        print('to be among the list of names provided below:\n')
    
    
# Setting up a function that gooes through the dataset (dictionary) and saves the usernames as a list.//
   
    def ratersList(self,dataset):
        
        self.dataset=dataset
       
        self.raterslist=[]
        
        for username,movieratings in dataset.items():
            self.raterslist.append(username)
            
            print(username)

        return self.raterslist
    
    
# A function that takes the program user's input (username) and verifies if this is in the dataset. // 
    def getUserName(self):
        
        print('\nYou can quit the program at anytime by inputting the letter "q".')
        self.UserX=input('Type the name of the person to whom you want to recommend a movie:\n')
        a=0
        
        while a==0:
            try:
                self.UserX=self.UserX.capitalize()
            
                if self.UserX=='Q':
                    sys.exit()
            
                elif self.UserX in self.raterslist:
                    print()
                    print('You want to recommend movies to',self.UserX, end='.')
                    return self.UserX
                
                else:
                    print('Incorrect name! Try again.')
                    self.UserX=input('Type the name of the person to whom you want to recommend a movie:\n')
            except:
                 print('You closed the program')
                 sys.exit()

# A function that extract the names and ratings of movies in the dataset (dictionary) and stores them
# in sub-dictionaries useful from which to make:
    # 1. calculations (Manhattan distance) to know closeness of movie-tastes among the users in the dataset
    # 2. a dictionary that has an intermediary recommendation list
    # 3. a dictionary that has the final movie recommendation list
    
    
    def movieRatings(self):
               
        self.ratings1D={}
        self.movie_username_username={}
        self.recommendation={}
        self.final_recommendation={}
             
        
        # extracting usernames and movieratings from the dataset
        for username,movieratings in self.dataset.items():
            
            # extracting names of movies and respective ratings from the movieratings dictionary
            for movie,ratings in movieratings.items():
                
                try:
                    if username != self.UserX:
                        
                        # calculating the Manhattan distances between each movie rating of the userinput and 
                        # the other users.//
                        
                        diff=abs(self.dataset[self.UserX][movie]-self.dataset[username][movie])
                        
                        self.username=username
                        
                        if movie in self.dataset[self.UserX]:
                            
                            # dictionary that stores the different Manhattan distances between the movies
                            # each user has rated
                            self.movie_username_username[movie+self.UserX+username]=diff
                   
                            somme=0
                            for moviename,diffrating in self.movie_username_username.items():
                                
                                # dictionary that stores the Manhattan distances between the different users
                                # based on all the movie ratings each user has rated.
                                if (self.UserX+username) in moviename:
                                    somme=somme+diffrating
                                    self.ratings1D[self.UserX+username]=somme
                                         
                except:
                    
                    # dictionaries with movies to be recommended 
                    self.recommendation[movie+self.UserX+username]=ratings
                    self.final_recommendation[movie]=ratings
        
            
# Function that goes through the sub-dictionaries created in the movieRating function. It determines
# lowest Manhattan distance and extracts information about the two users who are concerned. For this,
# a few other dictionaries are created to store this new information.
       
    def recommendationlist(self):
         
        self.similar_user={}
        self.recommendation_dictionary={}
        minvalue=min(self.ratings1D.values())

        for b in self.recommendation.keys():
        
            for i in self.ratings1D.keys():
                
                if self.ratings1D[i]== minvalue:
                    
                    if i in b:
                       
                        for similar_user in self.raterslist:
                            if similar_user !=self.UserX:
                                if similar_user in i:
                                    
                                    self.similar_user[similar_user]=similar_user
                       
                        for final_movie_name in self.final_recommendation.keys():
                            if final_movie_name in b:
                                self.recommendation_dictionary[final_movie_name]=self.recommendation[b]
        
# Defining a function that displays the final results in a wanted manner                              

    def printrecommendationlist(self):

        print()
        print()
        print('User',self.UserX,'likes the same movies as'," and ".join(self.similar_user.keys()),end='.')
        print()
        print('Therefore,',self.UserX, 'is recommended to watch:')
        print()
        count=1
        for movechoice,ratingchoice in self.recommendation_dictionary.items():
        
            print('=>',movechoice,'- rating:',ratingchoice)
            count=count+1

 # Main program
                           
f=User()
f.ratersList(UserMovieRatings)
f.getUserName()
f.movieRatings()
f.recommendationlist()
f.printrecommendationlist()




        

        

