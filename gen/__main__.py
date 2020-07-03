from os import listdir, makedirs
from sys import argv

from Combinations import Combinations

if len(argv) > 1:
	print('Too many arguments')
	exit(1)

dockerTemplates = {}
for templateFile in listdir('templates'):
	templateName = templateFile.split('.')[0]
	with open('templates/' + templateFile, 'r') as dockerfile:
		dockerTemplates[templateName] = dockerfile.read()
with open('templates/Makefile', 'r') as makefile:
	makefileTemplate = makefile.read()

for combination in Combinations:
	os = combination.os
	swift = combination.swift
	
	make = makefileTemplate
	docker = dockerTemplates[os.name]
	
	docker = docker.replace('{OS.Version}', os.version.toString(2))
	docker = docker.replace('{OS.Requirements.Key}', os.DockerInstall(combination.keyDependencies))
	docker = docker.replace('{OS.Requirements.Build}', os.DockerInstall(combination.buildDependencies))
	docker = docker.replace('{OS.Requirements.Deploy}', os.DockerInstall(combination.deployDependencies))
	docker = docker.replace('{Swift.URL}', swift.URL(os))
	
	make = make.replace('{Docker.Commands.Build}', combination.DockerBuildCommands())
	make = make.replace('{Docker.Commands.Tag}', combination.DockerTagCommands())
	make = make.replace('{Docker.Commands.Push}', combination.DockerPushCommands())
	
	directory = 'docker/{}/{}'.format(os.name + os.version.String(), swift.Name())
	makedirs(directory, exist_ok=True)
	with open(directory + '/Dockerfile', 'w') as dockerfile:
		dockerfile.write(docker)
	with open(directory + '/Makefile', 'w') as makefile:
		makefile.write(make)
