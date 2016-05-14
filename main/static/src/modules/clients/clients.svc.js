(function (ng) {
    var mod = ng.module('clientsModule');

    mod.service('clientsService', ['$http', 'clientsContext', function ($http, context) {

        this.getClient = function () {
            return $http({
                method: 'POST',
                url: '/client'
            });
        };

        this.updateClient = function (client) {
            return $http({
                method: 'POST',
                url: 'client/update',
                data: client
            });
        };


    }]);
})(window.angular);
