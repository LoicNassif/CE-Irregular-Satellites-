from swarms import CollSwarm

#main()
def main():
    #CollSwarm(self, M0, Dt, Dmax, L_s, M_s, M_pl, a_pl, R_pl, eta, rho=1500)
    jupiter = CollSwarm(7.37307e19, 100., 150000., 3.828e26, 1.989e30,
                        1.89587112e27, 7.7792e11, 6.9911e7, 0.4, 6.)
    area = jupiter.computeAtot()
    print('area = {0:.6e} au^2'.format(area*4.4683677582981e-23))

    t = 4.5e9
    jupiter.updateSwarm(t)
    area = jupiter.computeAtot()
    print('area at t = 4.5e9 years: {0:.6e} au^2'.format(area*4.4683677582981e-23))

if __name__ == '__main__':
    main()
