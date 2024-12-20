
**Cours Organisé sur les Réseaux Mobiles**

Pour maîtriser les réseaux mobiles en tant qu'administrateur, il est essentiel de comprendre leurs principales composantes, dans un ordre logique correspondant à leur architecture :  

- Réseau d'Accès Radio (RAN)  
- Réseau de Transport (Transport Network)  
- Réseau Cœur (Core Network)  
- Systèmes de Gestion des Réseaux (NMS)  
- OSS/BSS  
- Technologies et Concepts Complémentaires  

### 1. Réseau d'Accès Radio (RAN)  
Le RAN connecte les appareils des utilisateurs au réseau via des signaux radio.  

#### 1.1. Composants clés du RAN  

- **Stations de base** :  
  - BTS (Base Transceiver Station) : Utilisée dans les réseaux 2G.  
  - NodeB : Utilisée dans les réseaux 3G.  
  - eNodeB (LTE) : Fournit des débits plus élevés et gère à la fois la radio et certaines fonctions réseau.  
  - gNodeB (5G) : Supporte des communications à très faible latence et des débits ultra-rapides.  
- **Antennes** : Transmettent et reçoivent les signaux radio.  

#### 1.2. Technologies radio  

- 2G (GSM) : Fournit appels et SMS, avec des données limitées (GPRS, EDGE).  
- 3G (UMTS) : Augmente les débits grâce à WCDMA (Wideband CDMA).  
- 4G (LTE) : Basé uniquement sur IP, offre des débits jusqu'à 1 Gbps.  
- 5G NR (New Radio) : Prend en charge des cas d'usage avancés (IoT massif, réalité augmentée, etc.).  

#### 1.3. Défis dans le RAN  

- Gestion des interférences entre cellules.  
- Optimisation de la couverture pour garantir une bonne qualité de service (QoS).  
- Déploiement de petites cellules pour améliorer la capacité dans les zones denses.  

### 2. Réseau de Transport (Transport Network)  
Le réseau de transport relie le RAN au réseau cœur, en acheminant les données et en garantissant une connectivité fiable.  

#### 2.1. Rôles principaux  

- **Backhaul** : Connecte les stations de base (RAN) au Core Network.  
- **Fronthaul** : Relie les antennes au matériel de traitement centralisé (C-RAN).  
- **Transport des données** : Acheminement des paquets IP, voix et vidéo.  

#### 2.2. Technologies utilisées  

- Fibre optique : Grande capacité et faible latence.  
- Micro-ondes : Alternative pour les zones difficiles d'accès.  
- MPLS (Multiprotocol Label Switching) : Segmentation du trafic pour garantir la QoS.  

#### 2.3. Défis dans le transport  

- Assurer une faible latence, surtout pour les applications critiques (5G).  
- Dimensionner correctement la capacité pour gérer les pics de trafic.  

### 3. Réseau Cœur (Core Network)  
Le Core Network est le centre névralgique qui gère la connectivité, la mobilité et les services pour les utilisateurs.  

#### 3.1. Composants clés  

- **Mobile Switching Center (MSC)** : Gestion des appels dans les réseaux 2G/3G.  
- **Serving Gateway (SGW) et Packet Gateway (PGW)** : Transport des données dans les réseaux LTE.  
- **Home Subscriber Server (HSS)** : Base de données des informations des abonnés.  
- **AMF/SMF (5G)** :  
  - AMF : Gestion de l'accès et de la mobilité.  
  - SMF : Gestion des sessions IP.  

#### 3.2. Fonctions principales  

- Gestion de la mobilité : Permet la connectivité continue des utilisateurs.  
- Authentification et sécurité : Assure l'accès sécurisé au réseau.  
- Routage des données : Acheminement des paquets vers Internet ou d'autres réseaux.  

#### 3.3. Évolutions récentes  

- **4G LTE Core (EPC)** : Basé uniquement sur IP, remplace les infrastructures orientées circuit.  
- **5G Core** : Utilise la virtualisation des fonctions réseau (NFV) et le découpage réseau (Network Slicing).  

### 4. Systèmes de Gestion des Réseaux (NMS)  
Le NMS (Network Management System) est une plateforme utilisée pour surveiller, gérer et optimiser les équipements réseau.  

#### 4.1. Fonctionnalités  

- Surveillance : Analyse en temps réel des performances réseau via des KPI.  
- Détection des pannes : Identification rapide des problèmes.  
- Automatisation : Déploiement de configurations et mises à jour logicielles.  

#### 4.2. Exemples de solutions NMS  

- Ericsson ENM (Ericsson Network Manager).  
- Nokia NetAct.  
- Huawei iManager.  

### 5. OSS/BSS  

Les OSS (Operational Support Systems) et BSS (Business Support Systems) gèrent les aspects opérationnels et commerciaux du réseau.  

#### 5.1. OSS  

- Gestion des performances : Surveillance et optimisation du réseau.  
- Provisioning : Activation et configuration des services pour les utilisateurs.  
- Gestion des ressources : Suivi des équipements physiques et logiques.  

#### 5.2. BSS  

- Facturation : Calcul des coûts pour les appels, données, etc.  
- Gestion des abonnés : Création et modification des profils utilisateurs.  
- Support client : Interfaces pour répondre aux requêtes des clients.  

### 6. Technologies et Concepts Complémentaires  

#### 6.1. Sécurité du réseau  

- Chiffrement : Protection des données échangées.  
- Protection contre les attaques : Prévention des intrusions et des attaques DDoS.  

#### 6.2. NFV (Network Function Virtualization) et SDN (Software-Defined Networking)  

- NFV : Virtualisation des fonctions réseau pour réduire les coûts et améliorer la flexibilité.  
- SDN : Contrôle centralisé pour gérer efficacement le trafic.  

#### 6.3. Edge Computing  

- Permet de traiter les données à proximité des utilisateurs, réduisant ainsi la latence.  

### Compétences pour un Administrateur Réseau Mobile  

- Connaissance des protocoles : IP, GTP, MPLS, etc.  
- Maîtrise des outils NMS et OSS/BSS.  
- Compréhension des technologies radio (2G, 3G, 4G, 5G).  
- Analyse des logs réseau pour le dépannage.  
- Expertise en sécurité : Prévention des menaces et gestion des accès.  

### Conclusion  

Un réseau mobile est un écosystème complexe reliant le RAN, le transport et le cœur. Les outils de gestion (NMS, OSS/BSS) et les technologies émergentes (NFV, SDN, 5G) jouent un rôle crucial. Une bonne compréhension de ces composants permet d'optimiser et de sécuriser un réseau mobile moderne.  

---
