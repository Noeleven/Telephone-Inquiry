'use strict';

/*services*/

//登录服务

var LoginService = angular.module('LoginService',['ngResource']);

LoginService.factory('Login',['$resource',
    function($resource){
        return $resource('/scgi/login',{},{
	    query:{method:'GET',isArray:false}
	});
    }]);

var SwitchService = angular.module('SwitchService',['ngResource']);

SwitchService.factory('Switch',['$resource',
    function($resource){
	return $resource('/scgi/switch',{},{
	    query:{method:'GET',isArray:true}
	});
    }]);

var MainService = angular.module('MainService',['ngResource']);

MainService.factory('Input',['$resource',
    function($resource){
	return $resource('/scgi/input');
    }]);
MainService.factory('Modify',['$resource',
    function($resource){
	return $resource('/scgi/modify');
    }]);
MainService.factory('Delete',['$resource',
    function($resource){
	return $resource('/scgi/delete');
    }]);
MainService.factory('Modifypage',function(){
	return {
	    id:"null",
	    name:"null",
	    mphone:"null",
	    nphone:"null",
	    mail:"null",
	    position:"null"
	}
    });
