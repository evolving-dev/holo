def text_wrap(text, width, font):

    rendered = font.render(text, False, [0,0,0]) #Create a test render of the original text

    if rendered.get_width() < width:
        return text #Return the original text if it can be left unchanged


    text_cached = text.replace(".",".\n") #Try to split the text at the end of sentences

    rendered = []

    for i in text_cached.split("\n"):

        rendered += [font.render(i, False, [0,0,0]).get_width()] #Render every line separately

    if max(rendered) < width:

        return text_cached.strip() #Return text separated at the end of sentences if it doesn't exceed the designated width

    rendered = []
    text_cached = text.split(" ") #Split at every word

    for i in text_cached:

        i = i.rstrip() + " " #Add the spaces back in

        rendered += [font.render(i, False, [0,0,0]).get_width()] #Perform another test render and get the width

    for p in range(len(rendered)):

        for i in range(len(text_cached)-1):

            if rendered[i] + rendered[i+1] < width:

                rendered[i] += rendered[i+1] #Join words together if they don't exceed the maximum width
                del rendered[i+1]

                text_cached[i] += " "+text_cached[i+1]
                del text_cached[i+1]

                break

    return "\n".join(text_cached).rstrip() #Return the formatted text

def text_cutoff(text, width, font):

    text_changed = " ".join(list(text.replace(" ", "\_")))

    text_changed = text_wrap(text_changed, width, font)

    text_changed = text_changed.split(" ")

    for i in range(len(text_changed)):
        if text_changed[i] == "":
            text_changed[i] == " "

    text_changed = "".join(text_changed).replace("  ", " ")

    if len(text_changed) > 0:

        text_changed = text_changed.split("\n")
        text_changed = text_changed[0]

    else:

        return ""

    if text_changed.replace("\_"," ") != text:

        text_changed += "..."

    return text_changed.replace("\_"," ")
