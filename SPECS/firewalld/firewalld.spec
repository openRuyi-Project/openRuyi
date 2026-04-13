# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           firewalld
Version:        2.4.0
Release:        %autorelease
Summary:        A firewall daemon with D-Bus interface providing a dynamic firewall
License:        GPL-2.0-or-later
URL:            https://firewalld.org/
VCS:            git:https://github.com/firewalld/firewalld
#!RemoteAsset:  sha256:992853451a58d229068c0ed10c3e007b2032c0fb654f27d656bfa3c120a2f132
Source0:        https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(conf):  --enable-sysconfig
BuildOption(conf):  --enable-rpmmacros
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  iptables
BuildRequires:  libxslt
BuildRequires:  ebtables
BuildRequires:  ipset
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)

Provides:       firewall-macros = %{version}-%{release}

Requires:       python3-firewall = %{version}-%{release}

%description
firewalld is a firewall service daemon that provides a dynamic customizable
firewall with a D-Bus interface.

%package     -n python-firewall
Summary:        Python bindings for firewalld
Provides:       python3-firewall
%{?python_provide:%python_provide python3-firewall}
Requires:       python3dist(dbus-python)
Requires:       python3dist(pygobject)
Requires:       python3dist(nftables)

%description -n python-firewall
Python3 bindings for firewalld.

%package     -n firewall-applet
Summary:        Firewall panel applet
Requires:       firewall-config = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       python3dist(pyqt6)
Requires:       python3dist(pygobject)

%description -n firewall-applet
The firewall panel applet provides a status information of firewalld and also
the firewall settings.

%package     -n firewall-config
Summary:        Firewall configuration application
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       python3dist(pygobject)

%description -n firewall-config
The firewall configuration application provides an configuration interface for
firewalld.

%install -a
%if %{with gui}
desktop-file-install --delete-original \
    --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/firewall-applet.desktop
desktop-file-install --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/firewall-config.desktop
%endif

%find_lang %{name} --all-name

# TODO: Fix tests.
%check

%post
%systemd_post firewalld.service

%preun
%systemd_preun firewalld.service

%postun
%systemd_postun_with_restart firewalld.service

%files -f %{name}.lang
%doc COPYING README.md
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/helpers
%dir %{_prefix}/lib/firewalld/icmptypes
%dir %{_prefix}/lib/firewalld/ipsets
%dir %{_prefix}/lib/firewalld/policies
%dir %{_prefix}/lib/firewalld/services
%dir %{_prefix}/lib/firewalld/zones
%dir %{_prefix}/lib/firewalld/xmlschema
%dir %{_datadir}/firewalld
%{_prefix}/lib/firewalld/icmptypes/*.xml
%{_prefix}/lib/firewalld/ipsets/README.md
%{_prefix}/lib/firewalld/policies/*.xml
%{_prefix}/lib/firewalld/services/*.xml
%{_prefix}/lib/firewalld/zones/*.xml
%{_prefix}/lib/firewalld/helpers/*.xml
%{_prefix}/lib/firewalld/xmlschema/check.sh
%{_prefix}/lib/firewalld/xmlschema/*.xsd
%{_sbindir}/firewalld
%{_bindir}/firewall-cmd
%{_bindir}/firewall-offline-cmd
%{_sysconfdir}/modprobe.d/firewalld-sysctls.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/firewalld
%ghost %config(noreplace) %{_sysconfdir}/firewalld/firewalld.conf
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/helpers
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/icmptypes
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/ipsets
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/policies
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/services
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/zones
%config(noreplace) %{_sysconfdir}/sysconfig/firewalld
%config(noreplace) %{_datadir}/dbus-1/system.d/FirewallD.conf
%{_unitdir}/firewalld.service
%{_datadir}/polkit-1/*
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/firewall-cmd
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_firewalld
%{_mandir}/man1/firewall*cmd*.1*
%{_mandir}/man1/firewalld*.1*
%{_mandir}/man5/firewall*.5*
%{_rpmmacrodir}/macros.firewalld
# testsuite
%dir %{_datadir}/firewalld/testsuite
%{_datadir}/firewalld/testsuite/README.md
%{_datadir}/firewalld/testsuite/testsuite
%dir %{_datadir}/firewalld/testsuite/integration
%{_datadir}/firewalld/testsuite/integration/testsuite
%dir %{_datadir}/firewalld/testsuite/python
%attr(0755,root,root) %{_datadir}/firewalld/testsuite/python/*.py

%files -n python-firewall
%attr(0755,root,root) %dir %{python_sitelib}/firewall
%attr(0755,root,root) %dir %{python_sitelib}/firewall/config
%attr(0755,root,root) %dir %{python_sitelib}/firewall/core
%attr(0755,root,root) %dir %{python_sitelib}/firewall/core/io
%attr(0755,root,root) %dir %{python_sitelib}/firewall/server
%{python_sitelib}/firewall/*.py*
%{python_sitelib}/firewall/config/*.py*
%{python_sitelib}/firewall/server/*.py*
%{python_sitelib}/firewall/core/io/*.py*
%{python_sitelib}/firewall/core/*.py*

%files -n firewall-applet
%{_bindir}/firewall-applet
%config(noreplace) %{_sysconfdir}/xdg/autostart/firewall-applet.desktop
%dir %{_sysconfdir}/firewall
%config(noreplace) %{_sysconfdir}/firewall/applet.conf
%{_datadir}/icons/hicolor/*/apps/firewall-applet*.*
%{_mandir}/man1/firewall-applet*.1*

%files -n firewall-config
%{_bindir}/firewall-config
%{_datadir}/firewalld/firewall-config.glade
%attr(0755,root,root) %{_datadir}/firewalld/gtk3_chooserbutton.py*
%attr(0755,root,root) %{_datadir}/firewalld/gtk3_niceexpander.py*
%{_datadir}/applications/firewall-config.desktop
%{_datadir}/metainfo/firewall-config.appdata.xml
%{_datadir}/icons/hicolor/*/apps/firewall-config*.*
%{_datadir}/glib-2.0/schemas/org.fedoraproject.FirewallConfig.gschema.xml
%{_mandir}/man1/firewall-config*.1*

%changelog
%autochangelog
