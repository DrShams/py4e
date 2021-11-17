text = "X-DSPAM-Confidence:    0.8475";
min_value = max_value = None
for i in text:
    try:
        number = int(i)
        if (min_value == None or min_value > text.find(i)):
            min_value = text.find(i)
        if (max_value == None or max_value < text.find(i)):
            max_value = text.find(i)
    except:
        continue
number = float(text[min_value:max_value+1])
print(number)
