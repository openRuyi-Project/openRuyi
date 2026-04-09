# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           http-parser
Version:        2.9.4
Release:        %autorelease
Summary:        HTTP request/response parser for C
License:        MIT
URL:            https://github.com/nodejs/http-parser
#!RemoteAsset
Source0:        https://github.com/nodejs/http-parser/archive/v%{version}/http-parser-%{version}.tar.gz
Source1:        meson.build
BuildSystem:    meson

# https://github.com/nodejs/http-parser/pull/483
Patch0:         0001-url-treat-empty-port-as-default.patch

BuildRequires:  meson
BuildRequires:  gcc

%description
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package        devel
Summary:        Development headers and libraries for http-parser
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and libraries for http-parser.

%prep -a
cp %{SOURCE1} .

%files
%license LICENSE-MIT
%doc AUTHORS README.md
%{_libdir}/libhttp_parser.so.*
%{_libdir}/libhttp_parser_strict.so.*

%files devel
%{_includedir}/http_parser.h
%{_libdir}/libhttp_parser.so
%{_libdir}/libhttp_parser_strict.so

%changelog
%autochangelog
