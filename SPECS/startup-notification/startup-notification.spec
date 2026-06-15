# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           startup-notification
Version:        0.12
Release:        %autorelease
Summary:        Library for tracking application startup
License:        LGPL-2.0-or-later AND MIT
URL:            https://www.freedesktop.org/wiki/Software/startup-notification/
# Upstream freedesktop.org release dir now returns HTTP 418; use Debian's
# byte-identical orig tarball (same sha256) as a reliable mirror.
#!RemoteAsset:  sha256:3c391f7e930c583095045cd2d10eb73a64f085c7fde9d260f2652c7cb3cfbe4a
Source0:        https://deb.debian.org/debian/pool/main/s/startup-notification/%{name}_%{version}.orig.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-fix-test-xmessage-atom-types.patch

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xt)

%description
startup-notification implements the startup notification protocol used by
desktop environments and window managers to track launched applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers and library links for developing applications
that use startup-notification.

%prep -a
mkdir -p examples
cp -p test/*.c test/*.h examples

%files
%doc AUTHORS ChangeLog NEWS README doc/startup-notification.txt
%license COPYING
%{_libdir}/libstartup-notification-1.so.0*

%files devel
%doc examples
%license COPYING
%{_includedir}/startup-notification-1.0/
%{_libdir}/libstartup-notification-1.so
%{_libdir}/pkgconfig/libstartup-notification-1.0.pc

%changelog
%autochangelog
