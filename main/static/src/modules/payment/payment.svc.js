(function (ng) {
    var mod = ng.module('paymentModule');

    mod.service('paymentService', ['$http', 'paymentContext', function ($http, context) {

        this.svcPayCart = function (data) {
            return $http({
                method: 'POST',
                url: '/payment',
                data:data
            });
        };

    }]);
})(window.angular);