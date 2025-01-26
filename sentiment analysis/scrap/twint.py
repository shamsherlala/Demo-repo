import twint

t = twint.Config()

t.Search = 'pizza'

twint.run.Search(t)