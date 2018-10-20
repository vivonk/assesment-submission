## TO connect to remote server, just go to the directory where you downloaded key-pair file, a .pem file
## And then if you are using windows then go for Putty (Search it google about how to login to remote AMI server using Putty) and if ubuntu/linux then
	> chmod 400 <pem-file-name>.pem
	

	> ssh -i <pem-file-name>.pem ubuntu@ip-address-of-the-server

## Once you login to remote server, install elastic search with the help of this https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

or run following commands on remote server, one by one
### First install JAVA
	> sudo add-apt-repository ppa:webupd8team/java
	

	> sudo apt update; sudo apt install oracle-java8-installer


	 reference for this is here : http://tipsonubuntu.com/2016/07/31/install-oracle-java-8-9-ubuntu-16-04-linux-mint-18/ (install java 8)
	
### Then setup the java_home path
	> sudo nano ~/.bashrc

	and once it will open file, go to end and append this 
	
	> export JAVA_HOME='/usr/lib/jvm/java-8-oracle'
	
	use ctlr-c and then yes to save file
	
	
	and then reload the bash rc file
	
	> source ~/.bashrc


### Now install the elastic search

	> wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.4.2.deb
	> wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.4.2.deb.sha512
	> shasum -a 512 -c elasticsearch-6.4.2.deb.sha512 
	> sudo dpkg -i elasticsearch-6.4.2.deb 
	> sudo /bin/systemctl daemon-reload
	> sudo /bin/systemctl daemon-reloadsudo /bin/systemctl enable elasticsearch.service


	Elasticsearch can be started and stopped as follows:

	> sudo systemctl start elasticsearch.service
	> sudo systemctl stop elasticsearch.service

	to cross verify, check the logs 

	> sudo journalctl --unit elasticsearch

	now final verification, run this and check json response
	 > curl -X GET "localhost:9200/"
