pipeline {
    agent any
    environment {
        // Environment variables if needed
        REPO_URL = 'https://github.com/JcCassano/2202186_PracticalTest.git'
        DEPENDENCY_CHECK_CMD = 'dependency-check --noupdate'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code from GitHub...'
                git url: "${REPO_URL}", branch: 'main'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add build commands here, e.g., for a Maven project:
                sh 'mvn clean install'
            }
        }
        stage('Dependency Check') {
            steps {
                echo 'Running dependency check...'
                // Ensure you have the dependency-check tool installed and configured
                sh "${DEPENDENCY_CHECK_CMD}"
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test commands here, e.g., for a Maven project:
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add your deployment commands here
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // Perform any necessary cleanup here
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
