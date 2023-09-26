pipeline {
    agent any

    stages {
        stage('Build docker images') {
//             agent{
//                 docker{
//                     image 'flaskapp:2.3.3'
//                     reuseNode true
//                 }
//             }
            steps {
                echo 'Building...'
                sh "docker build -t flaskapp::2.3.3 ."
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
                 sh "docker run -d -p 5000:80 flaskapp:2.3.3"
            }
        }
    }
}