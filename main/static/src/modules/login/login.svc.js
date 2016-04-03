(function (ng) {
    var mod = ng.module('loginModule');

    mod.service('loginService', ['$http', 'loginContext', function ($http, context) {


        this.logIn = function (username,password) {
            return $http({
                method: 'POST',
                url: 'login/',
                data: {
                    username: username,
                    password: password
                }
            });
        };

    }]);
})(window.angular);
