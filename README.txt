Full credit for the triva questions goes to https://opentdb.com/

------------------------------------------------------------------------------------------------------------
json_parser.py
    - drop the .json files (from https://opentdb.com/) that contain the questions you want into the "data" 
      folder
    - add the .json file names to the constant "FILE_NAMES" in json_parser.py
    - run json_parser.py and it will create a "questions.json" file which game.py will use to generate 
      questions for the players
    - automatically removes duplicate questions