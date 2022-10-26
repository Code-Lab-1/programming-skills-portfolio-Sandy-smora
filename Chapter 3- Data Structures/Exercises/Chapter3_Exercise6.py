## Exercise 6: Shrinking Guest List :ballot_box_with_check:

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

# At this point, have everyone sit on the ground if you have no table T-T
print("""
\n Unfortunately due to technical difficulties, we are forced to 
limit the number of attendees. We sincerely apologize for any inconvenience caused.
""")

name = guest.pop()
print(f"""
{name.title()}
Considering our initial excitement at your acceptance of the invitation. 
We are extremely saddened to inform you that we have to remove you from the 
attendees' list. We will be sure in the future to prepare better for situations 
like this. Till then, we are incredibly sorry for the inconvenience.
""")

# Invitation part 2
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
