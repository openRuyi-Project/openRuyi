# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           semver
%define go_import_path  github.com/Masterminds/semver

Name:           go-github-masterminds-semver
Version:        1.5.0
Release:        %autorelease
Summary:        Semantic version parsing and constraints for Go
License:        MIT
URL:            https://github.com/Masterminds/semver
#!RemoteAsset:  sha256:c9140eddfb03dc862f826e7761561260b9a840afa7519cc0919e89a43b5be5ba
Source0:        https://github.com/Masterminds/semver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/Masterminds/semver) = %{version}

%description
Semantic version parsing and constraints for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
