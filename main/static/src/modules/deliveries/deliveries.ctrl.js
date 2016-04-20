(function (ng) {
    var mod = ng.module('deliveriesModule');

    mod.controller('deliveriesCtrl', ['$scope', 'deliveriesService', function ($scope, deliveriesService) {

        $scope.loading = true;

        $scope.filteredDeliveries = [];
        $scope.currentPage = 1;
        $scope.numPerPage = 6;
        $scope.maxSize = 10;

        $scope.$watch('search', function(val) {
            $scope.filteredDeliveries = $scope.deliveries
            $filter('filter')($scope.filteredDeliveries, val);
        });

        $scope.$watch('currentPage + numPerPage', function() {
            var begin = (($scope.currentPage - 1) * $scope.numPerPage);
            var end = begin + $scope.numPerPage;

            $scope.filteredDeliveries = $scope.deliveries.slice(begin, end);
        });

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getDates = function () {

            return deliveriesService.getDates().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.deliveries = response.data;

                var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                var end = begin + $scope.numPerPage;

                $scope.filteredDeliveries = $scope.deliveries.slice(begin, end);

            }, responseError);


        };

        this.initDates = function(){

            $scope.deliveries = {};

        };

    }]);
})(window.angular);
