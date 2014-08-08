'use strict';

/*Route config*/

angular.module('PhoneApp',[
    'ui.router',
    'ngResource',

    'LoginService',
    'SwitchService',
    'MainService',
    'PageController',
    'TableController',
    'timer'
    ])
.config(function($stateProvider,$urlRouterProvider){

	  $urlRouterProvider.otherwise('/login');
	  
	  $stateProvider
	    .state('login',{
		     url:'/login',
		     controller:'LoginCtrl'
		 })
             .state('main',{
		     url:'/main',
		     templateUrl:'/views/main.html',
		     controller:'MainCtrl'
		 })
	     .state('main.switch',{
		     url:'/switch',
		     templateUrl:'/views/switch.html',
		     controller:'SwitchCtrl'
		 })
	     .state('main.input',{
		     url:'/input',
		     templateUrl:'views/input.html',
		     controller:'InputCtrl'
		 })
	     .state('main.modify',{
		     url:'/modify?id',
		     templateUrl:'/views/modify.html',
		     controller:'ModifyCtrl'
		     })
	 });
	  
