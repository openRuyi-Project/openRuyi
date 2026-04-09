# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond x11 1

Name:           libxkbcommon
Version:        1.13.0
Release:        %autorelease
Summary:        Keymap handling library for toolkits and window systems
License:        MIT AND X11 AND MIT-CMU
URL:            https://xkbcommon.org/
VCS:            git:https://github.com/xkbcommon/libxkbcommon
#!RemoteAsset
Source0:        https://github.com/xkbcommon/libxkbcommon/archive/refs/tags/xkbcommon-%{version}.tar.gz
BuildSystem:    meson

# Mask X11 tests now because they require Xvfb
Patch1:         libxkbcommon-1.13.1-mask-x11-test.patch

BuildOption(conf):  -Denable-docs=false
BuildOption(conf):  -Denable-wayland=true
%if %{with x11}
BuildOption(conf):  -Denable-x11=true
%else
BuildOption(conf):  -Denable-x11=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
%if %{with x11}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
%endif

%description
libxkbcommon is a library to handle keyboard descriptions, including loading them
from disk, parsing them, and handling their state. It's mainly meant for
client toolkits, window systems, and other system applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        utils
Summary:        Utilities for %{name}
Requires:       %{name} = %{version}-%{release}

%description    utils
Utilities to analyze and test XKB parsing.

%if %{with x11}
%package        x11
Summary:        X11 support library for %{name}
Requires:       %{name} = %{version}-%{release}

%description    x11
X11 support library for %{name}.

%package        x11-devel
Summary:        Development files for %{name}-x11
Requires:       %{name}-x11%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    x11-devel
Development files for %{name}-x11.
%endif

%files
%license LICENSE
%{_libdir}/libxkbcommon.so.0*
%{_libdir}/libxkbregistry.so.0*

%files devel
%{_libdir}/libxkbcommon.so
%{_libdir}/libxkbregistry.so
%dir %{_includedir}/xkbcommon/
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_includedir}/xkbcommon/xkbcommon-compose.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_includedir}/xkbcommon/xkbregistry.h
%{_libdir}/pkgconfig/xkbcommon.pc
%{_libdir}/pkgconfig/xkbregistry.pc

%files utils
%{_bindir}/xkbcli
%{_libexecdir}/xkbcommon/xkbcli-compile-compose
%{_libexecdir}/xkbcommon/xkbcli-compile-keymap
%{_libexecdir}/xkbcommon/xkbcli-how-to-type
%{_libexecdir}/xkbcommon/xkbcli-interactive
%{_libexecdir}/xkbcommon/xkbcli-interactive-evdev
%{_libexecdir}/xkbcommon/xkbcli-list
%{_mandir}/man1/xkbcli-compile-compose.1*
%{_mandir}/man1/xkbcli-compile-keymap.1*
%{_mandir}/man1/xkbcli-how-to-type.1*
%{_mandir}/man1/xkbcli-interactive-evdev.1*
%{_mandir}/man1/xkbcli-list.1*
%{_mandir}/man1/xkbcli.1*
%{_datadir}/bash-completion/completions/xkbcli
%{_libexecdir}/xkbcommon/xkbcli-dump-keymap-wayland
%{_libexecdir}/xkbcommon/xkbcli-interactive-wayland
%{_libexecdir}/xkbcommon/xkbcli-dump-keymap
%{_mandir}/man1/xkbcli-dump-keymap-wayland.1*
%{_mandir}/man1/xkbcli-interactive-wayland.1*

%if %{with x11}
%files x11
%{_libdir}/libxkbcommon-x11.so.0*

%files x11-devel
%{_libdir}/libxkbcommon-x11.so
%{_includedir}/xkbcommon/xkbcommon-x11.h
%{_libdir}/pkgconfig/xkbcommon-x11.pc
%{_libexecdir}/xkbcommon/xkbcli-interactive-x11
%{_libexecdir}/xkbcommon/xkbcli-dump-keymap-x11
%{_mandir}/man1/xkbcli-interactive-x11.1*
%{_mandir}/man1/xkbcli-dump-keymap-x11.1*
%endif

%changelog
%autochangelog
