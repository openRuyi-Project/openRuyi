# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           semver
%define go_import_path  github.com/Masterminds/semver

Name:           go-github-masterminds-semver
Version:        1.5.0
Release:        %autorelease
Summary:        Go library for semver
License:        MIT
URL:            https://github.com/Masterminds/semver
VCS:            git:https://github.com/Masterminds/semver.git
#!RemoteAsset:  sha256:c9140eddfb03dc862f826e7761561260b9a840afa7519cc0919e89a43b5be5ba
Source0:        https://github.com/Masterminds/semver/archive/v1.5.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n semver-1.5.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/Masterminds/semver) = %{version}

%description
This package provides the github.com/Masterminds/semver Go module source.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
