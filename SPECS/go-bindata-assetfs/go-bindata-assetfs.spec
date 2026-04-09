# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-bindata-assetfs
%define go_import_path  github.com/elazarl/go-bindata-assetfs

Name:           go-bindata-assetfs
Version:        1.0.1
Release:        %autorelease
Summary:        Serves embedded files from `jteeuwen/go-bindata` with `net/http`
License:        BSD-2-Clause
URL:            https://github.com/elazarl/go-bindata-assetfs
#!RemoteAsset
Source0:        https://github.com/elazarl/go-bindata-assetfs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/elazarl/go-bindata-assetfs) = %{version}

%description
Serve embedded files from go-bindata (https://github.com/go-bindata/go-
bindata) with net/http.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
