;(function(namespace,settings,scout,subNamespace,w,d) {

	if (!w[namespace]) {
		w[namespace] = {};
	}
	if (!w[namespace][settings]) {
		w[namespace][settings] = {};
	}
	if (!w[namespace][settings][scout]) {
		w[namespace][settings][scout] = {};
	}

	/* Set some information about this scout file. */
	if (!w[namespace][settings][scout][subNamespace]) {
		w[namespace][settings][scout][subNamespace] ={
				name:"nbaLeaguePassScout",
				nonsecure:"z.cdn.",
				source:"http://z.cdn.turner.com/nba/tmpl_asset/static/nba-cms3-desktop/latest/js/pkgLeaguePass-min.js",
				secure:"s.cdn."
			};
	
		/* Get the current scout file. */
		var sct = w[namespace][settings][scout][subNamespace];
		/* Actually load the package. */
		d.write(unescape("%3Cscript src=\""+(sct.source.replace("http:","").replace(sct.nonsecure,(d.location.protocol == "http:"?sct.nonsecure:sct.secure)))+"\" %3E%3C/script%3E"));
	}

}("_nba","settings","scout","leaguepass",window,document));