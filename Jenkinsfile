pipeline {
    agent any
    
    environment {
        ANSIBLE_PATH = "${WORKSPACE}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Prepare') {
            steps {
                echo 'Vorbereitung der Deployment-Umgebung...'
                sh 'which ansible || echo "Ansible nicht gefunden"'
                sh 'which docker || echo "Docker nicht gefunden"'
            }
        }
        
        stage('Deploy Dev') {
            when {
                branch 'develop'
            }
            steps {
                echo 'Deployment in die Development-Umgebung...'
                sh 'cd ${ANSIBLE_PATH} && ansible-playbook setup_multi_env_app.yml -i inventory.yml --extra-vars "target_env=development"'
            }
        }
        
        stage('Deploy Release') {
            when {
                branch 'release'
            }
            steps {
                echo 'Deployment in die Release-Umgebung...'
                sh 'cd ${ANSIBLE_PATH} && ansible-playbook setup_multi_env_app.yml -i inventory.yml --extra-vars "target_env=release"'
            }
        }
        
        stage('Deploy Production') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deployment in die Produktions-Umgebung...'
                sh 'cd ${ANSIBLE_PATH} && ansible-playbook setup_multi_env_app.yml -i inventory.yml --extra-vars "target_env=production"'
            }
        }
    }
    
    post {
        success {
            echo 'Deployment erfolgreich!'
        }
        failure {
            echo 'Deployment fehlgeschlagen!'
        }
    }
}