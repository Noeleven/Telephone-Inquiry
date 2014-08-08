'use strict';

/*controllers of pages*/
angular.module('PageController',['ui.bootstrap','ngCookies'])

.controller('LoginCtrl',//['$rootScope','$scope','$state','login',
    function($state,$cookies,Login){
        Login.query(function(data){
	    delete $cookies.ip;
	    $cookies.ip = data.ip;
	    $state.go('main.switch');
	});
    }
)
.controller('MainCtrl',function($rootScope,$state,$scope,$cookies,$modal){
        $rootScope.footershow = true;
	//$scope.name = $cookies.name;
	$rootScope.msg = {
            version:"v2.0-beta2",
	    ip:$cookies.ip
        };
	$rootScope.loginTime = new Date();
	$scope.quit = function(size){
	    var modalInstance = $modal.open({
                templateUrl:'views/quit_warning.html',
		controller:QuitCtrl,
		size:size});
	};
	var QuitCtrl=function($scope,$state,$modalInstance){
	   $scope.ok = function(){
	    $scope.$broadcast('timer-stop');
	    $scope.timerRunning = false;
            $modalInstance.close($state.go('login'));
	   };
	   $scope.cancel = function(){
             $modalInstance.dismiss('cancle');
	   };
       };
    })
.controller('InputCtrl',function($scope,$state,$modal,Input){
	$scope.response = '';
	$scope.warning_show = false;
	$scope.user = {
	    name:'',
	    mphpone:'',
	    nphone:'',
	    mail:'',
	    position:''
	}
	$scope.toInput = function(size){
	    Input.save($scope.user,function(data){
	        if (data.input_ok == "ok"){
		    $state.go('main.switch');
	            var modalInstance = $modal.open({
                         templateUrl:'views/input_confirm.html',
		         controller:InputCtrl,
		         size:size
		    });
		}
		else if(data.input_ok == "being"){
		    $scope.warning_show = true;
		    $scope.response = "该姓名已经存在";
		}
		else { 
		    $scope.warning_show = true;
		    $scope.response = "好像出问题了哦！";
		}
	    });
	   var InputCtrl=function($scope,$state,$modalInstance){
	        $scope.ok = function(){
                    $modalInstance.close();
	        };
           };
        }
    })
