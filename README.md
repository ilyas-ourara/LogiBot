# 🤖 Autonomous Mobile Robot - ROS2 (Jazzy)

Ce projet met en place un **robot mobile autonome** utilisant **ROS 2 Jazzy**, avec les fonctionnalités suivantes :
- **Cartographie en temps réel (SLAM)** avec `slam_toolbox`
- **Navigation autonome** avec `Nav2`
- Visualisation dans **RViz**
- Exécution dans un environnement **Gazebo**

---

## 🚀 Objectif du projet

Permettre à un robot mobile de :
1. Se localiser et construire une carte de son environnement (SLAM)
2. Naviguer de façon autonome vers un objectif défini par l’utilisateur
3. Éviter les obstacles

---

## 🧩 Technologies utilisées

| Composant       | Rôle                                                    |
|------------------|---------------------------------------------------------|
| ROS2 Jazzy       | Framework robotique                                     |
| `slam_toolbox`   | Cartographie et localisation simultanées (SLAM)         |
| `Nav2`           | Navigation autonome (planification et contrôle)         |
| RViz             | Visualisation des capteurs, carte, trajectoire, etc.    |
| Gazebo           | Simulation du robot dans un environnement 3D            |

---

## ⚙️ Prérequis

- ROS2 Jazzy installé
- `colcon` installé
- Gazebo (simulator)
- Modèles Gazebo disponibles dans `/home/ilyas-ourara/Downloads/gazebo_models`

---

## 📦 Installation et Compilation

```bash
# 1. Cloner le projet
git clone https://github.com/yousefh112/autonomous_mobile_robot_ROS2_jazzy.git

# 2. Aller dans le dossier du package
cd autonomous_mobile_robot_ROS2_jazzy/car_nav2

# 3. Compiler
colcon build

# 4. Sourcer l’environnement
source install/setup.bash
