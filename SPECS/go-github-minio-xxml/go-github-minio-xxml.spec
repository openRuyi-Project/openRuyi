# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xxml
%define go_import_path  github.com/minio/xxml

Name:           go-github-minio-xxml
Version:        0.0.3
Release:        %autorelease
Summary:        Package xml implements a simple XML 1.0 parser that understands XML name spaces, extended support for control characters.
License:        BSD-3-Clause
URL:            https://github.com/minio/xxml
#!RemoteAsset
Source0:        https://github.com/minio/xxml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/minio/xxml) = %{version}

%description
Package xml implements a simple XML 1.0 parser that understands XML name
spaces, along with extended support for control characters such as
following

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
