pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'dotnet build Software_Calculator.sln'
      }
    }

    stage('Tests') {
      parallel {
        stage('Unit') {
          steps {
            sh 'dotnet test test/UnitTests'
          }
        }

        stage('Integration') {
          steps {
            sh 'dotnet test tests/IntegrationTests'
          }
        }

        stage('Functional') {
          steps {
            sh 'dotnet test tests/FunctionalTests'
          }
        }

      }
    }

    stage('Deployment') {
      steps {
        sh 'dotnet publish Software_Calculator.sln  -o /var/aspnet'
      }
    }

  }
}