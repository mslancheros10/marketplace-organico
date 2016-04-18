(function (ng) {

    var marketplaceOrganico = ng.module('marketplaceOrganico', [
        'ngRoute',
        'mainModule',
        'basketsModule',
        'productsModule',
        'providersModule',
        'loginModule',
        'shoppingItemsModule',
        'paymentModule',
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
            .when('/shoppingItems', {
                templateUrl: 'static/src/modules/shoppingItems/shoppingItems.tpl.html',
                controller: 'shoppingItemsCtrl',
                controllerAs: 'ctrl'
            })
            .when('/payf', {
                templateUrl: 'static/src/modules/payment/paymentFinished.tpl.html',
                controller: 'paymentCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/main');
    }]);
})(window.angular);
