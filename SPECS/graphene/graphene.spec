# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           graphene
Version:        1.10.8
Release:        %autorelease
Summary:        Thin layer of types for graphic libraries
License:        MIT
URL:            https://github.com/ebassi/graphene
#!RemoteAsset
Source0:        https://github.com/ebassi/graphene/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dinstalled_tests=false
%if %{with doc}
BuildOption(conf):  -Dgtk_doc=true
%else
BuildOption(conf):  -Dgtk_doc=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if %{with doc}
BuildRequires:  gtk-doc
%endif

%description
Graphene provides a small set of mathematical types needed to implement graphic
libraries that deal with 2D and 3D transformations and projections.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/girepository-1.0/
%{_libdir}/libgraphene-1.0.so.0*

%files devel
%{_includedir}/graphene-1.0/
%dir %{_libdir}/graphene-1.0
%{_libdir}/graphene-1.0/include/
%{_libdir}/libgraphene-1.0.so
%{_libdir}/pkgconfig/graphene-1.0.pc
%{_libdir}/pkgconfig/graphene-gobject-1.0.pc
%{_datadir}/gir-1.0/
%{_libexecdir}/installed-tests/
%if %{with doc}
%{_datadir}/gtk-doc/
%endif

%changelog
%autochangelog
