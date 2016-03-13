(function (ng) {
    var mod = ng.module('basketsModule');

    mod.controller('basketsCtrl', ['$scope', 'basketsService', function ($scope, basketsService) {

        function responseError(response) {
            console.log(response);
        }

        this.getBaskets = function () {
            return basketsService.getBaskets().then(function (response) {
                console.log(response);
                $scope.baskets = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
