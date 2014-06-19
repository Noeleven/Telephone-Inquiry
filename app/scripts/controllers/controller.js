'use strict';

angular.module('phoneControllers',[])
.controller('searchCtrl',['$scope','$http',
	function($scope,$http){
		//定义customer
		var customer = $scope.customer ={};
		customer.items=[];
		customer.checkAll = function(checked){
			angular.forEach(customer.items,function(item){
				item.$checked = checked;
			});
		};
		customer.selection = function(){
			return _.where(customer.items,{$checked:true});
		};
		//给customer获取数据
		$http.get('info.json').success(function(data){
			customer.items = data;
		});
		//define pages model
		$scope.pages = [5,10,20,50,100];
		$scope.mypage = $scope.pages[0]
    }
	])
.controller('inputCtrl',[
	]);