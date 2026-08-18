pipeline {
    agent none

    stages {

        stage('Checkout') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            agent {
                docker {
                    image 'python:3.12'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            agent {
                docker {
                    image 'python:3.12'
                }
            }
            steps {
                sh 'python -m pytest'
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