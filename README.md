# friendly-usernames

Just a small Python CLI tool to autogenerate random usernames. 

Directory of words were taken from [glitchdotcom's friendly-words repo](https://github.com/glitchdotcom/friendly-words). 

You can clone this repo and change the list of words or upload your own words and add the appropriate filepath(s) to your own .txt files. Which could be accomplished by either placing the .txt files directly in the `words` directory _or_ by altering the `directory` variable in `main.py#get_username` to read your .txt file(s) from there.  

---
### How to run:  
_I highly encourage the use of `pipenv` for all of my Python repos, but you don't need to have it installed in order to run this repo_
#### Method 1, with `pipenv`:
1. install all dependencies: 
    - If you're going to be editing `main.py`, you'll probably want to run a `pipenv sync` so your virtualenv will have the correct dependencies for further development
    - If you aren't going to be editing code and just want to run the cli to generate usernames, you can run `pipenv install -e .`, which will allow you to hook into the `console-scripts` alias `run`. This is as opposed to running `main.py` directly (e.g. `python3 main.py`)
2. run the cli tool via `run [OPTIONS]` _or_ `pipenv run python3 main.py [OPTIONS]`
### Method 2, without `pipenv`: 
1. install the dependencies by running `pip install --editable .` 
2. call `run [OPTIONS]` at the root directory

---
### Options:
There are 2 options to the cli tool, which are: 
1. `-h` / `--handle` -- this is an optional `string` parameter that you may pass to be prepended to your generated username.
2. `-l` / `--length` -- this is the number of words that you want your generated username to use. Default is 2. 


Running the cli and passing the option flags with no values will trigger the cli to prompt you for a response for the given option.

### Examples of passing options: 
#### pipenv example
If you ran `pipenv install -e .`
```
run -h myhandle -l 3
run --hande=myhandle --length=3
```
_or_ 
```
pipenv run python3 main.py -h myhandle -l 3
pipenv run python3 main.py --handle=myhandle --length=3
```
#### no pipenv example
```
python3 main.py -h myhandle -l 3
python3 main.py -handle=myhandle --length=3
```