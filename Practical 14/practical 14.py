import xml.dom.minidom
import matplotlib.pyplot as plt

print("start")
DOMTree = xml.dom.minidom.parse(
    "/Users/yiyi/Desktop/IBI1_2021-22/Practical 14/go_obo.xml")
print("finish")
obo = DOMTree.documentElement
terms = obo.getElementsByTagName("term")
# get the total number of terms currently recorded in the Gene Ontology
print('The total number of terms is', len(terms))

# create a dictionary to store the terms and their childnode numbers
childnode_dictionary = {}
childnode_number = []
childnode_translation_number = []

#define a function to help calculate the childnode number
def getchild(term):
    childnum = 0
    for child in childnode_dictionary[term]:
        childnum += getchild(child)
    return childnum+1


# read the whole text to build parent-child relationship
for term in terms:
    term_id = term.getElementsByTagName('id')[0].childNodes[0].data
    childnode_dictionary[term_id] = []
    for child in term.getElementsByTagName('is_a'):
        childnode_dictionary[term_id].append(child.childNodes[0].data)
print("done")

# calculate the number of child for each term
for term in terms:
    term_id = term.getElementsByTagName('id')[0].childNodes[0].data
    childnum = getchild(term.getElementsByTagName('id')[0].childNodes[0].data)
    childnode_number.append(childnum-1)
    term_def = term.getElementsByTagName('def')
    term_def_str = term_def[0].getElementsByTagName(
        'defstr')[0].childNodes[0].data
    if 'translation' in term_def_str:
        childnode_translation_number.append(childnum)


# plot the first chart
plt.boxplot(childnode_number,
            flierprops={'marker': '.',
                        'markerfacecolor': 'red', 'color': 'black'},
            medianprops={'linestyle': '--', 'color': 'orange'}
            )
plt.xlabel = ("terms associated with 'translation'")  # set x label
plt.ylabel('childnode number', fontsize=10)  # set y label
# set a title for the boxplot
plt.title('The Distribution of Childnodes Across Terms in the Gene Ontology')

plt.show()

# plot a second chart
plt.boxplot(childnode_translation_number,
            flierprops={'marker': '.',
                        'markerfacecolor': 'red', 'color': 'black'},
            medianprops={'linestyle': '--', 'color': 'orange'}
            )
plt.xlabel = ("terms associated with 'translation'")  # set x label
plt.ylabel("childnode number of terms associated with 'translation'",
           fontsize=10)  # set y label
# set a title for the boxplot
plt.title("The Distribution of Childnodes Across Terms Associated with 'translation'")

plt.show()
# The boxplot was squashed because there was too much data and the maximum was too large

# calculate the averge number
average_childnode_number = sum(childnode_number)/len(childnode_number)
average_childnode_translation_number = sum(
    childnode_translation_number)/len(childnode_translation_number)
print('The average childnode number across terms in the gene ontology is',
      round(average_childnode_number, 2))  # print the results
print("The average childnode number of terms associated with 'translation'is",
      round(average_childnode_translation_number, 2))

# The ‘translation’ terms contain, on average, a larger number of child nodes than the overall Gene Ontology.
