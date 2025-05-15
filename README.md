






_______________________Un robot autonome capable de naviguer et d’éviter les obstacles en temps réel grâce à ROS 2 et Gazebo.__________________






🚀 Instructions d'exécution
🧩 1. Cloner le dépôt

git clone https://github.com/ilyas-ourara/LogiBot.git



⚙️ 2. Définir le chemin des ressources Gazebo
Avant de lancer les simulations, assurez-vous de définir la variable d’environnement suivante (à adapter selon votre chemin local) :

export GZ_SIM_RESOURCE_PATH=/home/ilyas-ourara/Downloads/gazebo_models



🛠️ 3. Compilation du projet

cd autonomous_mobile_robot_ROS2_jazzy/car_nav2
colcon build
source install/setup.bash


NOte : !!!!  Remplacez install/setup.bash par le chemin absolu si nécessaire, par exemple :
/home/ilyas-ourara/Desktop/ROS_PROJECT_3/autonomous_mobile_robot_ROS2_jazzy/car_nav2/install/setup.bash


🧪 4. Lancer la simulation
🧷 Terminal 1 : Démarrage du robot dans Gazebo

export GZ_SIM_RESOURCE_PATH=/home/ilyas-ourara/Downloads/gazebo_models
ros2 launch car_nav2 spawn_robot.launch.py




🧷 Terminal 2 : Lancement de la navigation avec SLAM

cd /home/ilyas-ourara/Desktop/ROS_PROJECT_3/autonomous_mobile_robot_ROS2_jazzy
source install/setup.bash
export GZ_SIM_RESOURCE_PATH=/home/ilyas-ourara/Downloads/gazebo_models
ros2 launch car_nav2 navigation_with_slam.launch.py
