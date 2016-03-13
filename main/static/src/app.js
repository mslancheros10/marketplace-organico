(function (ng) {

    var marketplaceOrganico = ng.module('marketplaceOrganico', [
        'ngRoute',
        'mainModule',
        'basketsModule',
    ]);

    marketplaceOrganico.config(['$routeProvider', function ($routeProvider) {

        $routeProvider
            .when('/main', {
                templateUrl: 'static/src/modules/main/main.tpl.html',
                controller: 'mainCtrl',
                controllerAs: 'ctrl'
            })
            .when('/baskets', {
                templateUrl: 'static/src/modules/baskets/baskets.tpl.html',
                controller: 'basketsCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/main');

    }]);
})(window.angular);
