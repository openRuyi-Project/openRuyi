# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           editorconfig-core-c
Version:        0.12.10
Release:        %autorelease
Summary:        Parser for EditorConfig files written in C
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-1-Clause
URL:            https://github.com/editorconfig/editorconfig-core-c
#!RemoteAsset:  sha256:ab9f897a90fb36cfc34e5b67221e55ab0e3119b3512de8e31029d376c6bab870
Source0:        https://github.com/editorconfig/editorconfig-core-c/archive/refs/tags/v0.12.10.tar.gz
BuildSystem:    cmake

# Downstream-only: Do not compile with -Werror
#
# This makes sense upstream, but is too strict for downstream packaging
# across various architectures, compiler versions, and so on.
Patch0:         0001-Downstream-only-Do-not-compile-with-Werror.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  doxygen

%description
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
This package contains the command line tool.

%package        devel
Summary:        Parser library for EditorConfig files (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the files needed for development.

%install -a
rm -f %{buildroot}/%{_libdir}/libeditorconfig_static.a

%files
%doc README.md
%license LICENSE
%{_bindir}/editorconfig
%{_bindir}/editorconfig-%{version}
%{_libdir}/libeditorconfig.so.*
%{_mandir}/man1/editorconfig.1*
%{_mandir}/man3/editorconfig*
%{_mandir}/man5/editorconfig*

%files devel
%{_includedir}/editorconfig/
%{_libdir}/libeditorconfig.so
%{_libdir}/cmake/EditorConfig/
%{_libdir}/pkgconfig/editorconfig.pc

%changelog
%autochangelog
