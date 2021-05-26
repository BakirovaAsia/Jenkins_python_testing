pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.agent'
            args '-u 0:0 -v /var/run/docker.sock:/var/run/docker.sock'
            }
        }
        
    stages {
        stage ('Get source') {
            steps {
                git url: 'https://github.com/BakirovaAsia/Jenkins_python_testing.git'
            }
        }
        stage ('Testing') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'cd ./Jenkins_python_testing'
                sh 'pytest'
             }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}