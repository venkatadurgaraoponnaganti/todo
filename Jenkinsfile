pipeline {
agent any
stages {
 stage('checkout'){
	steps{
	git branch:'master', url:'https://github.com/venkatadurgaraoponnaganti/todo'
}}
 stage('build'){
	steps{
		sh ''' docker build -t todoo . '''
}}
stage('deploy'){
	steps{
		sh ''' docker run -d -p 5000:5000 todoo '''
}}
}}

