# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfyaml
Version:        0.9
Release:        %autorelease
Summary:        Complete YAML parser and emitter
License:        MIT AND GPL-2.0-only AND BSD-2-Clause
URL:            https://github.com/pantoniou/libfyaml
#!RemoteAsset
Source0:        https://github.com/pantoniou/libfyaml/archive/refs/tags/v%{version}.tar.gz
Source1:        LICENSE-GPL-2.0
Source2:        LICENSE-BSD-2-Clause
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(yaml-0.1)

%description
A fancy 1.2 YAML and JSON parser/writer.

%package        devel
Summary:        Development files for libfyaml
Requires:       %{name} = %{version}-%{release}

%description   devel
Header files and libraries for libfyaml.

%prep -a
cp %{SOURCE1} .
cp %{SOURCE2} .

%conf -p
autoreconf -fiv

%ldconfig_scriptlets

%files
%license LICENSE LICENSE-GPL-2.0 LICENSE-BSD-2-Clause
%doc README.md AUTHORS
%{_bindir}/fy-*
%{_libdir}/libfyaml.so.0*
%{_mandir}/man1/fy-*.1*

%files devel
%{_includedir}/libfyaml.h
%{_libdir}/libfyaml.so
%{_libdir}/pkgconfig/libfyaml.pc

%changelog
%{?autochangelog}
