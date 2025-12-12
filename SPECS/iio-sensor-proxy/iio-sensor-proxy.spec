# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0
%bcond doc 0

Name:           iio-sensor-proxy
Version:        3.8
Release:        %autorelease
Summary:        IIO accelerometer sensor to input device proxy
License:        GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/hadess/iio-sensor-proxy
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/archive/%{version}/iio-sensor-proxy-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dgtk-tests=false
%if %{with doc}
BuildOption(conf):  -Dgtk_doc=true
%else
BuildOption(conf):  -Dgtk_doc=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  systemd-rpm-macros

%if %{with doc}
BuildRequires:  gtk-doc
%endif

%if %{with tests}
BuildRequires:  umockdev
BuildRequires:  python3-dbusmock
%endif

%{?systemd_requires}

%description
iio-sensor-proxy is a system daemon to manage IIO accelerometer sensors and
proxies them to input devices.

%if %{with doc}
%package        docs
Summary:        Documentation for %{name}
License:        GFDL-1.1-or-later
BuildArch:      noarch

%description    docs
This package contains the documentation for %{name}.
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/monitor-sensor
%{_libexecdir}/iio-sensor-proxy
%{_unitdir}/iio-sensor-proxy.service
%{_udevrulesdir}/*-iio-sensor-proxy.rules
%{_datadir}/dbus-1/system.d/net.hadess.SensorProxy.conf
%{_datadir}/polkit-1/actions/net.hadess.SensorProxy.policy

%if %{with doc}
%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/iio-sensor-proxy/
%endif

%changelog
%{?autochangelog}
