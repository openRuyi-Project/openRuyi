# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           filetype
%define go_import_path  github.com/h2non/filetype

Name:           go-github-h2non-filetype
Version:        1.1.3
Release:        %autorelease
Summary:        File type and MIME type detection for Go
License:        MIT
URL:            https://github.com/h2non/filetype
#!RemoteAsset:  sha256:21b2c24b9749448a7849035a2473beb4d032dc7243b4cf38f1bc5c9566da93c1
Source0:        https://github.com/h2non/filetype/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/h2non/filetype) = %{version}

%description
Filetype is a dependency-free Go package that infers file and MIME types from
magic number signatures. It supports extension and MIME lookup as well as
custom matchers.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
