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
                sh 'cd ./UI_tests && pytest'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}