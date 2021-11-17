#import xml.etree.ElementTree as ET
import json
#'''the beginning and end''''of parsing data from XML/JSON
#difference between json xml:
    #in json there tags looks like different way
        #<tag1>text1</tag1> <tag2>text2</tag2>instead it will be  "tag1" : "text1","tag2" : "text2",
        #complicated sctructures has parentheses { }
            #types inside "phone" : { } identifies as separate tag "type" : "intl", "number" : "+7 913 1830924"
            #compared to xml <phone type="intl"> +79177424177 </phone> without additional <number> </number> tag
input = '''[
    {   "name" : "Ruslan",
        "phone" : {
            "type" : "intl",
            "number" : "+7 913 1830924"
        },
        "email" : {
            "hide" : "yes"
        }
    },
    {   "name" : "Liaisan",
        "phone" : {
            "type" : "intl",
            "number" : "+7 917 7424177"
        },
        "email" : {
            "hide" : "yes"
        }
    }
]'''
#if we change "phone" to "phone
    #Traceback: json.decoder.JSONDecodeError: Invalid control character at: line 3 column 19 (char 47)
        #line 3
            #input = '''[   line 1
        #column 19  '        "phone : {' +1 characters in that line
            #
        #char 47
            #input = '      char 0
            #input = ''     char 1 ...etc
info = json.loads(input)                            #if we take {}
                                                        #class dict
                                                    #if we take []
                                                        #class list
#comared to xml all_stuff = ET.fromstring(input)    #<class 'xml.etree.ElementTree.Element'>
    #print-> <Element 'stuff' at 0x7ff55f7980e0>
for item in info:
    print('Name:',item["name"])
    print('Hide:',item["email"]["hide"])
    #print('Hide:',item["email"]["hide"][2])

#lst = all_stuff.findall('users/user')#<class 'list'>
    #print-> [<Element 'user' at 0x7f710f8751d0>, <Element 'user' at 0x7f710f898400>]
        #2 user tags = 2 list of tags
#print('User count:', len(lst))
#for item in lst:#print(type(item))-> <class 'xml.etree.ElementTree.Element'>
    #print(item)-> <Element 'user' at 0x7f4279cc4220>
    #           -> <Element 'user' at 0x7f777c8c61d0>
        #at 0x7f4279cc4220 ALWAYS CHANGES
        #item-> <user x="1">what inside</user>
            #-> <user x="2">what inside</user>
    #print('text:',item.find('name').text)#text is an attribute which means <name>str inside tag</name>
    #print('text:',item.find('phone').text)#with spaces after tag as in source document
    #print('Attr:',item.find('phone').get('type'))
        #if inside <user x="999"> no text </user>
            #AttributeError: 'NoneType' object has no attribute 'text'
    #print('Attr:',item.find('email').get('hide'))#get there is an attribute  ="parse here"

    #Which of the following is not true about the service-oriented approach?
