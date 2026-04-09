# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pgzip
%define go_import_path  github.com/klauspost/pgzip

Name:           go-github-klauspost-pgzip
Version:        1.2.6
Release:        %autorelease
Summary:        Go parallel gzip (de)compression
License:        MIT, BSD-3-Clause
URL:            https://github.com/klauspost/pgzip
#!RemoteAsset
Source0:        https://github.com/klauspost/pgzip/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/compress)

Provides:       go(github.com/klauspost/pgzip) = %{version}

Requires:       go(github.com/klauspost/compress)

%description
Go parallel gzip compression/decompression. This is a fully gzip compatible drop in replacement for "compress/gzip".

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
