(function (ng) {
    var mod = ng.module('deliveriesModule');

    mod.service('deliveriesService', ['$http', 'deliveriesContext', function ($http, context) {

        this.getDates = function () {
            return $http({
                method: 'GET',
                url: '/deliveries'
            });
        };

    }]);
})(window.angular);