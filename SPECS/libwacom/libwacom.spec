# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0

Name:           libwacom
Version:        2.17.0
Release:        %autorelease
Summary:        Tablet Information Client Library
License:        HPND
URL:            https://github.com/linuxwacom/libwacom
#!RemoteAsset
Source:         https://github.com/linuxwacom/libwacom/archive/refs/tags/libwacom-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf): -Ddocumentation=disabled
%if %{with tests}
BuildOption(conf): -Dtests=enabled
%else
BuildOption(conf): -Dtests=disabled
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsystemd)

Requires:       %{name}-data = %{version}-%{release}

%description
%{name} is a library that provides information about Wacom tablets and tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Development files for libwacom.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

%description    data
Data files describing Wacom tablets and styli.

%package        utils
Summary:        Utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-libevdev
Requires:       python3-pyudev

%description    utils
Utilities to handle and/or debug libwacom devices.

%check
%if %{with tests}
%meson_test
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/libwacom.so.9*
%{_bindir}/libwacom-list-local-devices
%{_bindir}/libwacom-update-db
%{_mandir}/man1/libwacom-list-local-devices.1*

%files devel
%{_includedir}/libwacom-1.0/
%{_libdir}/libwacom.so
%{_libdir}/pkgconfig/libwacom.pc

%files data
%doc COPYING
%{_udevrulesdir}/*.rules
%{_udevhwdbdir}/*.hwdb
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%{_datadir}/libwacom/layouts/

%files utils
%{_bindir}/libwacom-list-devices
%{_bindir}/libwacom-show-stylus
%{_mandir}/man1/libwacom-list-devices.1*
%{_mandir}/man1/libwacom-show-stylus.1*

%changelog
%{?autochangelog}
