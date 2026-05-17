# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofpdi
%define go_import_path  github.com/phpdave11/gofpdi

Name:           go-github-phpdave11-gofpdi
Version:        1.0.16
Release:        %autorelease
Summary:        Go Free PDF Document Importer
License:        MIT
URL:            https://github.com/phpdave11/gofpdi
#!RemoteAsset:  sha256:2ce333b99f3573339c813af0b7263571b2fb4ed622090f1372e6c6c8d82331c7
Source0:        https://github.com/phpdave11/gofpdi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pkg/errors)

Provides:       go(github.com/phpdave11/gofpdi) = %{version}

Requires:       go(github.com/pkg/errors)

%description
gofpdi allows you to import an existing PDF into a new PDF.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
