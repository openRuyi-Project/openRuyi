# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dbus-glib
Version:        0.114
Release:        %autorelease
Summary:        GLib bindings for D-Bus
License:        (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:            https://www.freedesktop.org/software/dbus/
VCS:            git:https://gitlab.freedesktop.org/dbus/dbus-glib.git
#!RemoteAsset
Source:         https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-tests=yes
BuildOption(conf):  --enable-asserts=yes
BuildOption(conf):  --disable-gtk-doc
BuildOption(conf):  --disable-static
BuildOption(conf):  CFLAGS="%{optflags} -std=gnu17"

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(python3)
BuildRequires:  dbus-daemon
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

%description
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package        devel
Summary:        Libraries and headers for the D-Bus GLib bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and static libraries for the D-Bus GLib bindings.

%install -a
chmod -x %{buildroot}%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh

%files
%doc NEWS
%license COPYING
%{_libdir}/libdbus-glib-1.so.*
%{_bindir}/dbus-binding-tool
%{_mandir}/man1/dbus-binding-tool.1*

%files devel
%{_libdir}/libdbus-glib-1.so
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_includedir}/dbus-1.0/dbus/*
%{_datadir}/gtk-doc/html/dbus-glib
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libexecdir}/dbus-bash-completion-helper

%changelog
%autochangelog
