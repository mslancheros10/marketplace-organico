(function (ng) {
    var mod = ng.module('basketsModule');

    mod.controller('basketsCtrl', ['$scope','$filter', 'basketsService','$window', function ($scope,$filter, basketsService,$window) {

        $scope.loading = true;

        $scope.filteredBaskets = [];
        $scope.currentPage = 1;
        $scope.numPerPage = 6;
        $scope.maxSize = 10;

        $scope.$watch('search', function(val) {
            $scope.filteredBaskets = $scope.baskets
            $filter('filter')($scope.filteredBaskets, val);
        });

        $scope.$watch('currentPage + numPerPage', function() {
            var begin = (($scope.currentPage - 1) * $scope.numPerPage);
            var end = begin + $scope.numPerPage;

            $scope.filteredBaskets = $scope.baskets.slice(begin, end);
        });

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getBaskets = function () {
            return basketsService.getBaskets().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.baskets = response.data;
                    var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                    var end = begin + $scope.numPerPage;

                    $scope.filteredBaskets = $scope.baskets.slice(begin, end);
            }, responseError);
        };

        this.shareTwitter = function(){

            $window.open("https://twitter.com/intent/tweet?text=Encontré estas canastas orgánicas, visita:&url=https://grupo5-marketplace-organico.herokuapp.com/%23/baskets&via=MpOrganico");

        }

    }]);
})(window.angular);
