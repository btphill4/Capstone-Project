# Capstone-Project
Aisha Tenant Matching Application

# To-Do
- Link fake DB to code
- Add logic to methods
- Create Data structure to hold matches (or array of python tuples)
- Decide on weights for questions / how it is stored

# **Planning and Notes:**
## Filter Method:
- Eliminates potential matches if most important matches do not match
- Scoring system with weights in each category (most important, medium, and least) out of 100 and only saves if the person does not get filtered out by most important questions
- Assign a % to each category and weight each question based on number of questions in each category 
- Example: If given a weight of 60% to all most important questions and there are 6 most important questions, each of those questions returns a % up to 10%
- make a simple data structure to hold all the matches along with their score, or just use an array of python tuples
- have every question as a methods that returns a score out of 100 tha gets weighted

## Other Notes:
- Question 26: Take the two survey results and subtract the two numbers and the lower number the better

## Important Links:
- [Application Questions Importance](https://docs.google.com/document/d/1V_Ck4jLrqV8R8Zfp6E6u_KgL7fsAu6P7IxuN3JAnunk/edit)
- [Taiga](https://tree.taiga.io/project/bphillips-aisha-comfortable-living-tenant-matching/timeline) 