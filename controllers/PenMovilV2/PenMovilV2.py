from controller import Robot, Motor
import math
pi = 3.14159265359
pi2= pi*2
print(pi)

def run_robot(robot):
    ##Optener el tiepo de pasos de la simulacion
    timestep = 64
    max_speed = pi2
    
    #-----------------------------------#
    ####Creacion instancias del motor####
    #-----------------------------------# 
    iMotor = robot.getDevice('left wheel motor')
    dMotor = robot.getDevice('right wheel motor')
    
    iMotor.setPosition(float('inf'))
    iMotor.setVelocity(0.0)

    dMotor.setPosition(float('inf'))
    dMotor.setVelocity(0.0)

    #-----------------------------------#
    #### Creacion instancias del GPS ####
    #-----------------------------------# 
    gps = robot.getDevice('gps')
    gps.enable(timestep)

    #-----------------------------------#
    ####Creacion instancias del sensor###
    #-----------------------------------#

    sIzquierda = robot.getDevice('left wheel sensor')
    sIzquierda.enable(timestep)
    
    sDerecha = robot.getDevice('right wheel sensor')
    sDerecha.enable(timestep)

    ps_values = [0,0]
    dist_values = [0,0]

    #-----------------------------------#
                ####Encoder####
    #-----------------------------------#
    wheel_radius = 0.025
    distance_between_wheels = 0.09

    wheel_cirum =   2 * pi  * wheel_radius
    encoder_unit = wheel_cirum / pi2

    #-----------------------------------#
            ####Posicion Robot####
    #-----------------------------------#

    robot_pose = [0,0,0] # x, y, theta
    last_ps_values = [0,0]


    while robot.step(timestep) != -1:
        
        ps_values[0] = sIzquierda.getValue()
        ps_values[1] = sDerecha.getValue()
        
        gps_value = gps.getValues() ###x, z, y
        print(gps_value)

        posx = gps_value[0]
        posx = gps_value[0]
        posx = gps_value[0]
        print(posx)

        print("---------------------------")
        #print(f"Valores de los sensores de posicion: Derecha {ps_values[1]} Izquierda {ps_values[0]}")

        for ind in range(2):
            diff = ps_values[ind] - last_ps_values[ind]
            if diff < 0.001:
                diff=0
                ps_values[ind] = last_ps_values[ind]
            
            dist_values[ind] = ps_values[ind] * encoder_unit
        
        ##Calcular velocdad angular y lineal}
        v = (dist_values[0] + dist_values[1])/2.0
        w = (dist_values[0] - dist_values[1])/distance_between_wheels

        dt = 1
        robot_pose[2] += ( w * dt)

        vx = v * math.cos(robot_pose[2])
        vy = v * math.sin(robot_pose[2])

        robot_pose[0] += (vx*dt)
        robot_pose[1] += (vy*dt)

        #print(f"Posicion Robot: {robot_pose}")

        #print(f"Valores de distancia: Derecha {dist_values[1]} Izquierda {dist_values [0]}")

        iMotor.setVelocity(max_speed)
        dMotor.setVelocity(max_speed)

        for ind in range(2):
            last_ps_values[ind] = ps_values[ind]
        
        pass

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)