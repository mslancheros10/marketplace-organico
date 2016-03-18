(function (ng) {
    var mod = ng.module('providersModule');

    mod.controller('providersCtrl', ['$scope', 'providersService', function ($scope, providersService) {

        $scope.loading = true;

        $scope.filteredProviders = [];
        $scope.currentPage = 1;
        $scope.numPerPage = 6;
        $scope.maxSize = 10;

        $scope.$watch('search', function(val) {
            $scope.filteredProviders = $scope.providers
            $filter('filter')($scope.filteredProviders, val);
        });

        $scope.$watch('currentPage + numPerPage', function() {
            var begin = (($scope.currentPage - 1) * $scope.numPerPage);
            var end = begin + $scope.numPerPage;

            $scope.filteredProviders = $scope.providers.slice(begin, end);
        });

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getProviders = function () {
            return providersService.getProviders().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.providers = response.data;

                var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                var end = begin + $scope.numPerPage;

                $scope.filteredProviders = $scope.providers.slice(begin, end);

            }, responseError);
        };

    }]);
})(window.angular);
