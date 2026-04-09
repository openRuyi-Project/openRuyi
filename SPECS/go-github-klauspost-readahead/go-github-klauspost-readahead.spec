# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           readahead
%define go_import_path  github.com/klauspost/readahead

Name:           go-github-klauspost-readahead
Version:        1.4.0
Release:        %autorelease
Summary:        Asynchronous read-ahead for Go readers
License:        MIT
URL:            https://github.com/klauspost/readahead
#!RemoteAsset
Source0:        https://github.com/klauspost/readahead/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/klauspost/readahead) = %{version}

%description
Asynchronous read-ahead for Go readers
This package will allow you to add readhead to any reader. This means a separate goroutine will perform reads from your upstream reader, so you can request from this reader without delay.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
