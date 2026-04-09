# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond multihost 1

Name:           cockpit
Version:        352
Release:        %autorelease
Summary:        Web Console for Linux servers
License:        LGPL-2.1-or-later
URL:            https://cockpit-project.org/
VCS:            git:https://github.com/cockpit-project/cockpit
#!RemoteAsset
Source:         https://github.com/cockpit-project/cockpit/releases/download/%{version}/cockpit-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --with-pamdir=%{_libdir}/security
BuildOption(conf):  --disable-doc
BuildOption(conf):  --without-selinux

%if %{with multihost}
BuildOption(conf):  --enable-multihost
%endif

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  appstream
BuildRequires:  python3-pip
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.105
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(python3)
BuildRequires:  gettext >= 0.21
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  glib-networking
BuildRequires:  sed
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  openssh-clients
BuildRequires:  xmlto

Requires:       cockpit-bridge
Requires:       cockpit-ws
Requires:       cockpit-system

Recommends:     cockpit-storaged
Recommends:     cockpit-packagekit
Recommends:     cockpit-networkmanager
Recommends:     cockpit-kdump

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser. This is a metapackage that pulls in the core components.

%package        bridge
Summary:        Cockpit bridge server-side component
Requires:       glib

%description    bridge
The Cockpit bridge component installed server side.

%package        ws
Summary:        Cockpit Web Service
Requires:       glib-networking
Requires:       openssl
Requires:       glib

%description    ws
The Cockpit Web Service listens on the network.

%package        system
Summary:        Cockpit admin interface package
Requires:       cockpit-bridge >= %{version}-%{release}
Requires:       grep
Requires:       /usr/bin/date

%description    system
This package contains the Cockpit shell and system configuration interfaces.

%package        kdump
Summary:        Cockpit user interface for kernel crash dumping
Requires:       cockpit-bridge >= %{version}-%{release}
Requires:       cockpit-shell >= %{version}-%{release}

%description    kdump
The Cockpit component for configuring kernel crash dumping.

%package        networkmanager
Summary:        Cockpit user interface for networking
Requires:       cockpit-bridge >= %{version}-%{release}
Requires:       cockpit-shell >= %{version}-%{release}
Requires:       NetworkManager >= 1.6

%description    networkmanager
The Cockpit component for managing networking.

%package        sosreport
Summary:        Cockpit user interface for diagnostic reports
Requires:       cockpit-bridge >= %{version}-%{release}
Requires:       cockpit-shell >= %{version}-%{release}

%description    sosreport
The Cockpit component for creating diagnostic reports.

%package        storaged
Summary:        Cockpit user interface for storage
Requires:       cockpit-shell >= %{version}-%{release}
Requires:       udisks2 >= 2.9

%description    storaged
The Cockpit component for managing storage.

%package        packagekit
Summary:        Cockpit user interface for packages
Requires:       cockpit-bridge >= %{version}-%{release}
Requires:       PackageKit

%description    packagekit
The Cockpit components for installing OS updates via PackageKit.

%package        doc
Summary:        Cockpit deployment and developer guide

%description    doc
The Cockpit Deployment and Developer Guide.

%conf -p
autoreconf -fiv

# disable tests.
%check

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -p -m 644 tools/cockpit.pam %{buildroot}%{_sysconfdir}/pam.d/cockpit

install -D -p -m 644 AUTHORS COPYING README.md %{buildroot}%{_docdir}/cockpit/

# disable selinux,so we delete files.
rm -rf %{buildroot}%{_datadir}/cockpit/selinux
rm -f %{buildroot}%{_datadir}/metainfo/*selinux*

%post ws
%systemd_post cockpit.socket cockpit.service

%preun ws
%systemd_preun cockpit.socket cockpit.service

%postun ws
%systemd_postun_with_restart cockpit.socket cockpit.service

%files
%license COPYING
%doc %{_docdir}/cockpit/AUTHORS
%doc %{_docdir}/cockpit/COPYING
%doc %{_docdir}/cockpit/README.md
%{_datadir}/metainfo/org.cockpit_project.cockpit.appdata.xml
%{_datadir}/icons/hicolor/*/apps/cockpit.png

%files bridge
%license COPYING
%{_bindir}/cockpit-bridge
%{_libexecdir}/cockpit-askpass
%{python3_sitelib}/cockpit/
%dir %{_datadir}/cockpit
%{_datadir}/cockpit/base1/
%{_datadir}/cockpit/static/
%dir %{_sysconfdir}/cockpit/machines.d
%{_datadir}/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy
%{python3_sitelib}/cockpit-*.dist-info/

%files ws
%license COPYING
%{_libexecdir}/cockpit-desktop
%{_libexecdir}/cockpit-ws
%{_libexecdir}/cockpit-wsinstance-factory
%{_libexecdir}/cockpit-tls
%{_libexecdir}/cockpit-client*
%{_libexecdir}/cockpit-certificate-*
%{_libexecdir}/cockpit-session
%{_datadir}/cockpit/branding/
%dir %{_sysconfdir}/cockpit
%{_datadir}/cockpit/issue/
%config(noreplace) %{_sysconfdir}/cockpit/ws-certs.d
%config(noreplace) %{_sysconfdir}/pam.d/cockpit
# Systemd units
%{_unitdir}/cockpit*.service
%{_unitdir}/cockpit*.socket
%{_unitdir}/*.slice
# Tmpfiles
%{_prefix}/lib/tmpfiles.d/cockpit-ws.conf
# PAM modules
%{_libdir}/security/pam_ssh_add.so
%{_libdir}/security/pam_cockpit_cert.so
# Ghost files
%ghost %{_sysconfdir}/issue.d/cockpit.issue
%ghost %{_sysconfdir}/motd.d/cockpit
%ghost %{_sysconfdir}/cockpit/disallowed-users

%files system
%license COPYING
%{_datadir}/cockpit/shell/
%{_datadir}/cockpit/systemd/
%{_datadir}/cockpit/users/
%{_datadir}/cockpit/metrics/
%{_datadir}/cockpit/apps/

%files kdump
%{_datadir}/cockpit/kdump/
%{_datadir}/metainfo/*kdump*

%files sosreport
%{_datadir}/cockpit/sosreport/
%{_datadir}/metainfo/*sosreport*
%{_datadir}/icons/hicolor/*/apps/cockpit-sosreport.png

%files networkmanager
%{_datadir}/cockpit/networkmanager/
%{_datadir}/metainfo/*networkmanager*

%files storaged
%{_datadir}/cockpit/storaged/
%{_datadir}/metainfo/*storaged*

%files packagekit
%{_datadir}/cockpit/packagekit/

%files doc
%doc %{_docdir}/cockpit/
%exclude %{_docdir}/cockpit/AUTHORS
%exclude %{_docdir}/cockpit/COPYING
%exclude %{_docdir}/cockpit/README.md

%changelog
%autochangelog
