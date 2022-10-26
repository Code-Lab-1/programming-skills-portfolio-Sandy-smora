## Exercise 5: Change Guest List :ballot_box_with_check:

# The Invitation
guest = ["William James Moriarty", "Albert James Moriarty", "Louis James Moriarty"]

name = guest[0].title()
print(f"""{name},
You are cordially invited to join for drinks and dinner at the Warlington Estate. 
Your presence is requested from 3pm on 14th of July for an enjoyable evening. 
We do hope you are able to attend and share this evening with us.
""")

name = guest[1].title()
print(f"""{name},
You are cordially invited to join for drinks and dinner at the Warlington Estate. 
Your presence is requested from 3pm on 14th of July for an enjoyable evening. 
We do hope you are able to attend and share this evening with us.
""")

name = guest[2].title()
print(f"""{name},
You are cordially invited to join for drinks and dinner at the Warlington Estate. 
Your presence is requested from 3pm on 14th of July for an enjoyable evening. 
We do hope you are able to attend and share this evening with us.
""")

name = guest[1].title()
print(f"""\n 
It has come to our attention that {name} will not be able to attend the occasion 
due to work-related reasons that need his attention.
""")

# Non-attende
del(guest[1])
guest.insert(1, "Sherlock Holmes")

# Re-do
name = guest[0].title()
print(f"""{name},
You are cordially invited to join for drinks and dinner at the Warlington Estate. 
Your presence is requested from 3pm on 14th of July for an enjoyable evening. 
We do hope you are able to attend and share this evening with us.
""")

name = guest[1].title()
print(f"""{name},
You are cordially invited to join for drinks and dinner at the Warlington Estate. 
Your presence is requested from 3pm on 14th of July for an enjoyable evening. 
We do hope you are able to attend and share this evening with us.
""")

name = guest[2].title()
print(f"""{name},
You are cordially invited to join for drinks and dinner at the Warlington Estate. 
Your presence is requested from 3pm on 14th of July for an enjoyable evening. 
We do hope you are able to attend and share this evening with us.
""")