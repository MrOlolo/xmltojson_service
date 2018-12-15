# xmltojson_service
Simple service. Convert XML -> JSON

## How it works:
### Start service:

- #### You can build only image with gradle and run it with necessary options:

  `./gradlew buildImage`
  
  `docker run [OPTIONS] serv:latest (example:  docker run --rm -p 80:80 serv:latest)`
    
- #### You can create container with gradle and start it:

  `./gradlew createContainer`
  
  `docker start xmltojson_service`
    
- #### You can start container with gradle:

  `./gradlew startContainer`

### Send file:

    curl -d @test.xml http://localhost/postxml
