class Animation(object):
    def __init__(self, chamber):
        self.chamber = []
        self.particles = []
        self.len_chamber = len(chamber)

        # building empty chamber
        for i in range(len(chamber)):
            self.chamber.append(['.'])
            if chamber[i] is not '.':
                self.particles.append(Particle(chamber[i],i,self.len_chamber))

    def animate(self, speed):
        for particle in self.particles:
            particle.move_particle(speed)
        animation.build_chamber()

    def build_chamber(self):
        temp_chamber = []
        temp_index = '.'
        result = ''

        # building temp chamber
        for i in range(len(self.chamber)):
            temp_chamber.append(['.'])

        for particle in self.particles:
            if particle.exists:
                temp_chamber[particle.position].append(particle)

        # print(temp_chamber)
        for i in range(len(temp_chamber)):
            for j in range(len(temp_chamber[i])):
                if type(temp_chamber[i][j]) is Particle:
                    temp_index = 'X' # comment this and uncomment line bellow
                                    # if you want to see R and L instead of X
                    # temp_index = temp_chamber[i][j].direction
                else:
                    temp_index = '.'
            result += temp_index
        print(result)
        return(result)

class Particle(object):
    def __init__(self, direction, position, len_chamber):
        # map attributes
        self.direction = direction
        self.position = position
        self.len_chamber = len_chamber
        self.exists = True

    def move_particle(self,speed):
        if self.direction == 'R':
            self.position = self.position + speed
            if self.position > self.len_chamber - 1:
                self.exists = False
        else:
            self.position = self.position - speed
            if self.position < 0:
                self.exists = False
        # print(self.position, self.len_chamber)

# In lieu of UI elements that I used in JS:
init = 'R.R...L'
animation = Animation(init)
animation.build_chamber()
animation.animate(1)
animation.animate(2)
animation.animate(1)
animation.animate(1)
animation.animate(1)
animation.animate(1)