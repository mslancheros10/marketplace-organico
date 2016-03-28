(function (ng) {
    var mod = ng.module('providersModule');

    mod.service('providersService', ['$http', 'providersContext', function ($http, context) {

        this.getProviders = function () {
            return $http({
                method: 'GET',
                url: '/providers'
            });
        };

    }]);
})(window.angular);