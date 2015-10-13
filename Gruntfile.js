module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: ['nadej/nadej.js'],
        dest: 'build/<%= pkg.name %>.min.js'
      }
    },
    concat: {
      js: {
          src : [
                'node_modules/bootstrap/**/*.min.js',
                'node_modules/bootstrap-table/**/*.min.js',
            ],
          dest:'nadej/concated.js'
        },
      ss: {
          src : [
                    'node_modules/bootstrap/**/*.min.css',
                    'node_modules/bootstrap-table/**/*.min.css',
                ],
          dest : 'nadej/concated.css'
        },
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');

  // Default task(s).
  grunt.registerTask('default', ['concat','uglify']);

};

