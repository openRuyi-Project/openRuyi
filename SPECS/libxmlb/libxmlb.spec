# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond stemmer 0
%bcond tests 0
%bcond doc 0

Name:           libxmlb
Version:        0.3.24
Release:        %autorelease
Summary:        Library for querying compressed XML metadata
License:        LGPL-2.1-or-later
URL:            https://github.com/hughsie/libxmlb
#!RemoteAsset
Source:         https://github.com/hughsie/libxmlb/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

%if %{with doc}
BuildOption(conf): -Dgtkdoc=true
%else
BuildOption(conf): -Dgtkdoc=false
%endif

%if %{with tests}
BuildOption(conf): -Dtests=true
%else
BuildOption(conf): -Dtests=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)

%if %{with stemmer}
BuildRequires:  libstemmer-devel
%endif

%if %{with doc}
BuildRequires:  gtk-doc
%endif

%if %{with tests}
BuildRequires:  shared-mime-info
%endif

Requires:       glib
Requires:       shared-mime-info

%description
libxmlb is a library that takes XML source, and converts it to a structured
binary representation with a deduplicated string table. This allows applications
to mmap the binary XML file and do XPath queries efficiently.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%if %{with tests}
%package        tests
Summary:        Files for installed tests
Requires:       %{name} = %{version}-%{release}

%description    tests
Executable and data files for installed tests.
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/xb-tool
%{_mandir}/man1/xb-tool.1*
%{_libdir}/girepository-1.0/Xmlb-2.0.typelib
%{_libdir}/libxmlb.so.2*

%files devel
%{_datadir}/gir-1.0/Xmlb-2.0.gir
%{_includedir}/libxmlb-2
%{_libdir}/libxmlb.so
%{_libdir}/pkgconfig/xmlb.pc
%if %{with doc}
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libxmlb
%endif

%if %{with tests}
%files tests
%dir %{_libexecdir}/installed-tests/libxmlb
%{_libexecdir}/installed-tests/libxmlb/xb-self-test
%{_libexecdir}/installed-tests/libxmlb/test.*
%dir %{_datadir}/installed-tests/libxmlb
%{_datadir}/installed-tests/libxmlb/libxmlb.test
%endif

%changelog
%{?autochangelog}
