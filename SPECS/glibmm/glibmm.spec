# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global apiver 2.68
%global __provides_exclude ^perl\\(
%global __requires_exclude ^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)


Name:           glibmm
Version:        2.86.0
Release:        %autorelease
Summary:        C++ interface for the GLib library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://gtkmm.org/
#!RemoteAsset
Source:         https://download.gnome.org/sources/glibmm/2.86/glibmm-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf): -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sigc++-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.61.2
BuildRequires:  perl(Getopt::Long)

%description
glibmm is the official C++ interface for the popular cross-platform
library GLib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
# this test require network.
sed -i 's/.*giomm_tls_client.*//g' tests/meson.build

%install -a
chmod +x %{buildroot}%{_libdir}/glibmm-%{apiver}/proc/generate_wrap_init.pl
chmod +x %{buildroot}%{_libdir}/glibmm-%{apiver}/proc/gmmproc

%files
%license COPYING COPYING.tools
%doc NEWS README.md
%{_libdir}/libgiomm-%{apiver}.so.1*
%{_libdir}/libglibmm-%{apiver}.so.1*
%{_libdir}/libglibmm_generate_extra_defs-%{apiver}.so.1*

%files devel
%{_includedir}/glibmm-%{apiver}/
%{_includedir}/giomm-%{apiver}/
%{_libdir}/*.so
%{_libdir}/glibmm-%{apiver}/
%{_libdir}/giomm-%{apiver}/
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
