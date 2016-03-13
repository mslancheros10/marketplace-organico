(function (ng) {
    var mod = ng.module('basketsModule');

    mod.controller('basketsCtrl', ['$scope', 'basketsService', function ($scope, basketsService) {

        $scope.loading = true;

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getBaskets = function () {
            return basketsService.getBaskets().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.baskets = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
