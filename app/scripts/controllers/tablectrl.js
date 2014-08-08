'use strict';

angular.module('TableController',['ngTable','ngTableResizableColumns'])
.controller('SwitchCtrl',//['$scope','Switch','Modifypage','$filter','$cookies','$state','ngTableParams',
    function($scope,Switch,Modifypage,$filter,$state,ngTableParams){
	    $scope.$broadcast('timer-start');
	    $scope.timerRunning = true;
        $scope.tableParams = new ngTableParams({
	        page:1,
	        count:50,
			filter:{},
			sorting:{
				position:''
		    }
	    },{
	        total:0,
	        getData:function($defer,params){
                   Switch.query(function(get_data){
		       $scope.data = get_data;
		       var filteredData = params.filter() ?
		           $filter('filter')(get_data,params.filter()):
		           get_data;
		       var orderedData = params.sorting() ?
		           $filter('orderBy')(filteredData,params.orderBy()):
		           get_data;
		       params.total(orderedData.length);
		       $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
		})
	      }
	    });
	    $scope.skip_list = function(mess){
	       Modifypage.id = mess.id;
           Modifypage.name = mess.name;
	       Modifypage.mphone = mess.mphone;
	       Modifypage.nphone = mess.nphone;
	       Modifypage.mail = mess.mail;
	       Modifypage.position = mess.position;
	       $state.go('main.modify');
	    };

    }
 )
.controller('ModifyCtrl',function($scope,$state,$modal,Modify,Delete,Modifypage){
	$scope.user = Modifypage;
        $scope.back = function(){
	       $state.go('main.switch');
	    };
	$scope.tomodify = function(size){
	     Modify.save($scope.user,function(data){
	         if (data.modify_ok == "ok"){
		      $state.go('main.switch');
		      var modalInstance = $modal.open({
                         templateUrl:'views/modify_confirm.html',
		         controller:ModCtrl,
		         size:size
		      });
		  }
		  else{
		      $scope.warning_show = true;
		      $scope.response = "好像有问题呀，请检查";
		  }
		})
	 };
        $scope.todelete = function(size){
            var modalInstance = $modal.open({
		templateUrl:'views/delete_warning.html',
		controller:DeleteCtrl,
		size:size
		});
	};
	var DeleteCtrl = function($scope,$state,$modalInstance){
            $scope.username = Modifypage.name;
            $scope.ok = function(){
	        Delete.save(Modifypage,function(data){
	           $modalInstance.close();
	           if (data.del_ok == "ok"){
		       $state.go('main.switch');
		   }
	        });
           };
           $scope.cancel = function(){
	       $modalInstance.dismiss('cancle');
           };
       };
       var ModCtrl=function($scope,$modalInstance){
	        $scope.ok = function(){
                    $modalInstance.close();
	        };
       };
   });
