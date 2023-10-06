pipeline {
    agent any

    stages {
        stage('Build docker images') {
            steps {
                echo 'Building...'
                sh "docker build -t flaskapp:2.3.3 ."
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker stop ideal_train_flask_app || true && docker rm ideal_train_flask_app || true"
                sh "docker run -d --name ideal_train_flask_app -p 80:5000 flaskapp:2.3.3"
            }
        }
    }
}