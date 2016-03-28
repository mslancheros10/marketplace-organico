(function (ng) {
    var mod = ng.module('basketsModule');

    mod.service('basketsService', ['$http', 'basketsContext', function ($http, context) {

        this.getBaskets = function () {
            return $http({
                method: 'GET',
                url: '/baskets'
            });
        };

    }]);
})(window.angular);