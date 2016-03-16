(function (ng) {
    var mod = ng.module('providersModule');

    mod.controller('providersCtrl', ['$scope', 'providersService', function ($scope, providersService) {

        $scope.loading = true;

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getProviders = function () {
            return providersService.getProviders().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.providers = response.data;
            }, responseError);
        };

    }]);
})(window.angular);

