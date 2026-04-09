# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <ialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfyaml
Version:        0.9.3
Release:        %autorelease
Summary:        Complete YAML parser and emitter
License:        MIT AND GPL-2.0-only AND BSD-2-Clause
URL:            https://github.com/pantoniou/libfyaml
#!RemoteAsset:  sha256:99ec52a528c629de11da7ead35ffa3c0e8cb548e4acafbd292db47535720f04c
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
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for libfyaml.

%prep -a
cp %{SOURCE1} .
cp %{SOURCE2} .

%conf -p
autoreconf -fiv

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
%autochangelog
