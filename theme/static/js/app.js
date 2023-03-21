var nav = new Vue({
    el: '#nav',
    data() {
        return {
            home: 'Home',
            team: 'Team',
            search: 'Search',
        };
    },
    methods: {
    },
});

var team = new Vue({
    el: '#team',
    data() {
        return {
            dtravisany: {
                name: 'Dante Travisany',
                role: 'Researcher',
                photo: '../static/imgs/dtravisany.jpeg',
            },
            pcogram: {
                name: 'Patricia Cogram',
                role: 'Researcher',
                photo: '../static/imgs/pcogram.jpeg'
            },
            imartinez: {
                name: 'Irene Martinez',
                role: 'Researcher',
                photo: '../static/imgs/imartinez.jpeg'
            },
            curra: {
                name: 'Claudio Urra',
                role: 'Post Doc',
                photo: '../static/imgs/curra.jpeg'
            },
            fmarchese: {
                name: 'Franco Marchese',
                role: 'Research Assistant',
                photo: '../static/imgs/fmarchese.jpeg'
            }
        };
    },
});