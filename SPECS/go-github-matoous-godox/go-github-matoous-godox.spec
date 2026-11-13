# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           godox
%define go_import_path  github.com/matoous/godox

Name:           go-github-matoous-godox
Version:        1.1.0
Release:        %autorelease
Summary:        Find keyword comments in Go source code
License:        MIT
URL:            https://github.com/matoous/godox
#!RemoteAsset:  sha256:853d7687cc9c0f13b965f46bac596b23f6abe39b433957e6d63373b8039a91a4
Source0:        https://github.com/matoous/godox/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/matoous/godox) = %{version}
Provides:       go(github.com/matoous/godox/fixtures/02) = %{version}

%description
Find keyword comments in Go source code.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n godox-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/matoous/godox

%changelog
%autochangelog
