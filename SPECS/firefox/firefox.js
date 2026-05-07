pref("app.update.auto", false);
pref("app.update.enabled", false);
pref("app.update.autoInstallEnabled", false);
pref("browser.policies.perUserDir", true);

// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Disable DoH by default
pref("network.trr.mode", 5);

// Enable GNOME Shell search provider
pref("browser.gnome-search-provider.enabled", true);

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Branding
pref("browser.startup.homepage", "data:text/plain,browser.startup.homepage=https://openruyi.cn/");
