(function (ng) {

    var marketplaceOrganico = ng.module('marketplaceOrganico', [
        'ngRoute',
        'mainModule',
        'basketsModule',
        'productsModule',
        'providersModule',
        'loginModule',
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
            .when('/providers', {
                templateUrl: 'static/src/modules/providers/providers.tpl.html',
                controller: 'providersCtrl',
                controllerAs: 'ctrl'
            })
            .when('/home', {
                templateUrl: 'static/src/modules/home/home.html',
                controller: '',
                controllerAs: ''
            })
            .otherwise('/main');

    }]);
})(window.angular);
