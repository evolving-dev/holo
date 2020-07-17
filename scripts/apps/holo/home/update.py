screen.blit(data["assets"]["overlay"], (0,0)) #Blit black / white overlay onto the background image


if data["cache"]["swipeframe"] == 10:
    data["cache"]["swipe"] = 0
    data["cache"]["swipeframe"] = 0

if data["cache"]["swipe"]:
    FPS = 40
    data["cache"]["swipeframe"] += 1
    screen.blit(data["surfaces"][data["page"] + (-1 if data["cache"]["swipe"] == -1 else 1)], ((data["cache"]["swipeframe"] / 10) * SETTINGS["width"] * data["cache"]["swipe"],0)) #Blit the previous page onto the screen
    screen.blit(data["surfaces"][data["page"]], ((data["cache"]["swipeframe"] / 10) * SETTINGS["width"] * data["cache"]["swipe"] + (SETTINGS["width"] if data["cache"]["swipe"] == -1 else -SETTINGS["width"] * 2),0)) #Blit the current page onto the screen
else:
    FPS = 15
    screen.blit(data["surfaces"][data["page"]], (0,0)) #Blit the current page onto the screen

if not pygame.mouse.get_pressed()[0]:
    data["cache"]["swipecache"] = 0 #Reset the swipecache if the mouse is no longer pressed

if data["cache"]["swipecache"] == 0 and pygame.mouse.get_pressed()[0]:
    data["cache"]["mouseposcache"] = list(pygame.mouse.get_pos())[0] #Get x-coords of the mouse when the mouse button / finger is not held down

data["cache"]["swipecache"] += pygame.mouse.get_pressed()[0] #Save the time in frames in which the mousebutton has been held down