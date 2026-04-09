# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0

Name:           bolt
Version:        0.9.10
Release:        %autorelease
Summary:        Thunderbolt device manager
License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/bolt/bolt
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/bolt/bolt/-/archive/%{version}/bolt-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddb-name=boltd
BuildOption(conf):  -Dman=false
%if %{with tests}
BuildOption(conf):  -Dinstall-tests=true
%else
BuildOption(conf):  -Dinstall-tests=false
%endif

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

%if %{with tests}
BuildRequires:  python3-gobject-base
BuildRequires:  python3-dbus
BuildRequires:  python3-dbusmock
BuildRequires:  umockdev-devel
%endif
%{?systemd_requires}

%description
bolt is a system daemon to manage Thunderbolt devices via a D-BUS API.

%check
%if %{with tests}
%meson_test
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/boltctl
%{_libexecdir}/boltd
%{_unitdir}/bolt.service
%{_udevrulesdir}/*-bolt.rules
%{_datadir}/dbus-1/system.d/org.freedesktop.bolt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.bolt.xml
%{_datadir}/polkit-1/actions/org.freedesktop.bolt.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.bolt.rules
%{_datadir}/dbus-1/system-services/org.freedesktop.bolt.service
%ghost %dir %{_localstatedir}/lib/boltd
%if %{with tests}
%{_libexecdir}/installed-tests/bolt
%endif

%changelog
%autochangelog
