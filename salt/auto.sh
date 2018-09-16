#!/bin/bash

MAIN_ADD_HOST=$1
create_host(){
        echo "create host ok"
}

deploy_service(){
    #salt 'linux-node2.example.com' state.sls nginx.install env=prod
    ADD_HOST_PORT="8090"
}

deploy_code(){
     echo "deploy code ok"
}

service_check(){
    STATUS=$(curl -s --head http://"$ADD_HOST":"$ADD_HOST_PORT"/ | grep '200 OK')
    if [ -n "$STATUS" ];then
        echo "ok"
    else
        echo "not ok"
        exit
    fi
}

etcd_key(){
  ADD_HOST=$1
  curl http://10.10.202.183:2379/v2/keys/salt/haproxy/backend_www_oldboyedu_com/$ADD_HOST -XPUT -d value="10.10.202.183:${ADD_HOST_PORT}"
}

sync_state(){
  salt 'cs-01' state.sls cluster.haproxy-outside saltenv=prod
}

main(){
  create_host;
  deploy_service;
  deploy_code;
  etcd_key $MAIN_ADD_HOST;
  sync_state;
}

main $1
