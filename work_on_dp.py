<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>Jupyter Notebook</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="/static/base/images/favicon.ico?v=97c6417ed01bdc0ae3ef32ae4894fd03">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=3c2a865c832a1322285c55c6ed99abb2" type="text/css" />
    <link rel="stylesheet" href="/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=9df10041c3e07da766e7c48dd4c35e4a" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    

    <link rel="stylesheet" href="/static/style/style.min.css?v=2165fc0d023f0baf5cce3b2a6db40e22" type="text/css"/>
    
<link rel="stylesheet" href="/static/auth/css/override.css?v=ae668279c8a80c1d2e81fc28345169ee" type="text/css" />

    <link rel="stylesheet" href="/custom/custom.css" type="text/css" />
    <script src="/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/static/components/react/react.production.min.js?v=34f96ffc962a7deecc83037ccb582b58" type="text/javascript"></script>
    <script src="/static/components/react/react-dom.production.min.js?v=b14d91fb641317cda38dbc9dbf985ab4" type="text/javascript"></script>
    <script src="/static/components/create-react-class/index.js?v=94feb9971ce6d26211729abc43f96cd2" type="text/javascript"></script>
    <script src="/static/components/requirejs/require.js?v=951f856e81496aaeec2e71a1c2c0d51f" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200329200650",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

</head>

<body class=""
 
  
 
dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="/tree" title='dashboard'>
      <img src='/static/base/images/logo.png?v=641991992878ee24c6f3826e81054a0f' alt='Jupyter Notebook'/>
  </a></div>

  
  
  
  
  
  


  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site">


<div id="ipython-main-app" class="container">

    
    
    <div class="row">
    <div class="navbar col-sm-8">
      <div class="navbar-inner">
        <div class="container">
          <div class="center-nav">
            <form action="/login?next=%2Fnbconvert%2Fscript%2Ftraining%2Fdouble_pend%2Fdouble_pendulum-master%2Fwork_on_dp.ipynb%3Fdownload%3Dtrue" method="post" class="navbar-form pull-left">
              <input type="hidden" name="_xsrf" value="2|26881ef2|14ad29b144ba28c540b17b9103bf5d9317bc7a9617bf269640b12ecb10be299014bf7b9713ba29c012b029c71fb07bd711cb2fc71ebd2cca16b92ac3|1585490905"/>
              
                <label for="password_input"><strong>Password:</strong></label>
              
              <input type="password" name="password" id="password_input" class="form-control">
              <button type="submit" class="btn btn-default" id="login_submit">Log in</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    </div>
    
    
    
</div>


</div>








<script type="text/javascript">
  require(["auth/js/main"], function (auth) {
    auth.login_main();
  });
</script>



<script type='text/javascript'>
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>
</body>

</html>