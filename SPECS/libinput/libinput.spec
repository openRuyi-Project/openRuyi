# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0

Name:           libinput
Version:        1.30.0
Release:        %autorelease
Summary:        Input device library
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libinput/
VCS:            git:https://gitlab.freedesktop.org/libinput/libinput.git
#!RemoteAsset:  sha256:594d970cab7b3738ad99218e7dafc253780f58a7600ab0823d2fcc3941a04e86
Source:         https://gitlab.freedesktop.org/libinput/libinput/-/archive/%{version}/libinput-%{version}.tar.bz2
BuildSystem:    meson

BuildOption(conf):  -Ddebug-gui=false
BuildOption(conf):  -Ddocumentation=false
BuildOption(conf):  -Dudev-dir=%{_udevrulesdir}
%if %{with tests}
BuildOption(conf):  -Dtests=true
BuildOption(conf):  -Dinstall-tests=true
%else
BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dinstall-tests=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(mtdev) >= 1.1.0
BuildRequires:  pkgconfig(libevdev) >= 0.4
BuildRequires:  pkgconfig(udev)
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-rpm-macros
BuildRequires:  lua-devel

%description
libinput is a library that handles input devices for display servers and other
applications that need to directly deal with input devices. It provides device
detection, device handling, input device event processing and abstraction.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities and tools for debugging %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3dist(pyudev)
Requires:       python3dist(libevdev)

%description    utils
The %{name}-utils package contains tools to debug hardware and analyze
%{name}.

%prep -a
%py3_shebang_fix $(grep -rIl '#!/usr/bin/.*python3' .)

%check
%if %{with tests}
%meson_test
%endif

%files
%doc COPYING
%{_libdir}/libinput.so.*
%{_udevrulesdir}/libinput-device-group
%{_udevrulesdir}/libinput-fuzz-to-zero
%{_udevrulesdir}/libinput-fuzz-extract
%{_udevrulesdir}/rules.d/80-libinput-device-groups.rules
%{_udevrulesdir}/rules.d/90-libinput-fuzz-override.rules
%{_bindir}/libinput
%dir %{_libexecdir}/libinput/
%{_libexecdir}/libinput/libinput-debug-events
%{_libexecdir}/libinput/libinput-list-devices
%{_libexecdir}/libinput/libinput-test*
%{_mandir}/man1/libinput.1*
%dir %{_datadir}/libinput
%{_datadir}/libinput/*.quirks
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*
%{_mandir}/man1/libinput-list-devices.1*
%{_mandir}/man1/libinput-debug-events.1*
%{_mandir}/man1/libinput-test*.1*

%files devel
%{_includedir}/libinput.h
%{_libdir}/libinput.so
%{_libdir}/pkgconfig/libinput.pc

%files utils
%{_libexecdir}/libinput/libinput-analyze*
%{_libexecdir}/libinput/libinput-debug-tablet*
%{_libexecdir}/libinput/libinput-list-kernel-devices
%{_libexecdir}/libinput/libinput-measure*
%{_libexecdir}/libinput/libinput-quirks*
%{_libexecdir}/libinput/libinput-record
%{_libexecdir}/libinput/libinput-replay
%{_mandir}/man1/libinput-analyze*.1*
%{_mandir}/man1/libinput-debug-tablet*.1*
%{_mandir}/man1/libinput-list-kernel-devices.1*
%{_mandir}/man1/libinput-measure*.1*
%{_mandir}/man1/libinput-quirks*.1*
%{_mandir}/man1/libinput-record.1*
%{_mandir}/man1/libinput-replay.1*

%changelog
%autochangelog
