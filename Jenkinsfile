pipeline {
    agent none

    stages {

        stage('Checkout') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Test') {
    agent {
        docker {
            image 'python:3.12'
            args '-u root'
        }
    }
    steps {
        sh '''
            pip install -r requirements.txt
            python -m pytest
        '''
    }
}

        stage('Build Docker Image') {
            agent any
            steps {
                sh 'docker build -t anamarijakrsteska/docker-system-monitor-api:latest .'
            }
        }

        stage('Push Docker Image') {
            agent any
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push anamarijakrsteska/docker-system-monitor-api:latest
                    '''
                }
            }
        }
    }
}