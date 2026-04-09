# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           libtraceevent
Version:        1.8.4
Release:        %autorelease
Summary:        Linux kernel trace event parsing library
License:        LGPL-2.1-only AND GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git
#!RemoteAsset
Source0:        https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/%{name}-%{version}.tar.gz
BuildSystem:    meson

%if %{without doc}
BuildOption(conf):  -Ddoc=false
%endif
BuildOption(conf):  --default-library=shared
BuildOption(conf):  -Dhtmldir=%{_docdir}/%{name}
BuildOption(conf):  -Dplugindir=%{_libdir}/traceevent/plugins

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
%if %{with doc}
BuildRequires:  asciidoc
BuildRequires:  xmlto
%endif

%description
The libtraceevent library provides a C API to parse the event formats found
in the tracefs filesystem, which is the foundation of the kernel ftrace
infrastructure.

%package        plugins
Summary:        Plugins for the libtraceevent library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins
This package provides plugins for libtraceevent, which can add extra
functionality such as dynamically creating event formats from strings.

%if %{with doc}
%package        doc
Summary:        HTML documentation for the libtraceevent API
BuildArch:      noarch

%description    doc
This package contains the detailed HTML documentation for the libtraceevent API.
%endif

%package        devel
Summary:        Development files for the libtraceevent library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the header files, libraries, and pkg-config files
needed to develop applications that use libtraceevent.

%files
%license LICENSES/LGPL-2.1 LICENSES/GPL-2.0
%{_libdir}/libtraceevent.so.*

%files plugins
%dir %{_libdir}/traceevent
%dir %{_libdir}/traceevent/plugins
%{_libdir}/traceevent/plugins/*.so
%{_libdir}/traceevent/plugins/libtraceevent-dynamic-list

%if %{with doc}
%files doc
%{_docdir}/%{name}/
%endif

%files devel
%doc README samples/
%{_includedir}/traceevent/
%{_libdir}/libtraceevent.so
%{_libdir}/pkgconfig/libtraceevent.pc

%changelog
%autochangelog
