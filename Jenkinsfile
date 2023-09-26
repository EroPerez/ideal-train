pipeline {
    agent any

    stages {
        stage('Build docker images') {
            steps {
                echo 'Building docker image..'
                sh 'docker build -t flaskapp:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}