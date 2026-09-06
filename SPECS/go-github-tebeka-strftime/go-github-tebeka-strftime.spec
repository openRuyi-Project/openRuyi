# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strftime
%define go_import_path  github.com/tebeka/strftime

Name:           go-github-tebeka-strftime
Version:        0.1.5
Release:        %autorelease
Summary:        Python-compatible strftime implementation for Go
License:        MIT
URL:            https://github.com/tebeka/strftime
#!RemoteAsset:  sha256:0a0a22c57389e3c27585de9018a6d44198ee512ffe2fc1e7ab9c4ca876844659
Source0:        https://github.com/tebeka/strftime/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Strftime implements Python-style strftime time formatting directives for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
