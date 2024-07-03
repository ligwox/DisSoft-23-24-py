import tkinter as tk
#import keyboard
import sys
import os
sys.path.append(os.getcwd())
from builder.builder import *
from solution.maze import Point
from tkinter import messagebox

class RectApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.game=None
        self.person=None


        director=Director()
        director.procesar(os.getcwd() + '\\json\\maze2room2beasts.json')
        self.game=director.getGame()

        self.title("Laberinto rectangular")
        self.geometry("1150x900")
        self.menubar = tk.Menu(self)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Salir", command=self.quit)
        
        self.drawmenu = tk.Menu(self.menubar, tearoff=0)
        self.drawmenu.add_command(label="Lanzar bichos", command=self.game.launchThreds)
        self.drawmenu.add_command(label="Parar bichos", command=self.game.stopThreds)
        
        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)  
        self.menubar.add_cascade(label="Bichos", menu=self.drawmenu)
        
        self.config(menu=self.menubar)

        self.toolbar = tk.Frame(self)
        self.b1 = tk.Button(self.toolbar, text="Lanzar bichos", command=self.button1_click)
        self.b2 = tk.Button(self.toolbar, text="Parar bichos", command=self.button2_click)
        self.b3 = tk.Button(self.toolbar, text="Abrir puertas", command=self.button3_click)
        self.b4 = tk.Button(self.toolbar, text="Cerrar puertas", command=self.button4_click)
        
        self.b1.pack(side=tk.LEFT)
        self.b2.pack(side=tk.LEFT) 
        self.b3.pack(side=tk.LEFT)
        self.b4.pack(side=tk.LEFT)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
       
        self.person=self.game.person
        
        self.canvas = tk.Canvas(self, width=1100, height=650, bg="white")
        self.canvas.pack(expand=True)
        self.mostrarLaberinto()
        self.dibujarLaberinto()

    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()
    
    def calcularPosicion(self):
        if not(self.game):
            return
        h1=self.game.getCont(1)
        h1.setPoint(Point(0,0))
        h1.calcularPosicion()

    def normalizar(self):
        minX=0
        minY=0
        for h in self.game.maze.children:
            if h.getPoint().x<minX:
                minX=h.getPoint().x
            if h.getPoint().y<minY:
                minY=h.getPoint().y
        for h in self.game.maze.children:
            point=h.getPoint()
            h.setPoint(Point(point.x+abs(minX),point.y+abs(minY)))

    def calcularDimensiones(self):
        maxX = 0
        maxY = 0
        for h in self.game.maze.children:
            if h.getPoint().x > maxX:
                maxX = h.getPoint().x
            if h.getPoint().y > maxY:
                maxY = h.getPoint().y
        maxX += 1
        maxY += 1
        self.ancho = (1050 / maxX)
        self.alto = (600 / maxY)

    def asignarPuntosReales(self):
        origen=Point(10,10)
        for h in self.game.maze.children:
            x=origen.x+h.getPoint().x*self.ancho
            y=origen.y+h.getPoint().y*self.alto
            h.setPoint(Point(x,y))
            h.setExtent(Point(self.ancho,self.alto))           


    def dibujarLaberinto(self):
        if not(self.game):
            return
        self.game.maze.accept(self)
        self.draw_character()
        self.draw_beasts()

    def draw_rect_room(self,x1,y1,width,height):       
        x2 = x1 + width
        y2 = y1 + height
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    def draw_rect_treasury(self,x1,y1,width,height):       
        x2 = x1 + width
        y2 = y1 + height
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="wheat")

    def visitRoom(self,room):
        self.draw_rect_room(room.getPoint().x,room.getPoint().y,room.getExtent().x,room.getExtent().y)

    def visitTreasury(self,treasury):
        self.draw_rect_treasury(treasury.getPoint().x,treasury.getPoint().y,treasury.getExtent().x,treasury.getExtent().y)
        
    def button1_click(self):
        self.game.launchThreds()

    def button2_click(self):
        self.game.stopThreds()

    def button3_click(self):
        self.game.openDoors()

    def button4_click(self):
        self.game.closeDoors()

    def animate_sprite(self):
        # Código para animar un sprite en el canvas
        pass

    def keypress(self,event):
        """Recieve a keypress and move the ball by a specified amount"""
        print(event)
        if event.char == 'w':
            app.person.goNorth()
            self.draw_character()
        elif event.char == 's':
            app.person.goSouth()
            self.draw_character()
        elif event.char == 'a':
            app.person.goWest()
            self.draw_character()
        elif event.char == 'd':
            app.person.goEast()
            self.draw_character()
        elif event.char == 'e':
            self.attack_beast()
        else:
            pass
    
    def draw_character(self):
        # Clear the previous circle
        self.delete_character_from_canvas()

        # Get the position of the character's room
        room = self.person.position
        x = room.getPoint().x + room.getExtent().x / 4  # Position the circle on the left side
        y = room.getPoint().y + room.getExtent().y / 2
        radius = min(room.getExtent().x, room.getExtent().y) / 8  # Make the circle smaller

        # Draw the new circle at the updated position
        self.character_circle = self.canvas.create_oval(
        x - radius, y - radius, x + radius, y + radius, fill="blue", outline="", tags="character"
        )
        self.draw_character_stats()

    def delete_character_from_canvas(self):
        self.canvas.delete("character")
        self.canvas.delete("lives")
        self.canvas.delete("power")
        
    def draw_character_stats(self):
        # Get the position of the character's room
        room = self.person.position
        x = room.getPoint().x + room.getExtent().x / 4
        y = room.getPoint().y + room.getExtent().y / 2
        radius = min(room.getExtent().x, room.getExtent().y) / 8

        # Draw the lives text
        lives_text = f"Lives: {self.person.life}"
        self.canvas.create_text(x + radius + 10, y - radius - 10, text=lives_text, fill="black", font=("Arial", 12), tags="lives")

        # Draw the power text
        power_text = f"Power: {self.person.power}"
        self.canvas.create_text(x + radius + 10, y + radius + 10, text=power_text, fill="black", font=("Arial", 12), tags="power")

    def delete_beasts_from_canvas(self, beast):
            self.canvas.delete("beast"+str(beast.position.num))
            self.canvas.delete("lives"+str(beast.position.num))
            self.canvas.delete("power"+str(beast.position.num))
    
    def draw_beasts(self):
        for beast in self.game.beasts:
            room = beast.position
            self.delete_beasts_from_canvas(beast)
            x = room.getPoint().x + room.getExtent().x * 3 / 4  # Position the circle on the right side
            y = room.getPoint().y + room.getExtent().y / 2
            radius = min(room.getExtent().x, room.getExtent().y) / 8  # Make the circle smaller

            if type(beast.mode) is Aggressive:
                self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius,
                fill="maroon1", outline="", tags="beast"+str(beast.position.num)
                )
            elif type(beast.mode) is Lazy:
                self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius,
                fill="yellow", outline="", tags="beast"+str(beast.position.num)
                )
            elif type(beast.mode) is Delicioso:
                self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius,
                fill="green", outline="", tags="beast"+str(beast.position.num)
                )
            elif type(beast.mode) is Depredador:
                self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius,
                fill="red", outline="", tags="beast"+str(beast.position.num)
                )

            # Draw the lives and power text
            lives_text = f"Lives: {beast.life}"
            power_text = f"Power: {beast.power}"
            self.canvas.create_text(x + radius + 10, y - radius - 10, text=lives_text, fill="black", font=("Arial", 10), tags="lives"+str(beast.position.num))
            self.canvas.create_text(x + radius + 10, y + radius + 10, text=power_text, fill="black", font=("Arial", 10), tags="power"+str(beast.position.num))


    def attack_beast(self):
        # Get the current room and the beast in that room
        current_room = self.person.position
        enemy_creature = self.game.findEnemyCreature(current_room)
        
        if enemy_creature:
            # Character attacks the beast
            enemy_creature.life -= self.person.power
            print(f"Character attacked the beast! Beast's remaining life: {enemy_creature.life}")
            # Beast attacks the character
            if enemy_creature.life > 0:
                self.person.life -= enemy_creature.power
                print(f"Beast attacked the character! Character's remaining life: {self.person.life}")
                if self.person.life <= 0:
                    self.delete_character_from_canvas()
                    messagebox.showwarning("Game Over", "The character was killed!")
                    exit()
            else:
                self.game.beasts.remove(enemy_creature)
                self.delete_beasts_from_canvas(enemy_creature)
                if len(self.game.beasts) == 0:
                    messagebox.showinfo("Congratulations", "You have defeated all the beasts and won the game.")
                    exit()

            # Redraw the character and beasts
            self.draw_character()
            self.draw_beasts()
        else:
            print("No beast in the current room.")

        
if __name__ == "__main__":
    app = RectApp()
    app.bind('w',app.keypress)
    app.bind('s',app.keypress)
    app.bind('d',app.keypress)
    app.bind('a',app.keypress)
    app.bind('e',app.keypress)
    app.mainloop()