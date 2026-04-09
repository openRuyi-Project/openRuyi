# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __provides_exclude ^perl\\(
%global __requires_exclude ^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)

Name:           glibmm2.4
Version:        2.66.8
Release:        %autorelease
Summary:        C++ interface for the GLib library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/glibmm
VCS:            git:https://gitlab.gnome.org/GNOME/gtkmm.git
#!RemoteAsset:  sha256:64f11d3b95a24e2a8d4166ecff518730f79ecc27222ef41faf7c7e0340fc9329
Source0:        https://download.gnome.org/sources/glibmm/2.66/glibmm-%{version}.tar.xz
BuildSystem:    meson

# the name resolv will fail in the env.
Patch0:         0001-skip-name-resolv-test.patch

BuildOption(conf):  -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sigc++-2.0)

%description
glibmm is the official C++ interface for the popular cross-platform
library GLib.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
chmod +x %{buildroot}%{_libdir}/glibmm-*/proc/generate_wrap_init.pl
chmod +x %{buildroot}%{_libdir}/glibmm-*/proc/gmmproc

%files
%license COPYING COPYING.tools
%doc NEWS README.md
%{_libdir}/libgiomm-*.so.*
%{_libdir}/libglibmm-*.so.*
%{_libdir}/libglibmm_generate_extra_defs-*.so.*

%files devel
%{_includedir}/glibmm-*/
%{_includedir}/giomm-*/
%{_libdir}/*.so
%{_libdir}/glibmm-*/
%{_libdir}/giomm-*/
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
