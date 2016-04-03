(function (ng) {
    var mod = ng.module('loginModule');

    mod.controller('loginCtrl', ['$scope', 'loginService', function ($scope, loginService) {

        $scope.user = {};

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.logIn = function () {
            return loginService.logIn($scope.user.username,$scope.user.password).then(function (response) {
                $scope.message = response.data;
                console.log('logged  = ' + $scope.message)
                if($scope.message.message !== 'OK'){
                    console.log('error')
                    $scope.error = true;
                }else {
                    $scope.error = false;
                    $scope.user = {};
                    $('#loginModal').modal('hide')
                    window.location.assign('#/main');
                    window.location.reload(true);
                }
            }, responseError);
        };

    }]);
})(window.angular);
