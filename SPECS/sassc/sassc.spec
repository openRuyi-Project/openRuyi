# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sassc
Version:        3.6.2
Release:        %autorelease
Summary:        Wrapper around libsass to compile CSS stylesheet
License:        MIT
URL:            http://github.com/sass/sassc
#!RemoteAsset:  sha256:608dc9002b45a91d11ed59e352469ecc05e4f58fc1259fc9a9f5b8f0f8348a03
Source0:        https://github.com/sass/sassc/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(libsass)

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.

%conf -p
autoreconf -fiv

%files
%license LICENSE
%doc Readme.md
%{_bindir}/sassc

%changelog
%autochangelog
