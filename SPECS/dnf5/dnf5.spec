# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dnf5
Version:        5.4.2.0
Release:        %autorelease
Summary:        Command-line package manager
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf5
#!RemoteAsset:  sha256:fd37bad6c772bd0cc784a7a8808d530dfc06782f8dc7b225752eb296fcd1b7ad
Source0:        https://github.com/rpm-software-management/dnf5/archive/%{version}/dnf5-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DVERSION_PRIME:STRING=5
BuildOption(conf):  -DVERSION_MAJOR:STRING=4
BuildOption(conf):  -DVERSION_MINOR:STRING=2
BuildOption(conf):  -DVERSION_MICRO:STRING=0
BuildOption(conf):  -DPACKAGE_VERSION:STRING=%{version}
BuildOption(conf):  -DWITH_LIBDNF5_CLI:BOOL=ON
BuildOption(conf):  -DWITH_DNF5_PLUGINS:BOOL=ON
BuildOption(conf):  -DWITH_DNF5DAEMON_CLIENT:BOOL=OFF
BuildOption(conf):  -DWITH_DNF5DAEMON_SERVER:BOOL=OFF
BuildOption(conf):  -DWITH_COMPS:BOOL=OFF
BuildOption(conf):  -DWITH_MODULEMD:BOOL=OFF
BuildOption(conf):  -DWITH_SYSTEMD:BOOL=ON
BuildOption(conf):  -DWITH_HTML:BOOL=OFF
BuildOption(conf):  -DWITH_MAN:BOOL=OFF
BuildOption(conf):  -DWITH_GO:BOOL=OFF
BuildOption(conf):  -DWITH_PERL5:BOOL=OFF
BuildOption(conf):  -DWITH_PYTHON3:BOOL=ON
BuildOption(conf):  -DWITH_RUBY:BOOL=OFF
BuildOption(conf):  -DWITH_TESTS:BOOL=OFF
BuildOption(conf):  -DWITH_PLUGIN_APPSTREAM:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 10.1
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(librepo) >= 1.20.0
BuildRequires:  pkgconfig(libsolv) >= 0.7.36
BuildRequires:  pkgconfig(libsolvext) >= 0.7.25
BuildRequires:  pkgconfig(rpm) >= 4.19.0
BuildRequires:  pkgconfig(sqlite3) >= 3.35.0
BuildRequires:  pkgconfig(libpkgmanifest)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  toml11
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  swig
BuildRequires:  pkgconfig(python3)

Provides:       dnf

Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       coreutils

%description
DNF5 is a command-line package manager that automates the process of installing,
upgrading, configuring, and removing computer programs in a consistent manner.

%package     -n libdnf5
Summary:        Package management library
Requires:       libsolv
Requires:       librepo
Requires:       sqlite

%description -n libdnf5
Package management library.

%package     -n libdnf5-cli
Summary:        Library for terminal interactions in dnf5
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli
Library for working with a terminal in a command-line package manager.

%package        plugins
Summary:        Core plugins for dnf5
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       curl

%description    plugins
Core DNF5 plugins that enhance dnf5 with commands like builddep, config-manager, copr, etc.

%package     -n python-libdnf5
Summary:        Python bindings for the libdnf5 library
%python_provide python3-libdnf5
Provides:       python3-libdnf5
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n python-libdnf5
Python bindings for the libdnf library.

%package     -n python-libdnf5-cli
Summary:        Python bindings for the libdnf5-cli library
%python_provide python3-libdnf5-cli
Provides:       python3-libdnf5-cli
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}

%description -n python-libdnf5-cli
Python bindings for the libdnf5-cli library.

%package     -n python-libdnf5-python-plugins-loader
Summary:        Libdnf5 plugin that allows loading Python plugins
%python_provide python3-libdnf5-python-plugins-loader
Provides:       python3-libdnf5-python-plugins-loader
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       python3-libdnf5 = %{version}-%{release}

%description -n python-libdnf5-python-plugins-loader
Libdnf5 plugin that allows loading Python plugins.

%package        devel
Summary:        Development files for dnf5, libdnf5 and libdnf5-cli
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libsolv) >= 0.7.36

%description    devel
Development files for dnf5.

%install -a
ln -sf dnf5 %{buildroot}%{_bindir}/dnf
# By default we don't want enable local plugin.
sed -i 's/enabled = host-only/enabled = false/g' %{buildroot}%{_sysconfdir}/dnf/libdnf5-plugins/local.conf
%find_lang %{name} --generate-subpackages --all-name

%files
%license COPYING.md gpl-2.0.txt
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/dnf5
%{_bindir}/dnf
%dir %{_sysconfdir}/dnf
%dir %{_sysconfdir}/dnf/dnf5-aliases.d
%doc %{_sysconfdir}/dnf/dnf5-aliases.d/README
%dir %{_datadir}/dnf5
%dir %{_datadir}/dnf5/aliases.d
%{_datadir}/dnf5/aliases.d/compatibility.conf
%dir %{_datadir}/dnf5/dnf5-plugins
%dir %{_sysconfdir}/dnf/dnf5-plugins
%dir %{_libdir}/libdnf5/plugins
%{_sysconfdir}/bash_completion.d/dnf5
%{_datadir}/zsh/site-functions/_dnf5
%{_bindir}/dnf-automatic
%{_unitdir}/dnf-automatic.service
%{_unitdir}/dnf-automatic.timer
%{_unitdir}/dnf5-automatic.service
%{_unitdir}/dnf5-automatic.timer
%{_unitdir}/dnf5-makecache.service
%{_unitdir}/dnf5-makecache.timer
%{_unitdir}/dnf5-offline-transaction-cleanup.service
%{_unitdir}/dnf5-offline-transaction.service

%files -n libdnf5
%license lgpl-2.1.txt
%config(noreplace) %{_sysconfdir}/dnf/dnf.conf
%dir %{_sysconfdir}/dnf/vars
%dir %{_sysconfdir}/dnf/protected.d
%ghost %attr(0644, root, root) %{_sysconfdir}/dnf/versionlock.toml
%dir %{_datadir}/dnf5/libdnf.conf.d
%dir %{_datadir}/dnf5/libdnf.plugins.conf.d
%dir %{_datadir}/dnf5/vendors.d
%dir %{_sysconfdir}/dnf/libdnf5.conf.d
%dir %{_sysconfdir}/dnf/vendors.d
%dir %{_datadir}/dnf5/repos.override.d
%dir %{_sysconfdir}/dnf/repos.override.d
%dir %{_datadir}/dnf5/repos.d
%dir %{_datadir}/dnf5/vars.d
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so.*
%ghost %attr(0755, root, root) %dir %{_var}/cache/libdnf5
%ghost %attr(0755, root, root) %dir %{_sharedstatedir}/dnf

%files -n libdnf5-cli
%{_libdir}/libdnf5-cli.so.*

%files plugins
%dir %{_sysconfdir}/dnf/libdnf5-plugins
%dir %{_sysconfdir}/dnf/libdnf5-plugins/actions.d
%dir %{_sysconfdir}/dnf/libdnf5-plugins/python_plugins_loader.d
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/actions.conf
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/expired-pgp-keys.conf
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/local.conf
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/python_plugins_loader.conf
%dir %{_libdir}/dnf5
%dir %{_libdir}/dnf5/plugins
%doc %{_libdir}/dnf5/plugins/README
%{_libdir}/libdnf5/plugins/*.so
%{_libdir}/dnf5/plugins/*.so
%{_datadir}/dnf5/dnf5-plugins/automatic.conf
%{_datadir}/dnf5/aliases.d/compatibility-plugins.conf
%{_datadir}/dnf5/aliases.d/compatibility-reposync.conf

%files -n python-libdnf5
%{python3_sitearch}/libdnf5
%{python3_sitearch}/libdnf5-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt

%files -n python-libdnf5-cli
%{python3_sitearch}/libdnf5_cli
%{python3_sitearch}/libdnf5_cli-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt

%files -n python-libdnf5-python-plugins-loader
%{_libdir}/libdnf5/plugins/python_plugins_loader.*
%dir %{python3_sitelib}/libdnf_plugins/
%doc %{python3_sitelib}/libdnf_plugins/README

%files devel
%license COPYING.md lgpl-2.1.txt
%{_includedir}/dnf5/
%{_includedir}/libdnf5/
%{_includedir}/libdnf5-cli/
%{_libdir}/libdnf5.so
%{_libdir}/libdnf5-cli.so
%{_libdir}/pkgconfig/libdnf5.pc
%{_libdir}/pkgconfig/libdnf5-cli.pc

%changelog
%autochangelog
