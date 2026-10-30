# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xmlfmt
%define go_import_path  github.com/go-xmlfmt/xmlfmt

Name:           go-github-go-xmlfmt-xmlfmt
Version:        1.1.3
Release:        %autorelease
Summary:        XML formatting library for Go
License:        MIT
URL:            https://github.com/go-xmlfmt/xmlfmt
#!RemoteAsset:  sha256:b7f301168e17db0ee8c1010b8d680385d8e73ad61796bf531c297bb774de294d
Source0:        https://github.com/go-xmlfmt/xmlfmt/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-xmlfmt/xmlfmt) = %{version}

%description
XML formatting library for Go. This package contains the complete upstream
repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
