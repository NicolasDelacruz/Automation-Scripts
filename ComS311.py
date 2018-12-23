#Import for opening web pages
import webbrowser

#Import for opening terminal
import subprocess

#Opening canvas
webbrowser.open('https://canvas.iastate.edu/', new=2)

cmd = "gnome-terminal --working-directory=/home/nicolas/Documents/PyScripts"
subprocess.Popen(cmd, shell=True)
