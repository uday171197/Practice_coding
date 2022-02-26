contributer,projects = [int(i) for i in input('Enter no of contibuters and no of project').split()]


contibuters_details = {}
for i in range(contributer):
    contributer_name, skills = [i for i in input('Enter contibuter name and No of skills : ').split()]
    
    skills_data = {}
    for skill in range(int(skills)):
        skill_name,level =  [i for i in input('Enter contibuter skill and rating : ').split()]
        skills_data[skill_name] = int(level)
    contibuters_details[contributer_name] = skills_data

project_details = {}
for i in range(projects):
    projectname,a,b,c,skills_required = [i for i in input().split()]
    project_skill = {}
    for i in range(int(skills_required)):
        skill_name,level =  [i for i in input('Enter contibuter skill and rating : ').split()]
        project_skill[skill_name] = int(level)
    project_details[projectname] = [int(a),int(b),int(c),project_skill]
    
project_details

lexical_order

















