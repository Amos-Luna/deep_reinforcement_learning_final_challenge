# -*- coding: utf-8 -*-

import numpy as np

# El entorno MountainCar-v0, de gym versión 0.22.0, tiene un estado con 2 elementos:
# posición horizontal y velocidad
# https://gymnasium.farama.org/environments/classic_control/mountain_car/
# https://github.com/openai/gym/wiki/MountainCar-v0

def get_reward(state):
    x=state[0]
    v=state[1]
    if x >= 0.5:
      print("Car has reached the goal 😁")
      #No está permitido editar las anteriores líneas de código de esta función!
      return 100
    if -1.2 <= x < -0.6:
        return -20 * (x + 0.5)**2 + 0.5
    elif -0.6 <= x < -0.4:
        return 4000 * (x + 0.5)**3 - 8
    elif -0.4 <= x < 0.25:
        return 7 * (x + 0.5)**2 + 5 * abs(x + 0.5) + 2.5
    elif 0.25 <= x <= 0.6:
        return 5 * (x)**3 + 10 * x + 10
    else:
        return -1


class EstimadorEstadosInternos():
    def __init__(self, initial_state):
        self.estado_t_menos_1 = initial_state
        self.estado_t_menos_2 = initial_state

    def calculaEstadosInternos(self, nuevo_estado):
        estado_augmentado = np.array([
                nuevo_estado[0],
                nuevo_estado[1],
                nuevo_estado[1] - self.estado_t_menos_1[1], # "derivador" de la velocidad
                nuevo_estado[1]-2*self.estado_t_menos_1[1]+self.estado_t_menos_2[1], # "2do-derivador" de la velocidad
                self.estado_t_menos_1[1],
                self.estado_t_menos_2[1], # velocidades antiguas
                np.sin(nuevo_estado[0]),
                np.cos(nuevo_estado[0]),
              ])
        self.estado_t_menos_2 = self.estado_t_menos_1
        self.estado_t_menos_1 = nuevo_estado
        return estado_augmentado