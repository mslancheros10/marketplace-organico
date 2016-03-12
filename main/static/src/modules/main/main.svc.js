(function (ng) {
    var mod = ng.module('mainModule');

    mod.service('mainService', ['$http', 'mainContext', function ($http, context) {

        this.isLogged = function () {
            return $http({
                method: 'GET',
                url: '/islogged'
            });
        };

        this.logOut = function () {
            return $http({
                method: 'GET',
                url: '/logout'
            });
        };

    }]);
})(window.angular);