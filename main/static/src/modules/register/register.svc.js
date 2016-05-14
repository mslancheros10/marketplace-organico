(function (ng) {
    var mod = ng.module('registerModule');

    mod.service('registerService', ['$http', 'registerContext', function ($http, context) {

        this.geocoderAddress = function (address) {
            return $http({
                method: 'GET',
                url: 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=AIzaSyCL1qoAd2fWDwWM8y-SyngJ42ywrReHAEM'
            });
        };

        this.registerProvider = function (provider) {
            return $http({
                method: 'POST',
                url: 'register/provider',
                data: provider
            });
        };

        this.registerClient = function (client) {
            return $http({
                method: 'POST',
                url: 'register/client',
                data: client
            });
        };


    }]);
})(window.angular);
