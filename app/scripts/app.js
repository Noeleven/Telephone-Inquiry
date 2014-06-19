'use strict';

angular.module('testApp',['ngRoute','phoneControllers'])
.config(['$routeProvider',
    function($routeProvider){
        $routeProvider.
            when('/input',{
                templateUrl:'views/input.html',
				controller:'inputCtrl'
            }).
            when('/search',{
                templateUrl:'views/search.html',
				controller:'searchCtrl'
            }).
            otherwise({redirectTo:'/search'});
    }]);