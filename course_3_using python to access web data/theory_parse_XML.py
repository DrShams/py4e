import xml.etree.ElementTree as ET
#'''the beginning and end''''of parsing data from XML
input = '''<stuff>
    <users>
        <user x="1">
            <id>001</id>
            <name>Ruslan</name>
               <phone type="intl">
                    +79131830924
                </phone>
                <email hide="yes"/>
        </user>
        <user x="2">
            <id>002</id>
            <name>Liaisan</name>
                <phone type="intl">
                    +79177424177
                </phone>
                <email hide="yes"/>'
        </user>
    </users>
</stuff>'''
#if we change </users> to </users
    #xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 20
all_stuff = ET.fromstring(input)#<class 'xml.etree.ElementTree.Element'>
    #print-> <Element 'stuff' at 0x7ff55f7980e0>
lst = all_stuff.findall('users/user')#<class 'list'>
    #print-> [<Element 'user' at 0x7f710f8751d0>, <Element 'user' at 0x7f710f898400>]
        #2 user tags = 2 list of tags
print('User count:', len(lst))
for item in lst:#print(type(item))-> <class 'xml.etree.ElementTree.Element'>
    #print(item)-> <Element 'user' at 0x7f4279cc4220>
    #           -> <Element 'user' at 0x7f777c8c61d0>
        #at 0x7f4279cc4220 ALWAYS CHANGES
        #item-> <user x="1">what inside</user>
            #-> <user x="2">what inside</user>
    print('text:',item.find('name').text)#text is an attribute which means <name>str inside tag</name>
    print('text:',item.find('phone').text)#with spaces after tag as in source document
    print('Attr:',item.find('phone').get('type'))
        #if inside <user x="999"> no text </user>
            #AttributeError: 'NoneType' object has no attribute 'text'
    print('Attr:',item.find('email').get('hide'))#get there is an attribute  ="parse here"
