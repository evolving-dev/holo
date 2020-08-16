def text_wrap(text, width, font, passes=10):
    
    rendered = font.render(text, False, [0,0,0]) #Create a test render of the original text
    
    if rendered.get_width() < width:
        return text #Return the original text if it can be left unchanged
    
    
    text_cached = text.replace(".",".\n") #Try to split the text at the end of sentences
    
    rendered = []
    
    for i in text_cached.split("\n"):
        
        rendered += [font.render(i, False, [0,0,0]).get_width()] #Render every line separately
        
    if max(rendered) < width:
        
        return text_cached.rstrip() #Return text separated at the end of sentences if it doesn't exceed the designated width
    
    rendered = []
    text_cached = text.split(" ") #Split at every word
    
    for i in text_cached:
        
        i = i.rstrip() + " " #Add the spaces back in
        
        rendered += [font.render(i, False, [0,0,0]).get_width()] #Perform another test render and get the width
        
    for p in range(passes):
        try:
            for i in range(len(text_cached)-1):
                if rendered[i] + rendered[i+1] < width:
                    rendered[i] += rendered[i+1] #Join words together if they don't exceed the maximum width
                    del rendered[i+1]
                    text_cached[i] += " "+text_cached[i+1]
                    del text_cached[i+1]
                    i-=1
        except:
            pass
    return "\n".join(text_cached).rstrip() #Return the formatted text
            
def text_cutoff(text, width, font, passes=10):
    text_changed = " ".join(list(text))
    text_changed = text_wrap(text_changed, width, font, passes)
    
    text_changed = text_changed.split(" ")
    
    for i in range(len(text_changed)):
        if text_changed[i] == "":
            text_changed[i] == " "
    
    text_changed = "".join(text_changed).replace("  ", " ")
    
    if text_changed != text:
        text_changed += "..."
        
    return text_changed
    
    