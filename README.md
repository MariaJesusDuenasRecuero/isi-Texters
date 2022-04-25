

# SPRINT 4 - DESPLIEGUE

imagen docker: https://drive.google.com/file/d/1zwNsdA_rj4HN8K3L9QhHHciwelzMSyAM/view?usp=sharing

Wiki of the project:https://github.com/MJesusGit/isi-Texters/wiki

## Importante para hacer funcionar el contenedor Docker
Al hacer build, es necesario instalar algunos paquetes apt para que funcione. 
Los pasos son:
1. sudo docker run -it texters_final bash
2. apt-get -y update
3. apt-get -y install tesseract-ocr
4. apt-get -y install ocrmypdf

Después hacer commit del container con: `docker commit --change='CMD ["./run_server.sh"]' -c "EXPOSE 5000" [CONTAINER_ID] texters_final:latest`
