(function (ng) {
    var mod = ng.module('mainModule');

    mod.controller('mainCtrl', ['$scope', 'mainService', function ($scope, mainService) {

        function responseError(response) {
            console.log(response);
        }

        this.isLogged = function () {
            return mainService.isLogged().then(function (response) {
                $scope.message = response.data;
                console.log($scope.message)
            }, responseError);
        };

        this.logOut = function () {
            return mainService.logOut().then(function (response) {
                $scope.message.logged = false;
            }, responseError);
        };

    }]);
})(window.angular);
