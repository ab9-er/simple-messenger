# SIMPLE MESSENGER

Simple-Messenger uses flask-socketio to establish communication between clients.

It contains a Makefile which lets start the server as below.

    make run

Once started, to get the IP address of the server do the following.

If you use `docker-machine`,

    SIMPLE_SERVER=$(echo $DOCKER_HOST | cut -d '/' -f3 | cut -d ':' -f1)

else if you use `docker-for-mac`

    SIMPLE_SERVER=$(ifconfig en0 | grep 'inet' | cut -d " " -f2)

head over to `${SIMPLE_SERVER}:5000`
