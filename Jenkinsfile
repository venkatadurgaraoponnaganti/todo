pipeline {
    agent any

    environment {
        username = "pvdr8978"
        password = "PVdr@8978"
        name     = "todoo"
    }

    stages {

        stage('checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/venkatadurgaraoponnaganti/todo'
            }
        }

        stage('build') {
            steps {
                sh '''
                docker build -t $username/$name:latest .
                '''
            }
        }

        stage('deploy') {
            steps {
                sh '''
                echo "$password" | docker login -u "$username" --password-stdin
                docker push $username/$name:latest
                '''
            }
        }
    }
}

